from lib import print_linked_list, ListNode

def remove_node(head, num):
    if head == None:
        return head
    if head.val == num:
        new_head = head.next
        head.next = None
        return new_head
    
    prev = head
    curr = head.next

    while curr is not None:
        if curr.val == num:
            prev.next = curr.next
            curr.next = None
            return head
        else:
            prev = prev.next
            curr = curr.next
    
    return head


