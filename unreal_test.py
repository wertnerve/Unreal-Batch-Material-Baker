import unreal

def extract_thumbnail(asset_path, output_path):
    asset = unreal.EditorAssetLibrary.load_asset(asset_path)
    if asset:
        thumbnail = unreal.ThumbnailTools.render_thumbnail(asset, 256, 256)
        if thumbnail:
            thumbnail.save_to_disk(output_path)
            print(f"Thumbnail saved to {output_path}")
            return output_path
    return None

# Example usage
print(unreal.is_editor())
asset_path = "C:/Users/tedst/Documents/unreal_test.py"
output_path = "C:/Users/tedst/Documents/Unreal Projects/TART5/Content/ "
extract_thumbnail(asset_path, output_path)
