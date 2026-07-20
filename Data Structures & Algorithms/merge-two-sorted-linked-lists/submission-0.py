# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        mergedList = ListNode()
        tempMerge = mergedList

        while temp1 and temp2:
            print(tempMerge.val)
            if temp1.val > temp2.val:
                tempMerge.next = temp2
                tempMerge = tempMerge.next
                temp2 = temp2.next
            elif temp1.val <= temp2.val:
                tempMerge.next = temp1
                tempMerge = tempMerge.next
                temp1 = temp1.next
        
        if temp1:
            tempMerge.next = temp1
        
        if temp2:
            tempMerge.next = temp2
        
        return mergedList.next
        