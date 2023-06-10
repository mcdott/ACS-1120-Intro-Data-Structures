#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n) because we need to pass through all nodes once."""
        node = self.head  # O(1) time to assign new variable
        length = 0  # O(1) time to assign new variable
        while node:  # Up to n iterations
            length += 1  # O(1) time to increment length
            node = node.next  # O(1) time to assign new variable
        return length  # O(1) time to return value

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) because we have a reference to the tail node, 
        so we can append directly to it."""
        new_node = Node(item)  # O(1) time to create new node
        if self.is_empty():  # O(1) time to check if head is None
            self.head = new_node  # O(1) time to assign new head
            self.tail = new_node  # O(1) time to assign new tail
        else:
            self.tail.next = new_node  # O(1) time to assign next of tail
            self.tail = new_node  # O(1) time to assign new tail

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) because we have a reference to the head node, 
        so we can prepend directly to it."""
        new_node = Node(item)  # O(1) time to create new node
        if self.is_empty():  # O(1) time to check if head is None
            self.head = new_node  # O(1) time to assign new head
            self.tail = new_node  # O(1) time to assign new tail
        else:
            new_node.next = self.head  # O(1) time to assign next of new node
            self.head = new_node  # O(1) time to assign new head

    def find(self, matcher):
        """Return an item from this linked list if it is present.
        Best case running time: O(1) When the item is first in the list.
        Worst case running time: O(n) When the item is last in the list 
        or not in the list."""
        node = self.head  # O(1) time to assign new variable
        while node is not None:  # Up to n iterations
            if matcher(node.data):  # O(1) time to check equality
                return node.data  # O(1) time to return value
            node = node.next  # O(1) time to assign new variable
        return None  # O(1) time to return value

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) When the item is first in the list.
        Worst case running time: O(n) When the item is last in the list."""
        node = self.head  # O(1) time to assign new variable
        previous_node = None  # O(1) time to assign new variable
        while node is not None:  # Up to n iterations
            if item == node.data:  # O(1) time to check equality
                if node is not self.head and node is not self.tail:  # O(1) time to check equality
                    previous_node.next = node.next  # O(1) time to assign next of previous node
                elif node is self.head:  # O(1) time to check equality
                    self.head = node.next  # O(1) time to assign new head
                    if node is self.tail:  # O(1) time to check equality
                        self.tail = None  # O(1) time to assign new tail
                elif node is self.tail:  # O(1) time to check equality
                    self.tail = previous_node  # O(1) time to assign new tail
                    if previous_node:  # O(1) time to check if previous node is not None
                        previous_node.next = None  # O(1) time to assign next of previous node
                return  # O(1) time to return
            previous_node = node  # O(1) time to assign new variable
            node = node.next  # O(1) time to assign new variable
        raise ValueError('Item not found: {}'.format(item))  # O(1) time to raise exception
    
    def replace(self, old_item, new_item):
        """Replace the old item with the new item in the linked list, 
        or raise ValueError if the old item is not found. 
        Running time: O(n) because in the worst case we need to go through all nodes in the list."""
        node = self.head  # O(1) time to assign new variable
        while node is not None:  # Up to n iterations
            if old_item == node.data:  # O(1) time to check equality
                node.data = new_item  # O(1) time to replace data
                return  # O(1) time to return
            node = node.next  # O(1) time to assign new variable
        raise ValueError('Item not found: {}'.format(old_item))  # O(1) time to raise exception



def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))
    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
