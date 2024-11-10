import os

bash_history_path = os.path.expanduser("~/.bash_history")

keywords = input("Enter keywords to search for (separate multiple keywords with spaces): ").split()

try:
    with open(bash_history_path, 'r') as file:
        history = file.readlines()

    matching_commands = [command.strip() for command in history if all(keyword in command for keyword in keywords)]

    if matching_commands:
        print("\nCommands matching your keywords:")
        for command in matching_commands:
            print(command)
