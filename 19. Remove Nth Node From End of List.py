
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

MyList4 = ListNode(43)
MyList3 = ListNode(4, MyList4)
MyList2 = ListNode(3, MyList3)
MyList1 = ListNode(13, MyList2)
MyList = ListNode(23, MyList1)

def removeNthFromEnd(head, n):
    pointer_list = []
    node = ListNode(head.val, head.next)

    while node.next != None:
        pointer_list.append(node.next)
        node = ListNode(node.next.val, node.next.next)

    len_pointer = len(pointer_list)
    if len_pointer > 0:
        pointer_list.append(None)
        remove = pointer_list[-n]
    else: return None

    node = ListNode(head.val, head.next)
    for i in range(len_pointer):
        node = ListNode(node.next.val, node.next.next)
        if node.next.next == remove:
            node.next = remove
            break

    return head if n != len_pointer else head.next

print(removeNthFromEnd(MyList,2))