# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3=ListNode(0)
        h=l3
        flag=0
        pre = ListNode(0)
        while (l1!=None and l2!= None):
            flag = (l3.val + l1.val + l2.val)//10
            l3.val = (l3.val + l1.val + l2.val)%10
            temp = ListNode(0)
            pre = l3
            l3.next = temp
            l3 = temp
            if(l1.next == None and flag!= 0):
                l1.next = ListNode(flag)
                flag = 0
            elif(l2.next == None and flag != 0):
                l2.next = ListNode(flag)
                flag = 0
            l1 = l1.next
            l2 = l2.next
            l3.val = flag
            flag = 0
            
        
        if (l1 != None):
            l3.val = l1.val + l3.val
            l3.next = l1.next
        elif(l2 != None):
            l3.val = l2.val + l3.val
            l3.next = l2.next
        else:
            pre.next = None
        
        return h

        
obj=Solution();
l1=ListNode(2)
l1.next=ListNode(4)
l1.next.next=ListNode(3)
l2=ListNode(5)
l2.next=ListNode(6)
l2.next.next=ListNode(4)
res = obj.addTwoNumbers(l1,l2)


