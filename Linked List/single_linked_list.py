class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head

        while  itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            itr = itr.next
            count += 1
        return count

    def remove_at(Self, index):
        if index < 0 or index >= Self.get_length():
            raise Exception('Invalid Index')
            return
        
        count = 0
        itr = Self.head

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')

        count = 0
        itr =  self.head

        if index == 0:
            self.insert_at_beginning(data)
            return
        
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def show_result(self):
        if self.head is None:
            print('Linked List is empty')
            return
        
        itr = self.head
        linked_list_string = ''

        while itr:
            linked_list_string += str(itr.data) + ' --> '
            itr = itr.next
        print(linked_list_string)

    def insert_after_value(self, data_after, data):
        count = 0
        itr = self.head

        while itr != None:
            if itr.data == data_after:
                node = Node(data, itr.next)
                itr.next = node
                return True
            itr = itr.next
            count += 1
    
    def remove_by_value(self, data):
        count = 0
        itr = self.head

        if self.head is None:
            return
        
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
        
if __name__ == '__main__':
    ll = LinkedList() 
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(21)
    # ll.insert_at_end(51)
    ll.insert_values(['Apple', 'Banana', 'Orange', "Mango"])
    ll.remove_by_value('Banana')
    ll.insert_after_value("Mango","Pineapple")
    print('The length of linked list is ', ll.get_length())
    # ll.remove_at(2)
    # ll.insert_at(1, "lemon")
    ll.show_result()   