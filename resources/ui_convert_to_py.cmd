rem for %%i in ("%~dp0.") do set "resources=%%~fi"
set resources=%~dp0

"%USERPROFILE%\AppData\Local\Programs\Python\Python37\Scripts\pyside2-uic.exe" "%resources%\dialog.ui" -o "%resources%\..\python\bc\ui\dialog.py"
echo Converted: %~dp0..\python\bc\ui\dialog.py

"%USERPROFILE%\AppData\Local\Programs\Python\Python37\Scripts\pyside2-uic.exe" "%resources%\widget_action.ui" -o "%resources%\..\python\bc\ui\widget_action.py"
echo Converted: %~dp0..\python\bc\ui\widget_action.py

"%USERPROFILE%\AppData\Local\Programs\Python\Python37\Scripts\pyside2-uic.exe" "%resources%\widget_attr.ui" -o "%resources%\..\python\bc\ui\widget_attr.py"
echo Converted: %~dp0..\python\bc\ui\widget_attr.py

"%USERPROFILE%\AppData\Local\Programs\Python\Python37\Scripts\pyside2-uic.exe" "%resources%\worker.ui" -o "%resources%\..\python\bc\ui\worker.py"
echo Converted: %~dp0..\python\bc\ui\worker.py

"%USERPROFILE%\AppData\Local\Programs\Python\Python37\Scripts\pyside2-uic.exe" "%resources%\worker_action.ui" -o "%resources%\..\python\bc\ui\worker_action.py"
echo Converted: %~dp0..\python\bc\ui\worker_action.py

"%USERPROFILE%\AppData\Local\Programs\Python\Python37\Scripts\pyside2-uic.exe" "%resources%\code_editor.ui" -o "%resources%\..\python\bc\ui\code_editor.py"
echo Converted: %~dp0..\python\bc\ui\code_editor.py

"%USERPROFILE%\AppData\Local\Programs\Python\Python37\Scripts\pyside2-uic.exe" "%resources%\widget_button.ui" -o "%resources%\..\python\bc\ui\widget_button.py"
echo Converted: %~dp0..\python\bc\ui\widget_button.py