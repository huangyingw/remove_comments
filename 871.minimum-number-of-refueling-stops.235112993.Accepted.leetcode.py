import heapq
class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        stops = 0
        fuel = startFuel
        past_fuels = []
        stations.append([target, 0])
        for distance, station_fuel in stations:
            while fuel < distance:
                if not past_fuels:
                    return -1
                fuel -= heapq.heappop(past_fuels)
                stops += 1
            heapq.heappush(past_fuels, -station_fuel)
        return stops
