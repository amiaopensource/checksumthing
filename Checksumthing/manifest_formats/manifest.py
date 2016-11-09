from .abs_manifestFormats import ABS_Manifest


class Manifest:
    def __init__(self, manifestStyle):
        self._strategy = manifestStyle

    def add_line(self, manifest_path, hash_path, hash):
        self._strategy(manifest_path, hash_path, hash)