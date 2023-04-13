# Imports
from control    import Control


# Class
class Card:
    # Instances
    def __init__(self, text, is_face_up=False):
        self.text = text
        self.is_face_up = is_face_up
    
    
    # Methods
    @classmethod
    def load_from_bugtongs(cls, bugtongs) -> list:
        player = cls(bugtongs[0].second)
        enemy = cls(bugtongs[1].second)
        
        print(f"New player and enemy cards are on the floor.\n")
        
        return [player, enemy]
    
    @staticmethod
    def set_face_up(cards, face):
        # Set
        for card in cards:
            card.is_face_up = face
        
        # Print Direction
        if face:
            print_face = "UP"
            
            # Print Content if face UP
            player, enemy = cards
            print(f"    Player Card: {player.text.upper()}\n")
            print(f"    Enemy Card: {enemy.text.upper()}\n")
        else:
            print_face = "DOWN"
            
        print(f"[Cards face: {print_face}]\n")
        