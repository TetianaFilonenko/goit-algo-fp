class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

    # Функція реверсування списку
    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

    # Функція сортування злиттям
    def merge_sort(self):
        if not self.head or not self.head.next:
            return self.head

        def split(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            middle = slow.next
            slow.next = None
            return head, middle

        def merge(left, right):
            dummy = Node()
            tail = dummy
            while left and right:
                if left.data < right.data:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next
            tail.next = left or right
            return dummy.next

        def merge_sort_rec(head):
            if not head or not head.next:
                return head
            left, right = split(head)
            left = merge_sort_rec(left)
            right = merge_sort_rec(right)
            return merge(left, right)

        self.head = merge_sort_rec(self.head)

    # Функція об'єднання двох відсортованих списків
    def merge_sorted_lists(l1, l2):
        dummy = Node()
        tail = dummy
        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list


# Створення та наповнення списку
ll = LinkedList()
ll.insert_at_end(3)
ll.insert_at_end(1)
ll.insert_at_end(4)
ll.insert_at_end(2)

print("Original list:")
ll.print_list()

# Реверсування списку
ll.reverse()
print("Reversed list:")
ll.print_list()

# Сортування списку
ll.merge_sort()
print("Sorted list:")
ll.print_list()

# Об'єднання двох відсортованих списків
ll1 = LinkedList()
ll1.insert_at_end(1)
ll1.insert_at_end(3)
ll1.insert_at_end(5)

ll2 = LinkedList()
ll2.insert_at_end(2)
ll2.insert_at_end(4)
ll2.insert_at_end(6)

print("List 1:")
ll1.print_list()

print("List 2:")
ll2.print_list()

merged_list = LinkedList.merge_sorted_lists(ll1.head, ll2.head)
print("Merged sorted list:")
merged_list.print_list()
