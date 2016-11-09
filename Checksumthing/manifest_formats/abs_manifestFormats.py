import abc

class ABS_Manifest(metaclass=abc):

    @abc.abstractmethod
    def write_to_manifest(self):