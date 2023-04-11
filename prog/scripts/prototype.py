from random import choice


class Bugtong:
    fulls = [
        ["Kaaway ni bantay",                "May siyam na buhay",                   "Kuring"],
        ["Bangkang naglayag na",            "Pilit nagsasagwan pabalik",            "Kasama"],
        ["Binili ko nang \'di kagustuhan",  "Ginamit ko nang \'di ko nalalaman",    "Kabaong"],
        ["Mga bangkang naglalayag",	        "Magkakasamang nawawala",               "Galangmundo"],
        ["Kabaong na walang takip",	        "Sasakyang nasa tubig",	                "Bangka"],
        ["Aking palangga",                  "Ginising sa palanggana",               "Rara"],
        ["Kahel at puting balahibo",        "May munting mga paa",	                "Littlefoot"],
        ["Kaibigang dikit nang dikit",      "Nagpapakulo ng tubig",                 "Buyag"],
        ["Hikaw ng babayi",                 "Puno ng pag-uugnay",                   "Balete"],
        ["Isang prinsesa",                  "Punong-puno ng mata",                  "Pina"],
        ["Pusang gala nang gala",           "Sa tubig ay nagtatampisaw",            "Daloy"],
    ]
    
    firsts, seconds, answers = [],[],[]


    def __init__(self):
        Bugtong.load_parts()


    @classmethod
    def load_parts(cls):    
        for full in Bugtong.fulls:
            cls.firsts.append(full[0])
            cls.seconds.append(full[1])
            cls.answers.append(full[2])
            
     
class Card:
    def __init__(self, text, face, action, is_outside):
        self.text, self.face, self.action, self.is_outside = text, face, action, is_outside
     
     
    def draw(self, cards):
        Bugtong.seconds
        card = choice(cards)
        cards.remove(player_card)
        
        return card


class Character:
    def __init__(self, who, health, animation):
        self.who = who
        self.health = health
        self.animation = animation
            
            
def main():
    Bugtong()

main()
