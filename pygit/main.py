import argparse
from pygit.commands import (
    init_command,
    add_command,
    commit_command
)
from pygit.exceptions import PygitException

def main():
    parser = argparse.ArgumentParser(description="A simplified version of Git implemented in Python.")
    subparsers = parser.add_subparsers(title="commands", dest="command")
    
    # Define 'init' command
    parser_init = subparsers.add_parser('init', help="Initialize a new, empty repository.")
    parser_init.set_defaults(func=init_command)

    # Define 'add' command
    parser_add = subparsers.add_parser('add', help="Add file contents to the repository.")
    parser_add.add_argument('filepath', help="The path of the file to add.")
    parser_add.set_defaults(func=add_command)
    
    # Define 'commit' command
    parser_commit = subparsers.add_parser('commit', help="Record changes to the repository.")
    parser_commit.add_argument('message', help="The commit message.")
    parser_commit.set_defaults(func=commit_command)
    
    # Parse arguments
    args = parser.parse_args()
    
    # Execute the appropriate command
    if args.command is None:
        parser.print_help()
    else:
        try:
            args.func(args)
        except PygitException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
