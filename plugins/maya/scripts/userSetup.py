from bc import config
import maya.cmds as cmds
import maya.mel as mel


def add_menu():
    # Create a new menu item
    gMainWindow = mel.eval('$temp1=$gMainWindow')
    menu = cmds.menu(config.name(), label=config.name(), tearOff=True, parent=gMainWindow)
    # Add menu items to the new menu
    command = "from bc import editor; from importlib import reload; reload(editor); editor.run()"
    cmds.menuItem(label="Editor", parent=menu, command=command)


cmds.evalDeferred("add_menu()")


def add_shelf():
    app_name = "Automatizator"
    if not cmds.shelfLayout(app_name, ex=1):
        cmds.shelfLayout(app_name, p="ShelfLayout")
        command = "from bc import editor; from importlib import reload; reload(editor); editor.run()"
        button_editor = cmds.shelfButton("bc_editor", parent=app_name, ann="Editor", width=37, height=37,
                        image="bc_logo.png", l="Editor", command=command, dcc="", imageOverlayLabel="",
                        olb=(0, 0, 0, 0), olc=(.9, .9, .9))
        cmds.shelfLayout(app_name, edit=True, position=[(button_editor, 1)])


cmds.evalDeferred("add_shelf()")
