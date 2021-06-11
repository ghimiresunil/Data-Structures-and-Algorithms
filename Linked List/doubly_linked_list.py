class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            itr = itr.next
            count += 1
        return count

    
    def print_forward(self):
        if self.head is None:
            print('Linked List is Empty')
            return
        itr = self.head
        linked_list_string = ''

        while itr:
            linked_list_string += str(itr.data) + ' --> '
            itr = itr.next
        print(linked_list_string)

    def print_backward(self):
        if self.head is None:
            print('Linked List is empty')
            return
if __name__ == '__main__':
    ll = LinkedList() 
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(51)
    ll.insert_at_beginning(25)
    ll.print_forward()   