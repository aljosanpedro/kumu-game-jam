# IMPORTS
# Built-in
from time        import sleep

# Files
from control     import Control
from card        import Card

# Parent Class
from .phase      import Phase


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
        
        for _ in range(3):
            sleep(1)
            print("...")
        sleep(1)
        
        # Reading
        print(f"\n{reading}\n")
    
    @staticmethod
    def input_to_action(input):
        action = None
        
        if input == 'd'     : action = "attacked"
        elif input == 'a'   : action = "defended"
        elif input == ''    : action = "stood"
        elif input == "time": action = "time"
        else                : action = "invalid"
            
        return action
    
    @staticmethod
    def judge(bugtong, cards, action):
        # Clarify bugtong halves
        second = bugtong.second
        player, enemy = cards[0].text, cards[1].text
        
        # Result, correct half owner
        result = "lost" # default, since most conditions; saves logic
        owner = ""
        
        if second == player:
            owner = "player"
            if action == "attacked":
                result = "won"
        elif second == enemy:
            owner = "enemy"
            if action == "defended":
                result = "won"
        else:
            owner = "neither"
            if action == "stood":
                result = "stale"
    
        return [result, owner]
    
    @staticmethod
    def print_results(bugtong, result, owner):
        print(f"    Bugtong: {bugtong.first} | {bugtong.second.upper()} | {bugtong.answer}")

        print(f"\nThe bugtong's 2nd half belonged to: {owner.upper()}")
        print(f"\nResult: {result.upper()}\n")
    