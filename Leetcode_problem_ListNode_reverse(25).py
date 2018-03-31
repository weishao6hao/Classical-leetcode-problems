#Leetcode problem(25): Reverse Nodes in k-Group
class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy=jump=ListNode(0)
        dummy.next=l=r=head
        
        while 1:
            count=0
            while r and count<k:
                count=count+1
                r=r.next
            if count==k:
                cur=l
                pre=r
                for _ in range(k):
                    cur.next,cur,pre=pre,cur.next,cur
                jump.next,jump,l=pre,l,r
            else:
                return dummy.next