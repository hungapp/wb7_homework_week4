from heapq import *

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        min_heap = []
        count = 0
        
        for root in lists:
            if root is None: 
                continue
            heappush(min_heap, (root.val, count, root))
            count += 1
        
        head, tail = None, None
        while min_heap:
            val, c, node = heappop(min_heap)
            if not head:
                head = tail = node
            else:
                tail.next = node
                tail = tail.next
            
            if node.next:
                node = node.next
                heappush(min_heap, (node.val, count, node))
                count += 1
        
        return head
