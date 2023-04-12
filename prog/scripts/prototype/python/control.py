from os import system


class Control:
    @staticmethod
    def enter_to_continue():
        while True:
            continue_input = input(f"Press [Enter] to continue.")
            
            if continue_input == "":
                break
        print()
        
    @staticmethod
    def clear_screen():
        system("cls")
        