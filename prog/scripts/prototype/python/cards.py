from card import Card


class Cards:
    @staticmethod
    def load(bugtongs):
        player = Card(bugtongs[0].second)
        enemy = Card(bugtongs[1].second)
        
        print(f"---Cards on Floor---\n")
        print(f"Player: {player.text.upper()}\n")
        print(f"Enemy: {enemy.text.upper()}\n")
        
        return [player, enemy]
    
    
    @staticmethod
    def set_face_up(cards, face):
        for card in cards:
            card.is_face_up = face
        
        # printing
        player, enemy = cards
        print_face = "DOWN"
        if player.is_face_up and enemy.is_face_up:
            print_face = "UP"
        print(f"[Cards face: {print_face}]\n")
        


"""
    @classmethod 
    def draw(cls):
        # use Bugtong.is_on_floor later to filter out 1st half pool
        while True:
            bugtong = choice(Bugtongs.filtered)
            
            if (bugtong.is_real) and (not bugtong.is_on_floor):
                break
        
        bugtong.is_on_floor = True
            
        return bugtong
    """