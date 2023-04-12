from random     import choice

from control    import Control


class Bugtong:
    # Attributes
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
    
    reals, fakes = [], []
    
    
    # Instances
    def __init__(self, first, second, answer, is_real=True, is_on_floor=False):
        self.first = first
        self.second = second
        self.answer = answer
        self.is_real = is_real
        self.is_on_floor = is_on_floor
        
    
    # Methods
    @classmethod
    def load_raws(cls):
        for raws in [cls.real_raws, cls.fake_raws]:
            is_real = True
            if raws == cls.fake_raws:
                is_real = False
            
            for bugtong in raws: 
                first, second, answer = bugtong
                
                if is_real:
                    cls.reals.append(cls(first, second, answer, is_real))
                else:
                    cls.fakes.append(cls(first, second, answer, is_real))                
        Control.enter_to_continue()

    @classmethod
    def draw_bugtongs(cls):
        # preserve original reals, use a modifiable one
        # avoid duplicates between player & enemy by removing player's later
        reals = cls.reals 
        
        player = choice(reals)
        reals.remove(player)
        
        enemy = choice(reals)
        
        fake = choice(cls.fakes)
        
        return [player, enemy, fake]
