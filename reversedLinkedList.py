class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 2 pointer approach
        #a current and prev pointer 
        # we set the next pointer is going to point to previous current pointer points to the next pointer
        #at the end thge prev pointer is the head we need to return
        prev, curr = None, head
        #o(n)
        #meme is 0(1)
        #runs until curr becomes null
        while curr:
            #this saves the link before it gets rerouted to the prevoius pointer
            nxt = curr.next
            #reroutes the link to the previous link
            curr.next = prev
            #previous becomes the current after it is rerouted
            prev = curr
            #the current get reassigned to the next node over
            curr = nxt
            
        #this ends up being the head at the end of the loop because current will become null because at the end next will be a null value
        return prev
    
