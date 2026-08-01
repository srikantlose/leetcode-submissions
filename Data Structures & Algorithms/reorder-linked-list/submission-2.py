class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
         if not head or not head.next:
            return
        
         slow,fast=head,head
         while(fast and fast.next):
             fast=fast.next.next
             slow=slow.next
        
         prev,cur=None,slow.next
         slow.next=None
         while(cur):
             nextRef=cur.next
             cur.next=prev
             prev=cur
             cur=nextRef
         first,second=head,prev
         while second:
             temp1, temp2=first.next,second.next
             first.next=second
             second.next=temp1
             first=temp1
             second=temp2