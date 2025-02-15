'''

Given the head of a sorted linked list, delete all duplicates such that each
element appears only once. Return the linked list sorted as well.

Input: head = [1,1,2]
Output: [1,2]

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # print(head)
        
        aux = list(set(head))
        # print(aux)
        
        return aux

solution = Solution()
head = [1,1,2,3,3]
solution.deleteDuplicates(head)      