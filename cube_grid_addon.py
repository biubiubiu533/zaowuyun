bl_info = {
    "name": "Cube Grid",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > CubeGrid Tab",
    "description": "Adds a cube grid",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}

import bpy


class VIEW3D_PT_cube_grid(bpy.types.Panel):
    
    bl_label = "Add cube grid"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'CubeGrid'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Hello world!", icon='WORLD_DATA')

        row = layout.row()
        row.operator('mesh.cube_grid')



class MESH_OT_cube_grid(bpy.types.Operator):
    """Add cube grid"""
    bl_idname = 'mesh.cube_grid'
    bl_label = 'Add cube grid'
    bl_options = {'REGISTER', 'UNDO'}
    
    count_x : bpy.props.IntProperty(
            name = 'X',
            description = 'number of cubes in X axis',
            default = 5,
            min = 1, soft_max = 10)
    count_y : bpy.props.IntProperty(
            name = 'Y',
            description = 'number of cubes in Y axis',
            default = 5,
            min = 1, max = 10)
    count_z : bpy.props.IntProperty(
            name = 'Z',
            description = 'number of cubes in Z axis',
            default = 5,
            min = 1, max = 10)
    
    
    @classmethod
    def poll(cls, context):
        print(f'current context is {context.area.type}')
        if context.area.type == 'VIEW_3D':
            return True
        else:
            return False
    
    
    
    def execute(self, context):
        
        x = self.count_x
        y = self.count_y
        z = self.count_z

        for i in range(x):
            for j in range(y):
                for k in range(z):
                    bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(i*2, j*2, k*2), scale=(1, 1, 1))
        
        return {'FINISHED'}




def register():
    bpy.utils.register_class(VIEW3D_PT_cube_grid)


def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_cube_grid)


if __name__ == "__main__":
    register()