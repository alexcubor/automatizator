resources="$(cd "$(dirname "$0")" && pwd)"

pyside2-uic "${resources}/dialog.ui" -o "${resources}/../python/bc/ui/dialog.py"
echo "Converted:":$(realpath "${resources}/../python/bc/ui/dialog.py")

pyside2-uic "${resources}/widget_action.ui" -o "${resources}/../python/bc/ui/widget_action.py"
echo "Converted:":$(realpath "${resources}/../python/bc/ui/widget_action.py")

pyside2-uic "${resources}/widget_attr.ui" -o "${resources}/../python/bc/ui/widget_attr.py"
echo "Converted:":$(realpath "${resources}/../python/bc/ui/widget_attr.py")

pyside2-uic "${resources}/worker.ui" -o "${resources}/../python/bc/ui/worker.py"
echo "Converted:":$(realpath "${resources}/../python/bc/ui/worker.py")

pyside2-uic "${resources}/worker_action.ui" -o "${resources}/../python/bc/ui/worker_action.py"
echo "Converted:":$(realpath "${resources}/../python/bc/ui/worker_action.py")

pyside2-uic "${resources}/code_editor.ui" -o "${resources}/../python/bc/ui/code_editor.py"
echo "Converted:":$(realpath "${resources}/../python/bc/ui/code_editor.py")

pyside2-uic "${resources}/widget_button.ui" -o "${resources}/../python/bc/ui/widget_button.py"
echo "Converted:":$(realpath "${resources}/../python/bc/ui/widget_button.py")