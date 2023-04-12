from random     import choice
from bugtong    import Bugtong


class Bugtongs:
    real_raws = [
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
    
    fake_raws = [
        ["Aking sinta",                     "Ikaw lang ang tahanan",                "Mundo"      ],
        ["Sa ilalim ng puting ilaw",        "Sa dilaw na buwan",                    "Buwan"      ],
    ]
    
    reals, fakes = [], []
    
    
    
    def __init__(self):
        for raws in [Bugtongs.real_raws, Bugtongs.fake_raws]:
            Bugtongs.load_raws(raws)
        print(f"Bugtong lists loaded (real & fake).\n")
        
    
    @classmethod
    def load_raws(cls, raws):
        is_real = True
        if raws == cls.fake_raws:
            is_real = False
        
        for bugtong in raws: 
            first, second, answer = bugtong
            
            if is_real:
                cls.reals.append(Bugtong(first, second, answer, is_real))
            else:
                cls.fakes.append(Bugtong(first, second, answer, is_real))                


    @classmethod
    def draw(cls):
        # preserve original reals, use a modifiable one
        # avoid duplicates between player & enemy by removing player's later
        reals = cls.reals 
        
        player = choice(reals)
        reals.remove(player)
        
        enemy = choice(reals)
        
        fake = choice(cls.fakes)
        
        print(f"---Bugtongs Drawn---\n")
        print(f"Player: {player.first} | {player.second} | {player.answer}\n")
        print(f"Enemy: {enemy.first} | {enemy.second} | {enemy.answer}\n")
        print(f"Fake: {fake.first} | {fake.second} | {fake.answer}\n")
        
        return [player, enemy, fake]
