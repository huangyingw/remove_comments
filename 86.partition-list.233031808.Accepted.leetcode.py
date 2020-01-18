class Solution(object):
    def partition(self, head, x):
        if not head or not head.next:
        	return head
        left, right = ListNode(0), ListNode(0)
        leftPtr, rightPtr = left, right
        while head:
        	if head.val < x:
        		leftPtr.next = ListNode(head.val)
          leftPtr = leftPtr.next
         else:
        		rightPtr.next = ListNode(head.val)
          rightPtr = rightPtr.next
         head = head.next
        if not left.next:
        	return right.next
        elif not right.next:
        	return left.next
        else:
        	leftPtr.next = right.next
         return left.next
