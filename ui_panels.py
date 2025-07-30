import bpy

class VIEW3D_PT_simple_geo_nodes(bpy.types.Panel):
    bl_label = "Add Main Geometry Nodes for bake"
    bl_idname = "VIEW3D_PT_simple_geo_nodes"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'GeoNodes'

    def draw(self, context):
        layout = self.layout
        layout.operator("object.add_simple_geo_nodes", icon='MOD_NODES')

def register():
    bpy.utils.register_class(VIEW3D_PT_simple_geo_nodes)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_simple_geo_nodes)
