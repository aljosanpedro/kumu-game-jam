from random      import seed

from inputimeout import inputimeout

from control     import Control
from bugtongs    import Bugtongs


class Phases:
    @staticmethod
    def battle_start():
        Control.clear_screen()
        print("\n---BATTLE START!---\n")
        seed() # RNG set-up
        Bugtongs() # load real & fake bugtongs and their attributes
    
    @staticmethod
    def round_start():
        Control.clear_screen()
        print("\n---ROUND START!---\n")
    
    @staticmethod
    def memorization():
        Control.clear_screen()
        print("\n---MEMORIZE PHASE---\n")
    
    MP_TIME = 15
    
    mp_prompt = f"""
[Don't press Enter] to keep memorizing.
[Press Enter] to skip phase.
Type [G] to see bugtongs guide.

"""
    
    @classmethod
    def memorization_timer_input(cls):
        print(f"{Phases.MP_TIME} seconds to memorize! [Counting down...]")
        
        try:
            mp_input = inputimeout(prompt=cls.mp_prompt, timeout=cls.MP_TIME)            
        except Exception:
            mp_input = "Time's up!\n"
            print(mp_input)
            
        mp_input = mp_input.lower()
        
        if mp_input == 'g':
            print("\n---Guide---\n")
    
        print(f"---Phase Done---\n")
        
    @staticmethod
    def play():
        Control.clear_screen()
        print("\n---PLAY PHASE---\n")
    
    