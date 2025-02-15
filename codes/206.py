'''
Given the head of a singly linked list, reverse the list, and return the 
reversed list.


Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
'''

def create_linked_list(values):
    head = ListNode(values[0])
    currentNode = head
    for val in values[1:]:
        currentNode.next = ListNode(val)
        currentNode = currentNode.next
    return head

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        head = create_linked_list(head)
        
        previousNode = None
        currentNode = head
        
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode()            

        return previousNode                       
        

solution = Solution()
head = [1,2,3,4,5]
print(solution.reverseList(head))        