from pis import Pis


def main():    
    help_text = """
            Commands
            add     Add new product to PIS
            help    Display commands
            exit    Exit application
    """
    pis = Pis()

    # Start user prompt
    print(help_text)
    user_input = ""
    while (user_input != "exit"):
        user_input = input("> ").strip()

        # Help text
        if user_input == "help":
            print(help_text)
        # Add product
        elif user_input == "add":
            title = input(" Title? ")
            description = input(" Description? ")
            pis.add(title, description)


if __name__ == "__main__":
    main()

