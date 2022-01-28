bl_info = {
    "name": "Render Pass",
    "author": "SMK RUS Developer Team",
    "version": (1, 0),
    "blender": (2, 92, 0),
    "location": "View3D > UI > PASS",
    "description": "buat gampang atur pass",
    "warning": "",
    "doc_url": "",
    "category": "Add On",
}




import bpy


class SceneRender_Pass(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Render Pass"
    bl_idname = "RDR_PT_pass"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "PASS"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        row = layout.row()
        row.label(text="Render Pass")
        
        row = layout.row()
        row.operator("rdr.render_pass")



class RDR_Scene_Passes(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "rdr.render_pass"
    bl_label = "Render Pass"
    
    
    def execute(self, context):
        
        def Scene_AO():
            
            bpy.data.scenes["AO"].render.engine = 'CYCLES'
            bpy.data.scenes["AO"].cycles.feature_set = 'SUPPORTED'
            bpy.data.scenes["AO"].cycles.device = 'GPU'
            bpy.data.scenes["AO"].cycles.progressive = 'PATH' 
            bpy.data.scenes["AO"].cycles.samples = 128
            bpy.data.scenes["AO"].cycles.preview_samples = 64
            bpy.data.scenes["AO"].cycles.use_adaptive_sampling = True
            bpy.data.scenes["AO"].cycles.adaptive_threshold = 0.01
            bpy.data.scenes["AO"].cycles.adaptive_min_samples = 64
            bpy.data.scenes["AO"].render.use_simplify = True
            bpy.data.scenes["AO"].display_settings.display_device = 'sRGB'
            bpy.data.scenes["AO"].view_settings.view_transform = 'Standard'
            bpy.data.scenes["AO"].view_settings.look = 'None'
            bpy.data.scenes["AO"].view_settings.exposure = 0
            bpy.data.scenes["AO"].view_settings.gamma = 1
            bpy.data.scenes["AO"].sequencer_colorspace_settings.name = 'sRGB'
            bpy.data.scenes["AO"].render.resolution_x = 1920
            bpy.data.scenes["AO"].render.resolution_y = 1080
            bpy.data.scenes["AO"].render.resolution_percentage = 100
            bpy.data.scenes["AO"].render.pixel_aspect_x = 1
            bpy.data.scenes["AO"].render.pixel_aspect_y = 1
            bpy.data.scenes["AO"].frame_start = 1
            bpy.data.scenes["AO"].frame_end = 1
            bpy.data.scenes["AO"].frame_step = 1
            bpy.data.scenes["AO"].render.fps = 25
            bpy.data.scenes["AO"].render.fps_base = 1
            bpy.data.scenes["AO"].render.use_stamp_date = True
            bpy.data.scenes["AO"].render.use_stamp_time = True
            bpy.data.scenes["AO"].render.use_stamp_render_time = True
            bpy.data.scenes["AO"].render.use_stamp_frame = True
            bpy.data.scenes["AO"].render.use_stamp_lens = True
            bpy.data.scenes["AO"].render.use_stamp_camera = True
            bpy.data.scenes["AO"].render.use_stamp_scene = True
            bpy.data.scenes["AO"].render.use_stamp_filename = True
            bpy.data.scenes["AO"].view_layers["AO"].use = True
            
            #data
            bpy.data.scenes["AO"].view_layers["AO"].use_pass_combined = True
            bpy.data.scenes["AO"].view_layers["AO"].use_pass_z = False
            bpy.data.scenes["AO"].view_layers["AO"].pass_alpha_threshold = 0.5
            bpy.data.scenes["AO"].view_layers["AO"].use_pass_ambient_occlusion = True
            bpy.data.scenes["AO"].view_layers["AO"].pass_cryptomatte_depth = 6
            bpy.data.scenes["AO"].view_layers["AO"].use_pass_cryptomatte_accurate = True
            
            #filter
            bpy.data.scenes["AO"].view_layers["AO"].use_solid = True
            bpy.data.scenes["AO"].view_layers["AO"].use_volumes = True
            bpy.data.scenes["AO"].view_layers["AO"].use_sky = False
            bpy.data.scenes["AO"].view_layers["AO"].use_ao = False
            bpy.data.scenes["AO"].view_layers["AO"].use_strand = False
        
        
        
        def Scene_BG():
            
            bpy.data.scenes["BG"].render.engine = 'CYCLES'
            bpy.data.scenes["BG"].cycles.feature_set = 'SUPPORTED'
            bpy.data.scenes["BG"].cycles.device = 'GPU'
            
            #Sampling
            bpy.data.scenes["BG"].cycles.progressive = 'PATH'
            bpy.data.scenes["BG"].cycles.samples = 128
            bpy.data.scenes["BG"].cycles.preview_samples = 34
            
            #Adaptive Sampling 
            bpy.data.scenes["BG"].cycles.use_adaptive_sampling = True
            bpy.data.scenes["BG"].cycles.adaptive_threshold = 0.01
            bpy.data.scenes["BG"].cycles.adaptive_min_samples = 0
            
            #Simplify
            bpy.data.scenes["BG"].render.use_simplify = True
            bpy.data.scenes["BG"].render.simplify_subdivision_render = 6
            bpy.data.scenes["BG"].render.simplify_child_particles_render = 1
            bpy.data.scenes["BG"].cycles.texture_limit_render = 'OFF'
            
            #Transparent
            bpy.data.scenes["BG"].render.film_transparent = True
            bpy.data.scenes["BG"].cycles.film_transparent_glass = True
            bpy.data.scenes["BG"].cycles.film_transparent_roughness = 0.1
            
            #Color Management
            bpy.data.scenes["BG"].display_settings.display_device = 'sRGB'
            bpy.data.scenes["BG"].view_settings.view_transform = 'Standard'
            bpy.data.scenes["BG"].view_settings.look = 'None'
            bpy.data.scenes["BG"].view_settings.exposure = 0
            bpy.data.scenes["BG"].view_settings.gamma = 1
            bpy.data.scenes["BG"].sequencer_colorspace_settings.name = 'sRGB'
            
            #Output
            bpy.data.scenes["BG"].render.image_settings.color_mode = 'RGBA'
            bpy.data.scenes["BG"].render.use_placeholder = True
            bpy.data.scenes["BG"].render.image_settings.color_depth = '8'
            
            #Metadata
            bpy.data.scenes["BG"].render.use_stamp_date = True
            bpy.data.scenes["BG"].render.use_stamp_time = True
            bpy.data.scenes["BG"].render.use_stamp_render_time = True
            bpy.data.scenes["BG"].render.use_stamp_frame = True
            bpy.data.scenes["BG"].render.use_stamp_camera = True
            bpy.data.scenes["BG"].render.use_stamp_lens = True
            bpy.data.scenes["BG"].render.use_stamp_scene = True
            bpy.data.scenes["BG"].render.use_stamp_filename = True
            
            #Post Processing 
            bpy.data.scenes["BG"].render.use_compositing = True
            bpy.data.scenes["BG"].render.use_sequencer = True
            bpy.data.scenes["BG"].render.dither_intensity = 1
            
            #View layer 
            bpy.data.scenes["BG"].view_layers["B"].use = True
            
            #View layer data
            bpy.data.scenes["BG"].view_layers["B"].use_pass_combined = True
            bpy.data.scenes["BG"].view_layers["B"].cycles.denoising_store_passes = True
            bpy.data.scenes["BG"].view_layers["B"].pass_alpha_threshold = 0.5
            
            #View layer filter 
            bpy.data.scenes["BG"].view_layers["B"].use_sky = True
            bpy.data.scenes["BG"].view_layers["B"].use_ao = True
            bpy.data.scenes["BG"].view_layers["B"].use_ao = True
            bpy.data.scenes["BG"].view_layers["B"].use_strand = True
            bpy.data.scenes["BG"].view_layers["B"].use_volumes = True
        
        
        
        def Scene_MAIN():

            
            ## Render Properties MAIN
            bpy.data.scenes["MAIN"].render.engine = 'CYCLES'
            bpy.data.scenes["MAIN"].cycles.device = 'GPU'

            # Adaptive sampling
            bpy.data.scenes["MAIN"].cycles.use_adaptive_sampling = True
            bpy.data.scenes["MAIN"].cycles.adaptive_threshold = 0.01
            bpy.data.scenes["MAIN"].cycles.adaptive_min_samples = 64

            # Denoising viewport
            bpy.data.scenes["MAIN"].cycles.preview_denoiser = 'OPTIX'

            # Simplify
            bpy.data.scenes["MAIN"].render.use_simplify = True

            # Film
            bpy.data.scenes["MAIN"].render.film_transparent = True
            bpy.data.scenes["MAIN"].cycles.film_transparent_glass = True
            bpy.data.scenes["MAIN"].cycles.film_transparent_roughness = 0.10

            # Color Management
            bpy.data.scenes["MAIN"].view_settings.view_transform = 'Standard'

            ## Output Properties Main
            # Dimensions
            bpy.data.scenes["MAIN"].frame_end = 1
            bpy.data.scenes["MAIN"].render.fps = 25

            # Metadata
            bpy.data.scenes["MAIN"].render.use_stamp_lens = True

            ## View Layer Properties Main
            # Data
            bpy.data.scenes["MAIN"].view_layers["M"].use_pass_z = False
            bpy.data.scenes["MAIN"].view_layers["M"].cycles.denoising_store_passes = True
        
        
        
        def Scene_SH():
            
             bpy.data.scenes["SH"].render.engine = 'CYCLES'
             bpy.data.scenes["SH"].cycles.device = 'GPU'
             bpy.data.scenes["SH"].cycles.progressive = 'PATH' 
             bpy.data.scenes["SH"].cycles.samples = 128
             bpy.data.scenes["SH"].cycles.preview_samples = 64
             bpy.data.scenes["SH"].cycles.use_adaptive_sampling = True
             bpy.data.scenes["SH"].cycles.adaptive_threshold = 0.01
             bpy.data.scenes["SH"].cycles.adaptive_min_samples = 64
             bpy.data.scenes["SH"].render.use_simplify = True
             bpy.data.scenes["SH"].display_settings.display_device = 'sRGB'
             bpy.data.scenes["SH"].view_settings.view_transform = 'Standard'
             bpy.data.scenes["SH"].view_settings.look = 'None'
             bpy.data.scenes["SH"].view_settings.exposure = 0
             bpy.data.scenes["SH"].view_settings.gamma = 1
             bpy.data.scenes["SH"].sequencer_colorspace_settings.name = 'sRGB'
             bpy.data.scenes["SH"].render.resolution_x = 1920
             bpy.data.scenes["SH"].render.resolution_y = 1080
             bpy.data.scenes["SH"].render.resolution_percentage = 100
             bpy.data.scenes["SH"].render.pixel_aspect_x = 1
             bpy.data.scenes["SH"].render.pixel_aspect_y = 1
             bpy.data.scenes["SH"].frame_start = 1
             bpy.data.scenes["SH"].frame_end = 1
             bpy.data.scenes["SH"].frame_step = 1
             bpy.data.scenes["SH"].render.fps = 25
             bpy.data.scenes["SH"].render.fps_base = 1
             bpy.data.scenes["SH"].render.use_stamp_date = True
             bpy.data.scenes["SH"].render.use_stamp_time = True
             bpy.data.scenes["SH"].render.use_stamp_render_time = True
             bpy.data.scenes["SH"].render.use_stamp_frame = True
             bpy.data.scenes["SH"].render.use_stamp_lens = True
             bpy.data.scenes["SH"].render.use_stamp_camera = True
             bpy.data.scenes["SH"].render.use_stamp_scene = True
             bpy.data.scenes["SH"].render.use_stamp_filename = True
             bpy.data.scenes["SH"].view_layers["SD"].pass_alpha_threshold = 0.5
             bpy.data.scenes["SH"].view_layers["SD"].use_pass_ambient_occlusion = True
             bpy.data.scenes["SH"].view_layers["SD"].pass_cryptomatte_depth = 6
             bpy.data.scenes["SH"].view_layers["SD"].use_pass_cryptomatte_accurate = True
             bpy.data.scenes["SH"].view_layers["SD"].use_solid = True
             bpy.data.scenes["SH"].view_layers["SD"].use_volumes = True
             bpy.data.scenes["SH"].view_layers["SD"].use = True
        
        
        
        def Scene_UT():
            
            #RENDER ENGINE
            bpy.data.scenes["UT"].render.engine = 'CYCLES'
            
            #FEATURE SET
            bpy.data.scenes["UT"].cycles.feature_set = 'SUPPORTED'
            
            #DEVICE
            bpy.data.scenes["UT"].cycles.device = 'CPU'
            
            #SAMPLING
            bpy.data.scenes["UT"].cycles.samples = 128
            bpy.data.scenes["UT"].cycles.preview_samples = 32
            
            #SIMPLIFY
            bpy.data.scenes["UT"].render.use_simplify = True
            bpy.data.scenes["UT"].render.simplify_subdivision_render = 6
            bpy.data.scenes["UT"].render.simplify_child_particles_render = 1
            bpy.data.scenes["UT"].cycles.texture_limit_render = '128'
            
            #FILM
            bpy.data.scenes["UT"].cycles.film_exposure = 1
            bpy.data.scenes["UT"].cycles.pixel_filter_type = 'BLACKMAN_HARRIS'
            bpy.data.scenes["UT"].cycles.filter_width = 1.5
            bpy.data.scenes["UT"].render.film_transparent = True
            bpy.data.scenes["UT"].cycles.film_transparent_glass = True
            bpy.data.scenes["UT"].cycles.film_transparent_roughness = 0.1
            
            #COLOR MANAGEMENT
            bpy.data.scenes["UT"].display_settings.display_device = 'sRGB'
            bpy.data.scenes["UT"].view_settings.view_transform = 'Standard'
            bpy.data.scenes["UT"].view_settings.look = 'None'
            bpy.data.scenes["UT"].view_settings.exposure = 0
            bpy.data.scenes["UT"].view_settings.gamma = 1
            bpy.data.scenes["UT"].sequencer_colorspace_settings.name = 'sRGB'
            
            #DIMENSION
            bpy.data.scenes["UT"].render.resolution_percentage = 100
            
            #OUTPUT
            bpy.data.scenes["UT"].render.image_settings.file_format = 'OPEN_EXR_MULTILAYER'
            bpy.data.scenes["UT"].render.image_settings.color_depth = '16'
            
            #METADATA
            bpy.data.scenes["UT"].render.use_stamp_date = True
            bpy.data.scenes["UT"].render.use_stamp_time = True
            bpy.data.scenes["UT"].render.use_stamp_render_time = True
            bpy.data.scenes["UT"].render.use_stamp_frame = True
            bpy.data.scenes["UT"].render.use_stamp_frame_range = False
            bpy.data.scenes["UT"].render.use_stamp_memory = False
            bpy.data.scenes["UT"].render.use_stamp_hostname = False
            bpy.data.scenes["UT"].render.use_stamp_camera = True
            bpy.data.scenes["UT"].render.use_stamp_lens = True
            bpy.data.scenes["UT"].render.use_stamp_scene = True
            bpy.data.scenes["UT"].render.use_stamp_marker = False
            
            #PASSED/DATA
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_combined = True
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_z = False
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_mist = False
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_normal = False
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_vector = False
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_uv = False
            
            #PASSED/LIGHT
            #DIFFUSE
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_diffuse_color = True
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_diffuse_indirect = True
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_diffuse_direct = True
            #GLOSSY
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_glossy_color = True
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_transmission_indirect = True
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_glossy_direct = True
            
            #TRANSMISSION
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_transmission_color = True
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_transmission_indirect = True
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_transmission_direct = True 
            
            #VOLUME
            bpy.data.scenes["UT"].view_layers["CR"].cycles.use_pass_volume_direct = True
            bpy.data.scenes["UT"].view_layers["CR"].cycles.use_pass_volume_indirect = True
            
            #OTHER
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_ambient_occlusion = False
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_shadow = False
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_emit = False
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_environment = False 
        
            #PASSED/CRYPTOMATTE
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_cryptomatte_object = True
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_cryptomatte_material = True
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_cryptomatte_asset = True
            bpy.data.scenes["UT"].view_layers["CR"].pass_cryptomatte_depth = 6
            bpy.data.scenes["UT"].view_layers["CR"].use_pass_cryptomatte_accurate = True
            
            #PASSED/FILTER
            bpy.data.scenes["UT"].view_layers["CR"].use_ao = False
            bpy.data.scenes["UT"].view_layers["CR"].use_sky = False
            bpy.data.scenes["UT"].view_layers["CR"].use_solid = True
            bpy.data.scenes["UT"].view_layers["CR"].use_strand = False
            bpy.data.scenes["UT"].view_layers["CR"].use_volumes = True
            
            #PASSED/DATA
            bpy.data.scenes["UT"].view_layers["UT"].use_pass_combined = True
            bpy.data.scenes["UT"].view_layers["UT"].use_pass_z = True
            bpy.data.scenes["UT"].view_layers["UT"].use_pass_mist = True
            bpy.data.scenes["UT"].view_layers["UT"].use_pass_normal = True
            bpy.data.scenes["UT"].view_layers["UT"].use_pass_vector = True
            bpy.data.scenes["UT"].view_layers["UT"].use_pass_uv = True
        
        
        
        # get children collection
        def collection_Children( col, colTarget, colPathDict, calPathPrntDict ) :
            
            children_col = col
            child = col.children
            if len( child ) > 0 :
                for chd in child :
                    if chd.name == colTarget :
                        
                        # add collection path children to dictionary
                        colPathDict[chd.name] = chd
                        calPathPrntDict[chd.name] = children_col
                        break
                    
                    else :
                        collection_Children( chd, colTarget, colPathDict, calPathPrntDict )
        
        
        
        # exclude layer collection
        def collection_Exclude( viewLayer, layerCollection, EXCLUDE=True ) :
            
            # get collection exclude
            layerCollection = [LC.replace("_EXCLUDE", "") for LC in layerCollection if LC.endswith("EXCLUDE")]
            
            # get path collection
            collPath_Dictionary = {} # dictionary collection path
            collPathParent_Dictionary = {} # dictionary collection parent path
            children_col = viewLayer.layer_collection.children
            for LC in layerCollection :
                if len(children_col) > 0 :
                    for exclude in children_col :
                         collection_Children( exclude, LC, collPath_Dictionary, collPathParent_Dictionary )
            
            #print( self.collPath_Dictionary[layerCollection[1]] )
            #print( self.collPathParent_Dictionary[layerCollection[1]] )
            
            # make exclude layer collection
            for colls in collPath_Dictionary :
                coll_exclude = collPath_Dictionary[colls]
                if EXCLUDE :
                    coll_exclude.exclude = True
                    
        
        
        
        def create_SceneLayer( default_scene, dict_scene_layer ) :
            pass
            
            scenes = bpy.data.scenes # all scenes
            list_scenes = [ scn.name for scn in scenes ]
            for scenePass in dict_scene_layer :
                if scenePass not in scenes :
                    
                    # create scene pass
                    #SP = bpy.data.scenes.new( name=scenePass ) # new scene
                    SP = default_scene.copy() # copy scene
                    SP.use_fake_user = True
                    SP.name = scenePass
                    bpy.context.window.scene = SP # switch / change scene
                    
                    # first / default view layer
                    VL = SP.view_layers[0].name = dict_scene_layer[scenePass][0][0]
                    collection_Exclude( SP.view_layers[0], [col for col in dict_scene_layer[scenePass][1][0]] )
                    
                    if scenePass == "AO":
                        Scene_AO()
                    elif scenePass == "BG" :
                        Scene_BG()
                    elif scenePass == "MAIN" :
                        Scene_MAIN()
                    elif scenePass == "SH" :
                        Scene_SH()
                    #elif scenePass == "UT" :
                    #    self.Scene_UT()
                    
                    # add more view layers
                    for viewLayerPass in zip( dict_scene_layer[scenePass][0], dict_scene_layer[scenePass][1] ) : # add some view layer
                        if viewLayerPass[0] == VL :
                            continue
                        
                        # create view layer
                        VL = SP.view_layers.new( name=viewLayerPass[0] )
                        collection_Exclude( VL, [col for col in viewLayerPass[1]] )
                        
                        
                        bpy.context.window.view_layer = VL # switch / change view layer
                        if scenePass == "UT" and viewLayerPass[0] == "UT" :
                            Scene_UT()
                        
                        
                else :
                    
                    if scenePass == "AO" :
                        Scene_AO()
                    elif scenePass == "BG" :
                        Scene_BG()
                    elif scenePass == "MAIN" :
                        Scene_MAIN()
                    elif scenePass == "SH" :
                        Scene_SH()
                    elif scenePass == "UT" :
                        Scene_UT()
                    
                    viewLayers = bpy.data.scenes[scenePass].view_layers # all view layers
                    list_viewLayers = [ vlyr.name for vlyr in viewLayers ]
                    for viewLayerPass in zip( dict_scene_layer[ scenePass ][0], dict_scene_layer[ scenePass ][1] ) : # add some view layer
                        if viewLayerPass[0] not in list_viewLayers :
                            
                            # create view layer
                            VL = viewLayers.new( name=viewLayerPass[0] )
                            collection_Exclude( VL, [col for col in viewLayerPass[1]] )
        
        
        
        # change name scene default
        defautNameScene = "ALL"
        default_scene = bpy.context.scene
        default_scene.name = defautNameScene
        
        default_scene.render.engine = 'CYCLES'
        default_scene.cycles.feature_set = 'SUPPORTED'
        default_scene.cycles.device = 'GPU'
        
        # get outliner area
        screen_areas = bpy.context.screen.areas
        for SA in screen_areas :
            if SA.type == "OUTLINER" :
                outliner_area = SA
                break

        # another way
        #outliner_area = next(a for a in bpy.context.screen.areas if a.type == "OUTLINER")

        # restriction toggles
        space = outliner_area.spaces[0]
        space.show_restrict_column_enable = True  # Collection exclusion (Checkbox icon)
        space.show_restrict_column_select = True  # Selection state (Cursor icon)
        space.show_restrict_column_hide = True  # Local visibility (Eye icon)
        space.show_restrict_column_viewport = True  # Global visibility (Monitor icon)
        space.show_restrict_column_render = True  # Render visibility (Camera icon)
        space.show_restrict_column_holdout = True  # Holdout
        space.show_restrict_column_indirect_only = True  # Indirect only
        
        # dictionary scene with view layer "scene" : ( ["view layer"], ["collection exclude"] )
        
        dict_scene_layer = {
                             "AO"   : ( [ "AO", "CO" ], [ ["Dome_EXCLUDE", "Hidden_AO_EXCLUDE", "Lighting_EXCLUDE", "Hidden_All_EXCLUDE"],
                                                          ["Dome_EXCLUDE", "Hidden_AO_EXCLUDE", "Lighting_EXCLUDE", "Hidden_All_EXCLUDE"] ] ),
                             
                             "BG"   : ( [ "B" ], [ ["Chars_EXCLUDE", "Envi_EXCLUDE", "Props_EXCLUDE", "Floor_EXCLUDE", "FX_EXCLUDE", "Hidden_AO_EXCLUDE", "Hidden_MAIN_EXCLUDE", "Hidden_SH_EXCLUDE", "Hidden_UT_EXCLUDE", "Hidden_CRypto_EXCLUDE", "Hidden_WallAO_EXCLUDE", "Hidden_All_EXCLUDE"] ] ),
                             
                             "MAIN" : ( [ "M", "RM" ], [ ["Floor_EXCLUDE", "Hidden_MAIN_EXCLUDE", "Hidden_All_EXCLUDE"],
                                                        ["Envi_EXCLUDE", "Dome_EXCLUDE", "Floor_EXCLUDE", "Hidden_All_EXCLUDE"] ] ),
                             
                             "SH"   : ( [ "SD", "SH" ], [ ["Chars_EXCLUDE", "Envi_EXCLUDE", "Props_EXCLUDE", "Dome_EXCLUDE", "Hidden_SH_EXCLUDE", "Hidden_All_EXCLUDE"],
                                                          ["Dome_EXCLUDE", "Hidden_SH_EXCLUDE", "Hidden_All_EXCLUDE"] ] ),
                             
                             "UT"   : ( [ "CR", "UT" ], [ ["Floor_EXCLUDE", "Hidden_UT_EXCLUDE", "Lighting_EXCLUDE", "Hidden_All_EXCLUDE"],
                                                          ["Floor_EXCLUDE", "Hidden_UT_EXCLUDE", "Lighting_EXCLUDE", "Hidden_All_EXCLUDE"] ] )
        }
        
        create_SceneLayer( default_scene, dict_scene_layer )
        
        
        return {'FINISHED'}



classes = [ SceneRender_Pass, RDR_Scene_Passes ]

def register():
    for cls in classes :
        bpy.utils.register_class( cls )
    

def unregister():
    for cls in classes :
        bpy.utils.unregister_class( cls )


if __name__ == "__main__":
    register()
    #unregister()



