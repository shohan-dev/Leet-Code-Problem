class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        all_nodes = []
        for lst in lists:
            while lst:
                all_nodes.append(lst)
                lst = lst.next

        all_nodes.sort(key=lambda x: x.val)

        dummy = ListNode()
        current = dummy

        for node in all_nodes:
            current.next = node
            current = current.next
        
        return dummy.next