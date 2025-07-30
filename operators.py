import bpy
from .utils import create_geometry_node_group

class OBJECT_OT_add_geo_nodes(bpy.types.Operator):
    bl_idname = "object.add_simple_geo_nodes"
    bl_label = "Добавить Geometry Nodes"
    bl_description = "Добавляет модификатор с нод-группой"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        if not obj:
            self.report({'WARNING'}, "Нет активного объекта")
            return {'CANCELLED'}

        group = create_geometry_node_group()
        mod = obj.modifiers.new("SimpleGN", 'NODES')
        mod.node_group = group

        self.report({'INFO'}, "Geometry Nodes добавлены")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(OBJECT_OT_add_geo_nodes)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_add_geo_nodes)
