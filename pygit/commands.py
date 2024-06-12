import os
from pygit.config import PYGIT_DIR, OBJECTS_DIR, REFS_DIR, HEAD_FILE
from pygit.blob import write_blob

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

def add_command(args):
    """
    Add file contents to the repository.
    """
    try:
        if not os.path.exists(PYGIT_DIR):
            raise Exception(f"Repository not initialized. Please run 'pygit init' first.")
        
        filepath = args.filepath
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File {filepath} does not exist.")
        
        with open(filepath, 'r') as f:
            content = f.read()
        
        sha = write_blob(content)
        print(f'Added {filepath} to the repository with SHA: {sha}')
    except Exception as e:
        raise Exception(f"Error adding file: {e}")
    
def commit_command(args):
    """
    Record changes to the repository.
    """
    # Simplified commit implementation
    try:
        message = args.message
        # Logic to create a commit would go here
        print(f'Committed changes with message: {message}')
    except Exception as e:
        raise Exception(f"Error creating commit: {e}")