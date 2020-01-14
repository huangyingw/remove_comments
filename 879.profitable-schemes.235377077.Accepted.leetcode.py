class Solution(object):
    def profitableSchemes(self, G, P, group, profit):
        MOD = 10 ** 9 + 7
        schemes = [[0] * (G + 1) for _ in range(P + 1)]
        schemes[0][0] = 1
        for job_profit, job_gang in zip(profit, group):
            for p in range(P, -1, -1):
                for g in range(G, job_gang - 1, -1):
                    capped_profit = min(P, p + job_profit)
                    schemes[capped_profit][g] += schemes[p][g - job_gang]
        return sum(schemes[-1]) % MOD
