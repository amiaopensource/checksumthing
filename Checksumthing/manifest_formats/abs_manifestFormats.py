import abc
import sys

class ABS_Manifest(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def write_to_manifest(self, manifest_path, hash_path, hash):
        pass
