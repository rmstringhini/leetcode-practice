'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
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
        
# class Solution(object): # best solution
#     def middleNode(self, head):
#         head = create_linked_list(head)
    
#         slow = head
#         fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow        

class Solution(object): # mine solution
    def middleNode(self, head):
        head = create_linked_list(head)
        
        count = 0
        currentNode = head
        while currentNode:
            count += 1
            currentNode = currentNode.next
        
        if count == 1: return head
        
        aux_count = count
        middle = int(aux_count/2)
        
        count = 0
        currentNode = head
        while currentNode:
            count += 1
            currentNode = currentNode.next
            if count == middle:
                return currentNode
        return None
            
        

solution = Solution()
head = [1,2,3,4,5,6]
print(solution.middleNode(head))