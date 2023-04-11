class Bugtongs:
    unclassifieds = [
        ["Kaaway ni bantay",                "May siyam na buhay",                   "Kuring"     ],
        ["Bangkang naglayag na",            "Pilit nagsasagwan pabalik",            "Kasama"     ],
        ["Binili ko nang \'di kagustuhan",  "Ginamit ko nang \'di ko nalalaman",    "Kabaong"    ],
        ["Mga bangkang naglalayag",	        "Magkakasamang nawawala",               "Galangmundo"],
        ["Kabaong na walang takip",	        "Sasakyang nasa tubig",	                "Bangka"     ],
        ["Aking palangga",                  "Ginising sa palanggana",               "Rara"       ],
        ["Kahel at puting balahibo",        "May munting mga paa",	                "Littlefoot" ],
        ["Kaibigang dikit nang dikit",      "Nagpapakulo ng tubig",                 "Buyag"      ],
        ["Hikaw ng babayi",                 "Puno ng pag-uugnay",                   "Balete"     ],
        ["Isang prinsesa",                  "Punong-puno ng mata",                  "Pina"       ],
        ["Pusang gala nang gala",           "Sa tubig ay nagtatampisaw",            "Daloy"      ],
    ]
    
    classifieds = []
    
    def __init__(self):
        Bugtongs.load_all()
        
    @classmethod
    def load_all(cls):
        for bugtong in cls.unclassifieds:
            first,second,answer = bugtong[0],bugtong[1],bugtong[2]
            Bugtongs.classifieds.append(Bugtong(first, second, answer))


class Bugtong:
    def __init__(self, first, second, answer, is_real=True, is_on_floor=False):
        self.first,self.second,self.answer = first,second,answer
        self.is_real,self.is_on_floor = is_real,is_on_floor
     
   
class Card:
    def __init__(self, text, face, action, is_outside):
        self.text,self.face,self.action,self.is_outside = text,face,action,is_outside
     
     
    def draw(self, cards):
        Bugtong.seconds
        card = choice(cards)
        cards.remove(player_card)
        
        return card
     
    
def main():
    Bugtongs()
    print(Bugtongs.classifieds[4].first)



main()
