import abc
class ABS_Manifest:
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def write_to_manifest(self, manifest_path, hash_path, hash):
        pass