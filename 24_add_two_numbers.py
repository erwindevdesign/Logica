class Solution:
    def addTwoNumbers(self, l1: List[int], l2: List[int]) -> List[int]
        carry = 0
        head = tail = ListNode(0)
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sum = v1 + v2 + carry
            
            carry = sum // 10
            digit = sum % 10
            
            tail.next = ListNode(digit)
            tail = tail.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return head.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)