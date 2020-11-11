class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        odd_pointer = head

        even_pointer = head.next
        dummy_even_head = even_pointer

        while even_pointer and even_pointer.next:
            odd_pointer.next = even_pointer.next
            odd_pointer = even_pointer.next
            if odd_pointer: 
                even_pointer.next = odd_pointer.next
                even_pointer = odd_pointer.next

        odd_pointer.next = dummy_even_head
        
        return head
