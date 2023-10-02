# coding=utf-8
import os
import sys
import traceback
from PySide2 import QtCore, QtWidgets
import importlib
import traceback


'''
Здесь находится интерфейс чекера и сам его движок. Его можно наполнять неограниченным колличеством команд-чекеров. 
Все чекеры для удобства сложены в папку checkers, где каждый модуль является отдельным независимым чекером. 
Для добавления нового чекера надо добавить еще один файл.py в папку checkers и прописать его в __init__.py в этой же папке.
Он должен быть составлен по такому же принципу, как и другие модули в этой папке, 
то есть обязательно иметь класс Checker c функциями check и fix.
Так же чекер может включаться только при определённых условиях, заданных функцией enable() в каждой чекер-команде.
'''

version = "1.0"
date_update = ""


class Checker(QtWidgets.QDialog):
    def __init__(self, parent=None, dev=False):
        self.soft = soft_name()
        if parent:
            super(Checker, self).__init__(parent)
        else:
            QtWidgets.QWidget.__init__(self, parent, QtCore.Qt.WindowStaysOnTopHint)
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setGeometry(500, 300, 250, 110)
        self.setWindowTitle('Checker ' + version)
        #self.version = QtWidgets.QLabel("Версия %s" % version, self)
        #self.date = QtWidgets.QLabel(date_update, self)
        #hbox = QtWidgets.QHBoxLayout()
        #hbox.addWidget(self.version)
        #hbox.addWidget(self.date)
        #self.main_layout.addLayout(hbox)
        self.dev = dev
        self.checkers = self.get_checkers()
        if self.dev:
            print("[DEBUG][MAIN] list checkers", self.checkers)
        for checker in self.checkers:
            if self.dev:
                print("[DEBUG][MAIN] iter checker", checker)
            if not checker.enable:
                continue
            hbox = QtWidgets.QGridLayout()
            self.label = QtWidgets.QLabel(checker.name, self)
            print(checker)
            status = QtWidgets.QToolButton(self)
            status.setFocusPolicy(QtCore.Qt.NoFocus)
            status.setProperty("status", True)
            checker.status = status

            button = QtWidgets.QPushButton(self)
            button.setText("Проверка...")
            button.setMinimumWidth(120)
            button.setMaximumWidth(120)
            button.setFocusPolicy(QtCore.Qt.NoFocus)
            checker.button = button

            textbox = QtWidgets.QPlainTextEdit(self)
            textbox.resize(380, 40)
            textbox.setVisible(False)
            checker.info = textbox

            hbox.addWidget(status, 0, 0)
            hbox.addWidget(self.label, 0, 1)
            hbox.addWidget(button, 0, 2)
            hbox.addWidget(textbox, 1, 0, 1, 3)
            self.connect(button, QtCore.SIGNAL('clicked()'), checker.fix)

            self.main_layout.addLayout(hbox)
        from . import send
        if self.dev:
            from importlib import reload
            reload(send)
        send.Send(self.soft, self.main_layout, dev=self.dev)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

    def get_checkers(self):
        checkers = []
        modules_path = os.path.dirname(__file__) + "/checkers/" + self.soft
        modules = [os.path.splitext(c)[0] for c in os.listdir(modules_path) if "__" not in c]
        for module_name in modules:
            try:
                submodule_name = ".".join(["bc.checkers", self.soft, module_name])
                if self.dev:
                    print("[DEBUG][MAIN] Find checker", submodule_name)
                module = importlib.import_module(submodule_name)
                checker = module.Checker()
                if checker.enable:
                    checkers.append(checker)
            except Exception:
                traceback.print_exc()
        return checkers

    def start(self):
        for checker in self.checkers:
            if not checker.status:
                continue
            try:
                status = checker.check()
                if status == True:
                    checker.status.setStyleSheet("background-color: #148c07")
                    checker.status.setProperty("status", True)
                    checker.button.setStyleSheet("background-color: #148c07")
                    checker.button.setText("Успех")
                if status == False:
                    checker.status.setStyleSheet("background-color: #b00c00")
                    checker.status.setProperty("status", False)
                    checker.button.setStyleSheet("background-color: #b00c00")
                    checker.button.setText(checker.button_name)
                    checker.info.setVisible(True)
                if status == None:
                    checker.status.setStyleSheet("background-color: #d1ad0f")
                    checker.button.setStyleSheet("background-color: #d1ad0f")
                    checker.button.setText(checker.button_name)
                    checker.status.setProperty("status", "warning")
                    checker.info.setVisible(True)
            except:
                checker.status.setStyleSheet("background-color: #cc3d00")
                checker.button.setStyleSheet("background-color: #cc3d00")
                checker.button.setText("Ошибка")
                checker.status.setProperty("status", "warning")
                msg = traceback.format_exc()
                checker.info.setPlainText(msg)
                number_lines = min(len(msg.split("\n")), 10)
                checker.info.setMinimumHeight(number_lines * 40)
                checker.info.setVisible(True)
        self.send(ignore_warnings=False)

    def send(self, ignore_warnings=True):
        main_status = True
        for checker in self.checkers:
            if not checker.status:
                continue
            if checker.status.property("status") == "warning":
                if not ignore_warnings:
                    main_status = False
            else:
                if checker.status.property("status") == False:
                    main_status = False

        if main_status:
            # Подготовка перед отправкой
            import prepare
            if self.dev:
                from importlib import reload
                reload(prepare)
            prepare.Prepare(self.soft, self.main_layout, dev=self.dev)

            # Отправка на ферму
            import send
            if self.dev:
                from importlib import reload
                reload(send)
            send.Send(self.soft, self.main_layout)


def soft_name():
    if "maya" in sys.modules:
        return "maya"
    if "hou" in sys.modules:
        return "houdini"


def run(dev=False):
    parent = None
    if soft_name() == "maya":
        from maya import OpenMayaUI
        import shiboken2 as shiboken
        main_windows = OpenMayaUI.MQtUtil.mainWindow()
        parent = shiboken.wrapInstance(int(main_windows), QtWidgets.QWidget)
    dialog = Checker(parent=parent, dev=dev)
    dialog.show()
    dialog.start()
