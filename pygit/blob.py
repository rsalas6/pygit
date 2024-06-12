import os
import hashlib
from pygit.config import OBJECTS_DIR

def write_blob(content):
    """
    Write a blob object to the objects directory.
    """
    header = f'blob {len(content)}\0'
    store = (header + content).encode()
    sha = hashlib.sha1(store).hexdigest()
    path = f'{OBJECTS_DIR}/{sha[:2]}/{sha[2:]}'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'wb') as f:
        f.write(store)
    return sha

def read_blob(sha):
    """
    Read a blob object from the objects directory.
    """
    path = f'{OBJECTS_DIR}/{sha[:2]}/{sha[2:]}'
    if not os.path.exists(path):
        raise FileNotFoundError(f'Blob {sha} does not exist.')
    with open(path, 'rb') as f:
        data = f.read()
    return data

def get_blob_sha(content):
    """
    Get the SHA-1 hash of the blob content.
    """
    header = f'blob {len(content)}\0'
    store = (header + content).encode()
    return hashlib.sha1(store).hexdigest()
