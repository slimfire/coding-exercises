class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_linked_list(head):
    curr = head
    while(curr):
        print curr.val
        curr = curr.next