# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

#  Imports
#  Python
import importlib

bl_info = {
    "name": "Import id Tech 3 BSP",
    "author": "SomaZ",
    "version": (0, 9, 92),
    "description": "Importer for id Tech 3 BSP maps",
    "blender": (3, 3, 0),
    "location": "File > Import-Export",
    "warning": "",
    "category": "Import-Export"
}

if "bpy" not in locals():
    import bpy
if "UI" in locals():
    importlib.reload(UI)
else:
    from . import UI


# ------------------------------------------------------------------------
#    store properties in the user preferences
# ------------------------------------------------------------------------
class BspImportAddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__
    base_path: bpy.props.StringProperty(
        name="basepath",
        description="Path to base folder",
        default="",
        subtype="DIR_PATH",
        maxlen=2048,
    )

    mod_path_0: bpy.props.StringProperty(
        name="mod path",
        description="Path to a mod folder",
        default="",
        subtype="DIR_PATH",
        maxlen=2048,
    )

    mod_path_1: bpy.props.StringProperty(
        name="additional mod path",
        description="Path to an addtional mod folder",
        default="",
        subtype="DIR_PATH",
        maxlen=2048,
    )

    def assetslibs_list_cb(self, context):
        if bpy.app.version >= (3, 0, 0):
            libs = context.preferences.filepaths.asset_libraries
            return [(lib.path, lib.name, "")
                    for lib in libs]
        else:
            return []

    assetlibrary: bpy.props.EnumProperty(
        items=assetslibs_list_cb,
        name="Asset Library",
        description="Asset library to use for packing models"
    )

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.prop(self, "base_path")
        row = layout.row()
        row.prop(self, "mod_path_0")
        row = layout.row()
        row.prop(self, "mod_path_1")
        if bpy.app.version >= (3, 0, 0):
            row = layout.row()
            row.prop(self, "assetlibrary")
            row.operator("q3.fill_asset_lib", text="Fill with models")


classes = (UI.Import_ID3_BSP,
           UI.Import_MAP,
           UI.Import_ID3_MD3,
           UI.Import_ID3_TIK,
           UI.Export_ID3_MD3,
           UI.Export_ID3_TIK,
           UI.Q3_PT_ShaderPanel,
           UI.Q3_PT_EntityPanel,
           UI.Reload_preview_shader,
           UI.Reload_render_shader,
           UI.DynamicProperties,
           UI.SceneProperties,
           UI.Add_property,
           UI.Del_property,
           UI.Add_entity_definition,
           UI.Add_key_definition,
           UI.Update_entity_definition,
           UI.Q3_PT_EntExportPanel,
           UI.ExportEnt,
           UI.PatchBspEntities,
           UI.PatchBspData,
           UI.Prepare_Lightmap_Baking,
           UI.Store_Vertex_Colors,
           UI.Create_Lightgrid,
           UI.Convert_Baked_Lightgrid,
           UI.Pack_Lightmap_Images,
           UI.Q3_PT_PropertiesEntityPanel,
           UI.Q3_PT_DescribtionEntityPanel,
           UI.Q3_PT_EditEntityPanel,
           UI.Q3_PT_DataExportPanel,
           BspImportAddonPreferences,
           UI.FillAssetLibrary,
           )


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_file_import.append(UI.menu_func_map_import)
    bpy.types.TOPBAR_MT_file_import.append(UI.menu_func_bsp_import)
    bpy.types.TOPBAR_MT_file_import.append(UI.menu_func_md3_import)
    bpy.types.TOPBAR_MT_file_import.append(UI.menu_func_tik_import)
    bpy.types.TOPBAR_MT_file_export.append(UI.menu_func_md3_export)
    bpy.types.TOPBAR_MT_file_export.append(UI.menu_func_tik_export)
    bpy.types.Object.q3_dynamic_props = bpy.props.PointerProperty(
        type=UI.DynamicProperties)
    bpy.types.Scene.id_tech_3_settings = bpy.props.PointerProperty(
        type=UI.SceneProperties)
    bpy.types.Scene.id_tech_3_importer_preset = bpy.props.StringProperty(
        name="id3 importer preset",
        description="Last used importer preset")
    bpy.types.Scene.id_tech_3_file_path = bpy.props.StringProperty(
        name="ID3 file path",
        description="Full path to the last imported id tech 3 File")
    bpy.types.Scene.id_tech_3_lightmaps_per_row = bpy.props.IntProperty(
        name="Lightmaps per row",
        description=(
            "How many lightmaps are packed in one row of the lightmap atlas"
            ))
    bpy.types.Scene.id_tech_3_lightmaps_per_column = bpy.props.IntProperty(
        name="Lightmaps per column",
        description=(
            "How many lightmaps are packed in one column of the lightmap atlas"
            ))


def unregister():
    bpy.types.TOPBAR_MT_file_import.remove(UI.menu_func_map_import)
    bpy.types.TOPBAR_MT_file_import.remove(UI.menu_func_bsp_import)
    bpy.types.TOPBAR_MT_file_import.remove(UI.menu_func_md3_import)
    bpy.types.TOPBAR_MT_file_import.remove(UI.menu_func_tik_import)
    bpy.types.TOPBAR_MT_file_export.remove(UI.menu_func_md3_export)
    bpy.types.TOPBAR_MT_file_export.remove(UI.menu_func_tik_export)
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
