# Imports
from os import system


# Class
class Control:
    # METHODS
    # Terminal
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
     
        
    # Phases
    @staticmethod
    def start(phase):
        Control.clear_screen()
        print(f"\n---{phase.upper()} START!---\n")
    
    @staticmethod
    def end():
        print(f"---PHASE END---\n")
    