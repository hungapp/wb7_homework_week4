# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = joiner = ListNode()
        dummy.next = l = r = head
        
        while True:
            count = 0
            while r and count < k:
                r = r.next
                count += 1
            if count == k: #reverse k list
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur
                joiner.next = pre
                joiner = l
                l = r
            else:
                return dummy.next
                
