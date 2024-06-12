import os
from pygit.config import PYGIT_DIR, OBJECTS_DIR, REFS_DIR, HEAD_FILE


def init_command(args):
    """
    Initialize a new, empty repository.
    """
    try:
        if not os.path.exists(PYGIT_DIR):
            os.makedirs(OBJECTS_DIR)
            os.makedirs(REFS_DIR)
            with open(HEAD_FILE, 'w') as f:
                f.write('ref: refs/heads/master\n')
            print(f'Initialized empty Git repository in {PYGIT_DIR}/')
        else:
            print('Repository already initialized')
    except Exception as e:
        raise Exception(f"Error initializing repository: {e}")
