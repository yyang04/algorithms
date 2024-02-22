class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse(li: ListNode):
    if not li:
        return None

    dump = ListNode(0)
    head = dump

    n = []
    while li:
        n.append(li.val)
        li = li.next

    for i in range(len(n)):
        head.next = ListNode(n[len(n) - i - 1])
        head = head.next

    return dump.next


def reverseList(li: ListNode):
    if not li.next and not li:
        return li

    pre, next = li, li.next
    pre.next = None

    while next.next:
        tmp = next.next
        next.next = pre
        pre = next
        next = tmp
    next.next = pre
    return next


def searchRotatedArray(li, target):
    left, right = 0, len(li) - 1

    while left <= right:

        mid = (left + right) // 2

        if li[mid] == target:
            return mid

        if li[mid] > li[left]:
            if li[mid] >= target >= li[left]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if li[mid] <= target <= li[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


print(searchRotatedArray([5, 6, 7, 9, 1, 2, 3], 7))


class Solution:

    def searchMatrix(self, matrix, target: int):
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m-1
        while l <= r:
            mid = (l + r) // 2

            if target >= matrix[mid][0]:
                l = mid
            else:
                r = mid

        row = matrix[l]

        l, r = 0, n-1
        while l <= r:
            mid = (l+r)//2
            if row[mid] == target:
                return True

            if target > row[mid]:
                l = mid + 1
            else:
                r - mid - 1
        return False




