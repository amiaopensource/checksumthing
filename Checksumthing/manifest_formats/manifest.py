class Manifest:
    """This is for dynamically loading the various manifest formats. In the strategy pattern, this is the context
    class.

    """
    def __init__(self, manifestStyle):
        """
        Used to choose the correct strategy for writing out a manifest.

        :param manifestStyle: Manifest pattern. This needs to implement the ABS_Manifest base class to conform.
        :type manifestStyle: ABS_Manifest
        """
        self._strategy = manifestStyle

    def add_line(self, manifest_path, hash_path, hash):

        self._strategy.write_to_manifest(manifest_path, hash_path, hash)