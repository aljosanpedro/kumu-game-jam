# Imports
from random     import seed, choice

from control    import Control


# Class
class Bugtong:
    # Attributes
    reals, fakes = [], []
    
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
        ["Baka sakaling",                   "Makita kitang muli",                   "Malaya"     ],
        ["Kamukha mo si Paraluman",         "Noong tayo ay bata pa",                "El Bimbo"   ],
        ["Umuwi ka na baby",                "Di na ako sanay na wala ka",           "Lemons"     ],
        ["Huwag na huwag mong sasabihin",   "Na hindi mo nadama ito",               "Kitchie"    ],
        ["Oo nga pala, hindi na pala tayo", "Hanggang dito lang ako",               "Moonstar"   ],
        ["Ilang ulit pa ba ang uulitin",    "O giliw ko",                           "Ligaya"     ],
        ["Iba na ang iyong ngiti",          "Iba na ang iyong tingin",              "Magasin"    ],
        ["Walang sagot sa tanong",          "Kung bakit ka mahalaga",               "Sila"       ],
    ]
    
    
    # Instances
    def __init__(self, first, second, answer):
        self.first = first
        self.second = second
        self.answer = answer
        
    
    # Methods
    @classmethod
    def load_raws(cls):
        
        def classify(empty):
            empty.append(cls(first, second, answer))
            
        for raws in [cls.real_raws, cls.fake_raws]:
            # Real/Fake Filter
            is_real = True
            
            if raws == cls.fake_raws:
                is_real = False
            
            # Instancing
            for bugtong in raws: 
                first, second, answer = bugtong
                
                classify(cls.reals) if is_real else classify(cls.fakes)
        
        Control.enter_to_continue()
        
    @classmethod
    def draw_for_round(cls):
        # Copy List
        reals = cls.reals 
        
        # Draw
        seed() # RNG
        
        player = choice(reals)
        # avoid duplicates between player & enemy by removing player's draw
        reals.remove(player)
        
        enemy = choice(reals)
        
        fake = choice(cls.fakes)
        
        return [player, enemy, fake]

    @staticmethod
    def draw_reading(bugtongs):
        return choice(bugtongs)
