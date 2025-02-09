# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        k-=1
        def reverse(head):
            if not head or not head.next: return head
            ptr,nex,prev = head,head.next,None
            while nex:
                ptr.next = prev
                prev = ptr
                ptr = nex
                nex = nex.next
            ptr.next = prev
            return ptr
        def recursion(head):
            if not head or not head.next: return head
            count = k
            bk = head
            while bk and count:
                bk = bk.next
                count-=1
            if bk:
                nex = bk.next
                bk.next = None
                temp = head
                head = reverse(head)
                temp.next = recursion(nex)
            return head
        return recursion(head)
         
        