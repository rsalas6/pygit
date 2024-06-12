import sys
from pygit.commands import execute_command
from pygit.utils import init

def execute_command(command, args):
    if command == "init":
        init()
    else:
        print(f"Unknown command: {command}")

def main():
    if len(sys.argv) < 2:
        print("Usage: pygit <command> [<args>]")
        return
    command = sys.argv[1]
    args = sys.argv[2:]
    execute_command(command, args)

if __name__ == "__main__":
    main()
