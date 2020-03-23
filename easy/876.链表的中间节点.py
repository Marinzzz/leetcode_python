# 思路一 遍历链表一遍


# 思路二 双指针，一个指针走一下，一个指针走两下
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        one = head
        two = head
        if not one.next:
            return one
        while(1):
            one = one.next
            if two.next:
                two = two.next
            else:
                return one
            if two.next:
                two = two.next
            else:
                return one
            if not two.next:
                return one
