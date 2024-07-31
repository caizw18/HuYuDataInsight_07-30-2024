class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def quick_sort_list(head):
    if not head or not head.next:
        return head

    def partition(start, end):
        pivot, p = start.val, start.next
        small, large = ListNode(0), ListNode(0)
        small_head, large_head = small, large

        while p != end:
            if p.val < pivot:
                small.next = p
                small = small.next
            else:
                large.next = p
                large = large.next
            p = p.next

        small.next = start
        large.next = end
        start.next = large_head.next
        return small_head.next, start

    def quick_sort(start, end):
        if start != end:
            new_start, pivot = partition(start, end)
            if new_start != pivot:
                p = new_start
                while p.next != pivot:
                    p = p.next
                p.next = None
                new_start = quick_sort(new_start, pivot)
                p = new_start
                while p.next:
                    p = p.next
                p.next = pivot
            pivot.next = quick_sort(pivot.next, end)
        return start

    return quick_sort(head, None)


# Helper functions for testing
def list_to_linkedlist(lst):
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linkedlist_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst


# Example usage
lst = [4, 2, 1, 3]
head = list_to_linkedlist(lst)
sorted_head = quick_sort_list(head)
print(linkedlist_to_list(sorted_head))  # Output: [1, 2, 3, 4]