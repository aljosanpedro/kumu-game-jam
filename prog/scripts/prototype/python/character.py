class Character:
    def __init__(self, name, health, anim):
        self.name = name
        self.health = health
        self.anim = anim
    
    def status(self):
        print(f"{self.name} [Health: {self.health}] [Animation: {self.anim}]\n")
    
    def set_animation(self, anim):
        self.anim = anim
        
        Character.status(self)
                
    def damage(self, damage):
        self.health -= damage
        
        Character.status(self)    