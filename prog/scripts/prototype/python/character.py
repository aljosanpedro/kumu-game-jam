class Character:
    def __init__(self, name, health, anim):
        self.name = name
        self.health = health
        self.anim = anim
        
        Character.status(self)
    
    
    def status(self):
        print(f"{self.name} [Health: {self.health}] [Animation: {self.anim}]\n")
    
    
    def set_anim(self, anim):
        self.anim = anim
        
        Character.status(self)
        
    @staticmethod        
    def set_anim_both(characters, anim):
        player, enemy = characters

        player.set_anim(anim)
        enemy.set_anim(anim)
             
                
    def damage(self, damage):
        self.health -= damage
        
        Character.status(self)

    @staticmethod
    def apply_result(action, result, characters):
        player, enemy = characters