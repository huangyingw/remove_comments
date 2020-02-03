class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
                      current.next.val if current.next else 'null')
                          if current.next:
                          current=current.next
                          return dummy.next
