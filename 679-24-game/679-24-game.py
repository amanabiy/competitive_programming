class Solution:
    def __init__(self):
        self.is24Found = False

    def judgePoint24(self, cards: List[int]) -> bool:
        """
        I have four cards -> which has 1 to 8
        self.is24Found = False
        [a, b, c, d]
        
                                      d
                            +       -      /      * 
                          (ans)   (ans)  (ans)   (ans)
                          +-*/
                          (ans)
                          +-*/
        return        [elements]
        Time: O((cards * operations) ^ 2)
        """
        operations = ['*', '+', '-', '/']
        
        def possibleResults(a, b):
            res = [ a + b, a - b, b - a, a * b]
            if a:
                res.append(b / a)
            if b:
                res.append(a / b)
            return res
        
        def backtracking(cards):
            if len(cards) == 1:
                return abs(cards[0] - 24.0) <= 0.1
            
            for i in range(len(cards)):
                for j in range(i + 1, len(cards)):
                    a, b = cards[i], cards[j]
                    notTaken = [cards[k] for k in range(len(cards)) if k != i and k != j]
                    
                    # add all the possiblities of a and b operation to notTaken and do same thing
                    allPossibilities = possibleResults(a, b)
                    
                    for eachPossibility in allPossibilities:    
                        notTaken.append(eachPossibility)
                        
                        res = backtracking(notTaken)
                        
                        if res:
                            return True
                        
                        notTaken.pop()
    
            return False
        
                    
        
        return backtracking(cards)
