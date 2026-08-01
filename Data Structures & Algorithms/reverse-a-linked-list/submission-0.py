
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while(cur != None):
            nextRef = cur.next
            cur.next = prev
            prev = cur
            cur = nextRef
        return prev