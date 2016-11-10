from .abs_manifestFormats import ABS_Manifest

class TextManifest(ABS_Manifest):
    def write_to_manifest(self, manifest_path, hash_path, hash):
                
        with open(manifest_path, "a") as f:
            f.write(hash + "\n")
            
        pass