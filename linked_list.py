# 2095. Delete the Middle Node of a Linked List
class Solution(object):
    def deleteMiddle(self, head):
        if not head or not head.next: return None
        fast, slow = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head


# 328. Odd Even Linked List
# Method 1 - In-place pointer rewiring
class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next: return head
        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head

# Method 2 - dummy nodes
class Solution(object):
    def oddEvenList(self, head):
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)

        while head:
            odd.next = head
            odd = odd.next
            head = head.next

            if head:
                even.next = head
                even = even.next
                head = head.next

        odd.next = dummy2.next
        even.next = None
        return dummy1.next

# Better version of the Method 2
class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next: return head

        odd_dummy = odd = ListNode(0)
        even_dummy = even = ListNode(0)

        is_odd = True

        while head:
            if is_odd:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next

            head = head.next
            is_odd = not is_odd

        even.next = None
        odd.next = even_dummy.next
        return odd_dummy.next

# 206. Reverse Linked List
class Solution(object):
    def reverseList(self, head):
        cur = head
        prev = None

        while cur:
            temp_next = cur.next
            cur.next = prev
            prev = cur
            cur = temp_next

        return prev

# 2130. Maximum Twin Sum of a Linked List
class Olution(object):
    def pairSum(self, head):
        # Find meddle
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # mid == slow

        # reverse 2nd half
        prev = None
        cur = slow
        while cur:
            temp_next = cur.next
            cur.next = prev
            prev = cur
            cur = temp_next
        
        # Get the sum
        left = head
        right = prev
        res = 0
        while right: # only right can be used bz it contains only half the list
            res = max(res, left.val + right.val)
            left = left.next
            right = right.next
        return res








