class Solution:

    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        """
        [] -> I know how much of each coin I have
        50 -> values 
         nums = [1,2,3,3], quantity = [2]
         nums = {
                 1: 1
                 2: 1
                 3: 2
         }
         
                        []
        [1->1, 0],              [2->2, 0]
        [2->2, 0]               
        """
        c = Counter(nums)
        m = len(quantity)
		# we only need at most m different numbers, so we choose the ones which are most abundant
        left = sorted(c.values())[-m:]
        
		# If the customer with most quantity required can't be fulfilled, we don't need to go further and answer will be false
        quantity.sort(reverse=True)
        
        def func(left, quantity, customer):
            if customer == len(quantity):
                return True
            
            for i in range(len(left)):
                if left[i] >= quantity[customer]:
                    left[i] -= quantity[customer]
                    if func(left, quantity, customer+1):
                        return True
                    left[i] += quantity[customer]
            return False
        
        return func(left, quantity, 0)
