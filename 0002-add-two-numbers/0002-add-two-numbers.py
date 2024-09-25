# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def build_num(node, num, d):
            num += node.val * (10 ** d)
            if node.next:
                num = build_num(node.next, num, d+1)
            return num

        def build_list(node, num):
            node = ListNode(num.popleft(), node)
            if num:
                node = build_list(node, num)
            return node

        first_num = l1.val
        if l1.next:
            first_num = build_num(l1.next, first_num, 1)
        sec_num = l2.val
        if l2.next:
            sec_num = build_num(l2.next, sec_num, 1)

        res = first_num + sec_num
        res = collections.deque(str(res))
        return build_list(None, res)

