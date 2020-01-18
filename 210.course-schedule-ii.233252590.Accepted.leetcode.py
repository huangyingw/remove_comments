class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visited = [False for _ in range(numCourses)]
        stack = [False for _ in range(numCourses)]
        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)
        result = []
        for course in range(numCourses):
        	if visited[course] == False:
        		if self.dfs(graph, visited, stack, course, result):
        			return []
        return result

    def dfs(self, graph, visited, stack, course, result):
    	visited[course] = True
     stack[course] = True
     for neigh in graph[course]:
    		if visited[neigh] == False:
    			if self.dfs(graph, visited, stack, neigh, result):
    				return True
      elif stack[neigh]:
    			return True
     stack[course] = False
     result.append(course)
     return False
