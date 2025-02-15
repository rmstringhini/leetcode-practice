'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing 
together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''

def create_linked_list(values):
    head = ListNode()
    currentNode = head
    for val in values:
        currentNode.next = ListNode(val)
        currentNode = currentNode.next
    return head

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list1 = create_linked_list(list1)
        list2 = create_linked_list(list2)
        
        aux = ListNode()
        current = aux 
        
        while list1 and list2:
            if list1.val < list2.val:
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
        current.next = list1 if list1 else list2
        
        return current.next
                
                
                
                
        
        
solution = Solution()
list1 = [1,2,4]
list2 = [1,3,4]
print(solution.mergeTwoLists(list1, list2))
        