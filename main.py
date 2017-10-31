def main():    
    help_text = """
            Commands
            help: Display commands
            exit: Exit application
    """

    print(help_text)
    user_input = ""
    while (user_input != "exit"):
        user_input = input("> ")

        if user_input == "help":
            print(help_text)


if __name__ == "__main__":
    main()

