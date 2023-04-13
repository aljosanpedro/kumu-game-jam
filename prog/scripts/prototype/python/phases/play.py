# IMPORTS
# Built-in
from time       import sleep

# Files
from character  import Character

# Parent Class
from .phase     import Phase


# CLASS
class PlayPhase(Phase):
    # Attributes
    PROMPT = f"""
Type [A] to swipe left      [Defend] 
Type [D] to swipe right     [Attack]
[Enter] to do nothing       [Stand]

Action: """
    
    
    # Set-up
    def __init__(self, time):
        super().__init__(time)
    
    
    # Unique Methods
    @staticmethod
    def read(bugtong):
        # Load Reading
        reading = bugtong.first.upper()
        
        # Announcer
        print("The announcer reads:")
        
        # Wait-Timer
        for _ in range(3):
            sleep(1)
            print("...")
        sleep(1)
        
        # Reading
        print(f"\n{reading}\n")
    
    @staticmethod
    def input_to_action(input) -> str:
        action = None
        
        if   input == 'd'   : action = "attacked"
        elif input == 'a'   : action = "defended"
        elif input == ''    : action = "stood"
        elif input == "time": action = "time"
        else                : action = "invalid"
                      
        return action
    