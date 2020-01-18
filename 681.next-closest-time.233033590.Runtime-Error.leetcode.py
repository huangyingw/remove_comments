class Solution(object):
    def nextClosestTime(self, time):
    	current_time = 60 * int(time[:2]) + int(time[3:])
     allowed = {int(x) for x in time if x != ':'}
     result = 24*60
     ans = current_time
     for h1, h2, m1, m2 in itertools.product(allowed, repeat=4):
    		hours, minutes = 10*h1+h2, 10*m1+m2
      if hours < 24 and minutes < 60:
    			elapsed = 60*hours + minutes
       diff = (current_time - elapsed)%(24*60)
       if 0 < diff < result:
    				result = diff
        ans = elapsed
     return "{:02d}:{:02d}".format(divmod(ans, 60))
