# IMPORTS
# Installed
from inputimeout import inputimeout

# Files
from control     import Control

# CLASS
class Phase:
    # Attributes
    PROMPT = ""
    
    
    # Set-up
    def __init__(self, time):
        self.time = time
       
        
    # Shared Methods
    @classmethod
    def timer_input(cls, self) -> str:
        print(f"{self.time} seconds! [Counting down...]")
        
        try:
            input = inputimeout(prompt=cls.PROMPT, timeout=self.time)            
        except Exception:
            input = "time"
        
        input = input.strip().lower()
        
        return input

    @staticmethod
    def print_action(action, phase):
        Control.print_phase(phase)
        print(f"{action.title()}!\n")
        