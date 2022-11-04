# copy from addon template
bl_info = {
    "name": "TextTool",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (3, 2, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}

#copy from UI panel simple
import bpy


class VIEW3D_PT_TextTool(bpy.types.Panel):

    bl_label = "Text Tool"
    bl_idname = "VIEW3D_PT_TextTool"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Text Tool"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("wm.text_tool", text = 'Add Text')



class WM_OT_text_tool(bpy.types.Operator): # WM Wndow manager 
    bl_label = 'Text Tool Operator'
    bl_idname = 'wm.text_tool'

    text : bpy.props.StringProperty(name = 'Enter Text: ')
    scale : bpy.props.FloatProperty(name = 'Scale', default=1)
    center : bpy.props.BoolProperty(name = 'Center Origin', default=False)
    
    def execute(self, context):
        t = self.text
        s = self.scale
        c = self.center
        
        #edit mode = True
        bpy.ops.object.text_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        
        # delete font, change parameter, search in API
        bpy.ops.font.delete(type='PREVIOUS_WORD')
        # add words
        bpy.ops.font.text_insert(text=self.text)
        bpy.ops.object.editmode_toggle()
        
        if c == True:
            bpy.context.object.data.align_x = 'CENTER'
            bpy.context.object.data.align_y = 'CENTER'



        
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)





def register():
    bpy.utils.register_class(VIEW3D_PT_TextTool)
    bpy.utils.register_class(WM_OT_text_tool)


def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_TextTool)
    bpy.utils.unregister_class(WM_OT_text_tool)


if __name__ == "__main__":
    register()
