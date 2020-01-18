class Solution(object):
    def reorderList(self, head):
        if not head:
        	return None
        slow, fast = head, head.next
        while fast and fast.next:
        	slow = slow.next
         fast = fast.next.next
        head1, head2 = head, slow.next
        slow.next = None
        prev = None
        curr = head2
        while curr:
        	nex = curr.next
         curr.next = prev
         prev  = curr
         curr = nex
        head2 = prev
        while head2:
        	n1 = head1.next
         n2 = head2.next
         head1.next = head2
         head1.next.next = n1
         head2 = n2
         head1 = head1.next.next
        head = head1
