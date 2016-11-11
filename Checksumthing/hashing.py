import os
import re
import warnings

# Always warn of Deprecations
warnings.simplefilter('always', DeprecationWarning)

hash_lengths = {'md5': 32,
                'sha1': 40,
                'sha256': 64,
}


def read_hash(filename, hash_length):
    """
    Reads the hash value in a given file

    :param filename: path to a file to read hash value
    :param hash_length: Length of a file
    :return: Hash value
    """

    # Question: can we better read this without knowing the length ahead of time? Could be better to refactor into a
    # factory pattern.

    with open(filename, 'r+') as f:
        text = f.read()
        regex = '([0-9a-f]{' + str(hash_length) + '})'
        m = re.search(regex, text, flags=re.IGNORECASE)
        return m.group()
    pass


def decorate_hash(pre_hash, hash_value, post_hash, no_space=False):

    if no_space:
        return pre_hash + hash_value + post_hash
    else:
        if pre_hash == "" and post_hash == "":
            return hash_value
        elif pre_hash == "" and post_hash != "":
            return hash_value + ' ' + post_hash
        elif pre_hash != "" and post_hash == "":
            return pre_hash + ' ' + hash_value
        else:
            return pre_hash + ' ' + hash_value + ' ' + post_hash
        


def modify_hash(hash_value, args):
    """
    Generates a new hash from an existing hash.

    :param hash_value: Original hash value to be modified
    :param args: User arguments from arg parse
    :return: Newly generated hash value
    """

    # Advice: refactor to use a strategy pattern

    if args.c == 'lower':
        new_hash = hash_value.lower()
    elif args.c == 'upper':
        new_hash = hash_value.upper()
    else:
        new_hash = hash_value

    # if hasattr(args, "ns"):
    # # if args.ns:
    #     new_hash = args.b + new_hash + args.a
    # else:
    #     before_text = replace_file_parts(args.b, filepath, args)
    #     after_text = replace_file_parts(args.a, filepath, args)
    #     if before_text != '':
    #         before_text = before_text + ' '
    #     if after_text != '':
    #         after_text = ' ' + after_text
    #     new_hash = before_text + new_hash + after_text
        

    return new_hash


def write_hash(new_hash, filename):
    """
    Writes a hash value to a given file

    :param new_hash: The hash value
    :param filename: File path to the file to write to
    :return:
    """
    with open(filename, "w") as f:
        f.write(new_hash)


def get_hash_length(hash_name):
    """
    Provides the length of a given Hash type

    :param hash_name: String. name of hash file
    :return:
    """
    return hash_lengths[hash_name]


def create_decoration(input_string, filepath, args):
    """
    Replaces special strings with particular strings
    
    :param input_string: any string
    :param filepath: the path of the checksum sidecar file being processed
    :param args: User arguments from arg parse
    :return:
    """
    
    filepath = filepath.replace(args.ie, "")

    output_string = input_string.replace("{filename}", os.path.basename(filepath))
    output_string = output_string.replace("{fullpath}", filepath)

    if args.outputPath:
        manifest_dir_path = os.path.dirname(args.outputPath)
        manifest_dir_path = os.path.abspath(manifest_dir_path)
        relative_path = filepath.replace(manifest_dir_path, "")
        output_string = output_string.replace("{relativepath}", relative_path)
    else:
        output_string = output_string.replace("{relativepath}", os.path.basename(filepath))
    return output_string


#     DON'T USE THIS
def add_hash_to_manitest(manifest_path, hash_path, hash):
    """
    :param manifest_path: path to the manifest file
    :param hash_path: path to the hash file
    :param hash: the hash to be added to the manifest
    """

    warnings.warn("The 'add_hash_to_manitest' class was Deprecated. "
                  "Use Checksumthing.manifest_formats.manifest instead.", DeprecationWarning)

    with open(manifest_path, "w+") as f:
        f.write(hash + "\n")
  