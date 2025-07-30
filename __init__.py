bl_info = {
    "name": "Simple Geometry Nodes Creator",
    "blender": (4, 0, 0),
    "category": "Object",
    "author": "OpenAI",
    "description": "Добавляет Geometry Nodes через панель в N-панели"
}

import importlib

from . import ui_panel, operators, utils

def register():
    importlib.reload(ui_panel)
    importlib.reload(operators)
    importlib.reload(utils)

    operators.register()
    ui_panel.register()

def unregister():
    operators.unregister()
    ui_panel.unregister()
