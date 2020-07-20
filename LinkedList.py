class Element(object):

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):

    def __init__(self, head = None):
        self.head = head

    def append(self, new_element):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
    
    def delete_element(self, position):
        pass

    def search_element(self, value):
        pass

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if position <= 0:
            return None
        current = self.head
        for i in range(position-1):
            if current.next:
                current = current.next
            else:
                return None
        return current

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""

        if position <= 0:
            return False
        current = self.head
        for i in range(position-2):
            if current.next:
                current = current.next
            else:
                return False
        new_element.next = current.next
        current.next = new_element
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current.next:
                previous = current
                if current.next.value != value:
                    current = current.next
                else:
                    previous.next = current.next.next
                    current = current.next

    def print_list(self):
        head = self.head
        while head is not None:
            print (head.value)
            head = head.next
    
    def delete_duplicates(self):
        head = self.head
        if not head:
            return head
        root, prev = head.next, head
        while root is not None:
            if root.value == prev.value:
                prev.next = root.next
            else:
                prev = prev.next
            root = root.next
        return head

    def detect_cycle(self):
        head = self.head
        slow, fast = head, head
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
    
    def length_of_cycle(self):
        slow, fast = self.head, self.head
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                print ('cycle is present, now calculating length of the cycle')
                count = 1
                t = slow.next
                while t is not fast:
                    t= t.next
                    count += 1                
                return True, count

        return False, 0

    def length_of_cycle_using_space_and_less_time(self):
        d = {}
        head = self.head
        i = 0
        while head:
            if head in d:
                print ('cycle is present, now calculating length of the cycle')
                return True, i-d[head]+1
            else:
                i += 1
                d[head] = i
                head = head.next
        return False, 0

    # https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/
    # we can remove the loop using a set as well like we calculated the length of cycle above
    def detect_and_remove_loop(self):
        head = self.head
        slow, fast = head, head
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                print ('cycle exists, now removing the cycle')
                slow = self.head
                prev = fast
                while slow != fast:
                    prev = fast
                    slow = slow.next
                    fast = fast.next
                prev.next = None
            
                return True
                
        return False

    def sort_absolute_sorted_ll_regular_sorted(self):
        current = self.head.next
        prev = self.head
        while current:
            if current.value <= self.head.value:
                temp = current
                prev.next = temp.next
                current = prev
                temp.next = self.head
                self.head = temp
            
            prev = current
            current = current.next

    # https://www.geeksforgeeks.org/intersection-of-two-sorted-linked-lists/
    def intersection_of_sorted_ll(self, head1, head2):

        head3 = Element(None)
        res = head3
        while head1 and head2:
            if head1.value != head2.value:
                if head1.value <= head2.value:
                    head1 = head1.next
                else:
                    head2 = head2.next
            else:
                head3.next = head1
                head3 = head1
                head1 = head1.next
                head2 = head2.next
        head3.next = None
        return res.next



# e1 = Element(1)
# e2 = Element(2)
# e3 = Element(3)
# e4 = Element(4)
# e5 = Element(5)
# l2 = LinkedList(e1)
# l2.append(e2)
# l2.append(e3)
# l2.append(e4)
# l2.append(e5)
# l2.print_list()

# delete duplicates and then print
# print ('deleting')
# l2.delete_duplicates()
# l2.print_list()

# detect loop
# en = Element('40')
# l2.append(en)
# l2.print_list()
# en.next = e2
# print ('is cycle - {}'.format(l2.detect_cycle()))

# detect loop and count length
# en = Element('40')
# l2.append(en)
# l2.print_list()
# en.next = e4
# print ('is cycle - {}'.format(l2.length_of_cycle()))
# print ('is cycle more space- {}'.format(l2.length_of_cycle_using_space_and_less_time()))

# remove loop
# en = Element('40')
# l2.append(en)
# l2.print_list()
# en.next = e4
# print ('removing loop - {}'.format(l2.detect_and_remove_loop()))
# l2.print_list()

# sort into regular list from absolute ordered
# e1 = Element(10)
# e2 = Element(2)
# e3 = Element(-3)
# e4 = Element(-4)
# e5 = Element(-4)
# e6 = Element(20)
# ll = LinkedList(e1)
# ll.append(e2)
# ll.append(e3)
# ll.append(e4)
# ll.append(e5)
# ll.append(e6)

# ll.print_list()
# ll.sort_absolute_sorted_ll_regular_sorted()
# print ('AFter sorting')
# ll.print_list()

# intersection of 2 sorted linked list
e1 = Element(1)
e2 = Element(2)
e3 = Element(6)
e4 = Element(10)
e5 = Element(50)
e6 = Element(100)
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)
ll.append(e6)

e21 = Element(3)
e22 = Element(6)
e23 = Element(50)
ll2 = LinkedList(e21)
ll2.append(e22)
ll2.append(e23)

ll.print_list()
ll2.print_list()
new_head = ll.intersection_of_sorted_ll(e1, e21)
ll3 = LinkedList(new_head)
print ('AFter intersecting')
ll3.print_list()


'''
class ElementRightDown(object):

    def __init__(self, value):
        self.value = value
        self.right = None
        self.down = None

class LinkedListRightDown(object):

    def __init__(self, head = None):
        self.head = head

    def flatten(self):
        current = self.head
        contenders = []
        while current:
            if current.down:
                contenders.append(current.down)
            if current.right:
                contenders.append(current.right)
            
            if contenders:
                next_node = min(contenders, key = lambda x:x.value)
                contenders.remove(next_node)
                current.next = next_node
                current = next_node
            else:
                return self.head

        return self.head



e1 = ElementRightDown(5)
e2 = ElementRightDown(7)
e3 = ElementRightDown(8)
e4 = ElementRightDown(30)
e5 = ElementRightDown(10)
e6 = ElementRightDown(20)
e7 = ElementRightDown(19)
e8 = ElementRightDown(22)
e9 = ElementRightDown(50)
e10 = ElementRightDown(28)
e11 = ElementRightDown(35)
e12 = ElementRightDown(40)
e13 = ElementRightDown(45)
ll = LinkedListRightDown(e1)

e1.right = e5
e5.right = e7
e7.right = e10

e1.down = e2
e2.down = e3
e3.down = e4

e5.down = e6

e7.down = e8
e8.down = e9

e10.down = e11
e11.down = e12
e12.down = e13

current = ll.flatten()
print (current)



'''
