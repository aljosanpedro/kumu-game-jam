class Result:
    @staticmethod
    def judge(bugtong, cards, action) -> list:
        # Clarify bugtong halves
        second = bugtong.second
        player, enemy = cards[0].text, cards[1].text
        
        # Result, correct half owner
        result = "lost" # default, since most conditions; saves logic
        owner = ""
        
        if second == player:
            owner = "player"
            if action == "attacked":
                result = "won"
        elif second == enemy:
            owner = "enemy"
            if action == "defended":
                result = "won"
        else:
            owner = "neither"
            if action == "stood":
                result = "stale"
    
        return [result, owner]
    
    @staticmethod
    def print_results(bugtong, result, owner):
        print(f"    Bugtong: {bugtong.first} | {bugtong.second.upper()} | {bugtong.answer}")

        print(f"\nThe bugtong's 2nd half belonged to: {owner.upper()}")
        print(f"\nResult: {result.upper()}\n")
    