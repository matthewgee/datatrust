import hashlib

def get_resource_hash(resource_source_data):
    """
    Given a resource generate a hash for identification
    :param resource_source_data:
    :return:
    """

    return hashlib.sha256(resource).hexdigest()
