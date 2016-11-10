import abc
import sys

class ABS_Manifest(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def write_to_manifest(self, manifest_path, hash_path, hash):
        """Use this base class to implement different manifest reports

        :param manifest_path: Path to the original file that the hash points to.
        :param hash_path: The path to the sidecar file which contains the hash file.
        :param hash: The hash value
        """
        pass
