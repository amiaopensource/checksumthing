import abc
import sys

class ABS_Manifest(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def write_to_manifest(self, manifest_path, hash_path, hash):
        pass
