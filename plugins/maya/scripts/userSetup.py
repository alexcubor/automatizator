import maya.cmds as cmds


def add_shelf():
    shelf_name = "Automatizator"
    if not cmds.shelfLayout(shelf_name, ex=1):
        cmds.shelfLayout(shelf_name, p="ShelfLayout")
    shelves = cmds.shelfLayout(shelf_name, q=1, ca=1)
    if not shelves:
        shelves = []
    if "bc_editor" not in shelves:
        command = "from bc import editor; from importlib import reload; reload(editor); editor.run()"
        button_editor = cmds.shelfButton("bc_editor", parent=shelf_name, ann="Editor", width=37, height=37,
                        image="bc_logo.png", l="Editor", command=command, dcc="", imageOverlayLabel="",
                        olb=(0, 0, 0, 0), olc=(.9, .9, .9))
        cmds.shelfLayout(shelf_name, edit=True, position=[(button_editor, 1)])


cmds.evalDeferred("add_shelf()")
