colmap feature_extractor --database_path database.db --image_path input --ImageReader.single_camera 1 --ImageReader.camera_model PINHOLE --SiftExtraction.use_gpu 1

colmap exhaustive_matcher --database_path database.db --SiftMatching.use_gpu 1

mkdir sparse

colmap mapper --database_path database.db --image_path input --output_path sparse --Mapper.ba_global_function_tolerance=0.000001

colmap image_undistorter --image_path input --input_path sparse/0 --output_path ./ --output_type COLMAP --max_image_size 2000 

mkdir dense

colmap patch_match_stereo --workspace_path dense --workspace_format COLMAP --PatchMatchStereo.geom_consistency true

colmap stereo_fusion --workspace_path dense --workspace_format COLMAP --input_type geometric --output_path dense/fused.ply