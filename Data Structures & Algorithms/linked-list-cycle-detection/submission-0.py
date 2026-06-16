
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        currentNode = head
        nodeSet = set()
        while currentNode:
            if self.checkNodeCyle(currentNode, nodeSet):
                return True
            nodeSet.add(currentNode)
            currentNode = currentNode.next

        return False 
    
    def printNodeData(self, node: Optional[ListNode]) -> None:
        print(f"Node Val: {node.val}")
        if node.next:
            print(f"Next Node Val: {node.next.val}")
        print("\n")
    
    def checkNodeCyle(self, node, nodeSet) -> bool:
        if node in nodeSet:
            return True
        return False