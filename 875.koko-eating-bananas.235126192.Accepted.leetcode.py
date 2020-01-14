class Solution(object):
    def minEatingSpeed(self, piles, H):
        bananas, max_pile = sum(piles), max(piles)
        min_rate = (bananas + H - 1) // H
        max_rate = max_pile
        while min_rate < max_rate:
            rate = (min_rate + max_rate) // 2
            time = 0
            for pile in piles:
                time += (pile + rate - 1) // rate
                if time > H:
                    break
            if time > H:
                min_rate = rate + 1
            else:
                max_rate = rate
        return min_rate
