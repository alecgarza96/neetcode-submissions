# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode()
        tempMerge = mergedList

        while list1 and list2:
            print(tempMerge.val)
            if list1.val > list2.val:
                tempMerge.next = list2
                tempMerge = tempMerge.next
                list2 = list2.next
            elif list1.val <= list1.val:
                tempMerge.next = list1
                tempMerge = tempMerge.next
                list1 = list1.next
        
        if list1:
            tempMerge.next = list1
        
        if list2:
            tempMerge.next = list2
        
        return mergedList.next
        