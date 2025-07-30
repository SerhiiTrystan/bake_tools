import bpy


    # Создаём узлы
    cube = nodes.new("GeometryNodeMeshCube")
    cube.location = (-300, 0)

    transform = nodes.new("GeometryNodeTransform")
    transform.location = (0, 0)
    transform.inputs['Translation'].default_value = (0, 0, 1)

    output = nodes.new("NodeGroupOutput")
    output.location = (300, 0)

    links.new(cube.outputs["Mesh"], transform.inputs["Geometry"])
    links.new(transform.outputs["Geometry"], output.inputs["Geometry"])

    return node_group

    def create_geo_node_group(group_name="MainNG"):
    #добавление группы нодов
        if group_name in bpy.data.node_groups:
            return bpy.data.node_groups[group_name]

        node_group = bpy.data.node_groups.new(group_name, 'GeometryNodeTree')

    #чистим сокеты
        while node_group.inputs:
            node_group.inputs.romove(node_group.inputs[0])
        while node_group.outputs:
            node_group.outputs.remove(node_group.outputs[0])
        
        node_group.outputs.new("NodeSocketGeometry", "Geometry")

        nodes = node_group.nodes
        links = node_group.links
        nodes.clear()

        #создаем систему узлов

        inp_nd = nodes.new(type='NodeGroupInput')
        inp_nd.lacation = (,)
        
        out_nd = nodes.new(type='NodeGroupOutput')
        out_nd.location = (,)

        nm_attrb = nodes.new(type='GeometryNodeStoreNamedAttribute')
        nm_attrb.location = (,)