'''
Given head which is a reference node to a singly-linked list. 
The value of each node in the linked list is either 0 or 1. The linked list 
holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

Example 1:

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
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
    def getDecimalValue(self, head):
        
        head = create_linked_list(head)
        
        ans = 0
        currentNode = head
        
        aux = []
        
        while currentNode:
            ans = ans * 2 + currentNode.val
            currentNode = currentNode.next
        
        return ans
        
    
solution = Solution()
head = [1,0,1]
print(solution.getDecimalValue(head))