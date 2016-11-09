import re

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
    if args.ns:
        new_hash = args.b + new_hash + args.a
    else:
        new_hash = args.b + ' ' + new_hash + ' ' + args.a

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
    # if t == 'md5':
    #     hash_length = 32
    # elif t == 'sha1':
    #     hash_length = 40
    # elif t == 'sha256':
    #     hash_length = 64
    # else:
    #     raise Exception("invalid hash value")
    # return hash_length