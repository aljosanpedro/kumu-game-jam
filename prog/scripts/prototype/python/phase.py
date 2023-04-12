from random      import seed
from time        import sleep

from inputimeout import inputimeout

from control     import Control
from bugtong     import Bugtong
from card        import Card


class Phase:
    # ATTRIBUTES
    MP_TIME = 15
    MP_PROMPT = f"""
[Don't press Enter] to keep memorizing.
[Press Enter] to skip phase.
Type [G] to see bugtongs guide.

Action: """
    
    PP_TIME = 10
    PP_PROMPT = f"""
Type [A] to swipe left      [Defend] 
Type [D] to swipe right     [Attack]
[Enter] to do nothing       [Stand]

Action: """
    
    
    # METHODS
    # Standards
    @staticmethod
    def done():
        print(f"---PHASE DONE---\n")
    
    @staticmethod
    def battle_start():
        Control.clear_screen()
        print("\n---BATTLE START!---\n")
        seed() # RNG set-up
        Bugtong.load_raws() # load real & fake bugtongs and their attributes
    
    @staticmethod
    def round_start():
        Control.clear_screen()
        print("\n---ROUND START!---\n")
    
    
    # Memory
    @staticmethod
    def memory_start():
        Control.clear_screen()
        print("\n---MEMORIZE PHASE---\n")
    
    @classmethod
    def memory_timer_input(cls):
        print(f"{cls.MP_TIME} seconds to memorize! [Counting down...]")
        
        try:
            mp_input = inputimeout(prompt=cls.MP_PROMPT, timeout=cls.MP_TIME)            
        except Exception:
            mp_input = "time"
          
        Control.clear_screen()
        Phase.memorization_start()
          
        mp_input = mp_input.strip().lower()
        
        action = None
        if mp_input == 'g':
            action = "guide"
        elif mp_input == '':
            action = "skipped"
        elif mp_input == 'time':
            action = mp_input
        else:
            action = "invalid"
            
        print(f"{action.title()}!\n")
       
    
    # Play
    @staticmethod
    def play_start():
        Control.clear_screen()
        print("\n---PLAY PHASE---\n")
    
    @staticmethod
    def play_read(bugtong):
        reading = bugtong.first.upper()
        
        print("The announcer reads:")
        
        for _ in range(3):
            sleep(1)
            print("...")
        sleep(1)
        
        print(f"\n{reading}\n")
    
    @classmethod
    def play_timer_input(cls):
        print(f"{Phase.PP_TIME} seconds to act! [Counting down...]")
        
        try:
            pp_input = inputimeout(prompt=cls.PP_PROMPT, timeout=cls.PP_TIME)            
        except Exception:
            pp_input = "\ntime\n"
            
        pp_input = pp_input.strip().lower()
        
        action = None
        
        if pp_input == 'd':
            action = "attacked"
        elif pp_input == 'a':
            action = "defended"
        elif pp_input == '':
            action = "stood"
        elif pp_input == "time":
            action = pp_input
        else:
            action = "invalid"
            
        
        return action
    
    @staticmethod
    def play_judge(bugtong, cards, action):
        Control.clear_screen()
        Phase.play_start()
        print(f"Player: {action.upper()}!\n")
        
        
        second = bugtong.second
        player = cards[0].text
        enemy = cards[1].text
        
        
        round = "lost"
        owner = ""
        
        if second == player:
            owner = "player"
            if action == "attacked":
                round = "won"
        elif second == enemy:
            owner = "enemy"
            if action == "defended":
                round = "won"
        else:
            owner = "neither"
            if action == "stood":
                round = "stale"
    
        
        Card.set_face_up(cards, True)
        print(f"    Bugtong: {bugtong.first} | {bugtong.second.upper()} | {bugtong.answer}")
        
        print(f"\nThe bugtong's 2nd half belonged to: {owner.upper()}")
        print(f"\nRound: {round.upper()}\n")
        
    
        return round
    