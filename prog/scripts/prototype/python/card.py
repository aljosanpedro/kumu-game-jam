from control    import Control


class Card:
    # Instances
    def __init__(self, text, is_face_up=False, is_outside=False):
        self.text = text
        self.is_face_up = is_face_up
        self.is_outside = is_outside
    
    
    # Methods
    @classmethod
    def load_cards(cls, bugtongs):
        player = cls(bugtongs[0].second)
        enemy = cls(bugtongs[1].second)
        
        print(f"New player and enemy cards are on the floor.\n")
        
        return [player, enemy]
    
    @staticmethod
    def set_face_up(cards, face):
        # Set face
        for card in cards:
            card.is_face_up = face
        
        # Print face 
        player, enemy = cards

        print_face = "DOWN"
        
        if player.is_face_up and enemy.is_face_up:
            print_face = "UP"
        print(f"[Cards face: {print_face}]\n")
        
        Control.enter_to_continue()
        
        # Print card texts if face UP
        if face:
            print(f"    Player Card: {player.text.upper()}\n")
            print(f"    Enemy Card: {enemy.text.upper()}\n")
            
        