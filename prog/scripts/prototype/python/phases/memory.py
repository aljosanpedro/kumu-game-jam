# IMPORTS
# Files
from control     import Control

# Parent Class
from .phase      import Phase


# CLASS
class MemoryPhase(Phase):
    # Attributes
    PROMPT = f"""
[Don't press Enter] to keep memorizing.
[Press Enter] to skip phase.
Type [G] to see bugtongs guide.

Action: """
    
    
    # Set-up
    def __init__(self, time):
        super().__init__(time)
    
    
    # Unique Methods
    @staticmethod
    def input_to_action(input) -> str:
        action = None
        
        if   input == 'g'   : action = "guide"
        elif input == ''    : action = "skipped"
        elif input == 'time': action = "time"
        else                : action = "invalid"
            
        return action
