class Cmd:
    def __init__(self):
        self.help_text = """
        Commands
        help: Display commands
        exit: Exit application
        """

    def start(self):
        print(self.help_text)
        user_input = ""
        while (user_input != "exit"):
            user_input = input("> ")

            if user_input == "help":
                print(self.help_text)
