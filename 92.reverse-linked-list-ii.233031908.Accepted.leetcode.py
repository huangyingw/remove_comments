class Solution(object):
    def reverseBetween(self, head, m, n):
        if m == n:
        	return head
        result = ListNode(0)
        result.next = head
        prev = result
        for index in range(m - 1):
        	prev = prev.next
        reverse = None
        curr = prev.next
        for i in range(n - m + 1):
        	temp = curr.next
         curr.next = reverse
         reverse = curr
         curr = temp
        prev.next.next = curr
        prev.next = reverse
        return result.next
