# Course: CS2302 Data Structures
# Author: Valeria Macias
# Assignment: LinkedList Implementation
# Instructor: Olac Fuentes
# T.A.: Ismael Villanueva-Miranda
# Date of Last Modification: 6/25/19
# Purpose: A Linked List implementation

class Node(object):
    # Creates a new node
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class List(object):
    # Creates a new list
    def __init__(self):
        self.head = None
        self.tail = None
        
# Inserts Node at end of List
def append(L, n):
    node = Node(n)
    if is_empty(L):
        L.head = node
        L.tail = L.head
    else:
        L.tail.next = node
        L.tail = L.tail.next
    return

# Inserts Node at start of List
def prepend(L, n):
    node = Node(n)
    if is_empty(L):
        L.head = node
        L.tail = L.head
    else:
        temp = L.head
        L.head = node
        L.head.next = temp
    return

# Inserts m data after n data, if it exists
def insert_after(L, n, m):
    if Search(L, n) != None and IsEmpty(L) != True:
        node = Node(m)
        if L.tail.data == n:
            append(L, m)
            return
        else:
            iter = L.head
            while iter.data != n:
                iter = iter.next
            temp = iter.next
            iter.next = node
            node.next = temp
    return

# Inserts m data after a particular Node, if it exists
def insert_after_node(L, node, m):
    if node != None and is_empty(L) != True:
        new_node = Node(m)
        if node == L.tail:
            append(L, m)
            return
        else:
            iter = L.head
            while iter != node:
                iter = iter.next
            temp = iter.next
            iter.next = newNode
            new_node.next = temp
    return

# Removes the first Node containing n data
def remove(L, n):
    if is_empty(L) != True or search(L, n) != None:
        if L.head.data == n:
            L.head = L.head.next
            return
        if L.tail.data == n:
            iter = L.head
            while iter.next != L.tail:
                iter = iter.next
            L.tail = iter
            iter.next = None
            return
        else:
            iter = L.head
            while iter.next.data != n:
                iter = iter.next
            iter.next = iter.next.next
            return
    return

# Removes the specified node from list
def remove_node(L, node):
    if is_empty(L) != True:
        if node == L.head:
            L.head = L.head.next
            return
        iter = L.head
        if node == L.tail:
            while iter.next != L.tail:
                iter = iter.next
            L.tail = iter
            iter.next = None
            return
        else:
            while iter.next != node:
                iter = iter.next
            iter.next = iter.next.next
            return
    return

# Data is returned if found, else None is returned
def search(L, data):
    if is_empty(L):
        return None
    iter = L.head
    while iter != None:
        if iter.data == data:
            return data
        iter = iter.next
    return None

# Prints List Nodes in order
def print_list(L):
    if is_empty(L) != True:
        iter = L.head
        while iter != None:
            print(iter.data, end=' ')
            iter = iter.next
        print()
    return

# Prints List in reverse order
def print_reverse(L):
    if is_empty(L) != True:
        iter = L.head
        print_reversal(L, iter)
        print()
    return

# Recursive function that assists the print_reverse function
def print_reversal(L, iter):
    if iter == L.tail:
        print(iter.data, end=' ')
    else:
        print_reversal(L, iter.next)
        print(iter.data, end=' ')
    return

# Sorts the list Nodes in ascending order
def sort(L):
    if get_length(L) >= 2:
        pre_iter = L.head
        iter = L.head.next
        while iter != None:
            position = insert_position(L, iter.data)
            
            if position == pre_iter:
                pre_iter = iter
            else:
                remove_node(L, iter)
                if position == None:
                    prepend(L, iter.data)
                else:
                    insert_after_node(L, position, iter.data)
            iter = iter.next
    return

# Finds position to insert for sort function
def insert_position(L, data):
    iter1 = None
    iter2 = L.head
    while iter2 != None and data > iter2.data:
        iter1 = iter2
        iter2 = iter2.next
    return iter1

# Returns true if there are no Nodes in the List
def is_empty(L):
    return L.head == None and L.tail == None

# Returns the number of nodes in the List
def get_length(L):
    if is_empty(L):
        return 0
    iter = L.head
    count = 0
    while iter != None:
        iter = iter.next
        count += 1
    return count

# Builds and returns a copy of the List
def copy(L):
    copy = List()
    if L.head != None:
        iter = L.head
        while iter != None:
            append(copy, iter.data)
            iter = iter.next
    return copy
    
# Returns the data item at position i in List
def item_at(L, i):
    if is_empty(L) != True and i < get_length(L):
        iter = L.head
        for j in range(i):
            iter = iter.next
            j += 1
        return iter.data
    return
    
def node_at(L, i):
    if is_empty(L) != True and i < get_length(L):
        iter = L.head
        for j in range(i):
            iter = iter.next
            j += 1
        return iter
    return None

# Removes the item at position i in List. If i is not specified, it removes the first item in the List
def pop(L, i=0):
    node = node_at(L, i)
    if is_empty != True and node != None:
        remove_node(L, node)
    return
    
# Returns the number of items x appears in the List
def count(L, x):
    if is_empty(L) != True:
        count = 0
        iter = L.head
        while iter != None:
            if iter.data == x:
                count += 1
            iter = iter.next
        return count
    return
    
# Returns the index of the first item whose value is equal to x in the List
def index(L, x):
    if is_empty(L) != True:
        iter = L.head
        index = 0
        while iter != None:
            if iter.data == x:
                return index
            else:
                index += 1
                iter = iter.next
    return
    
# Removes all items from the List
def clear(L):
    if is_empty(L) != True:
        L.head = None
        L.tail = None
    return
    
# Builds and returns a sublist of the List from element start to elemend end, not inclusive
def sublist(L, start=0, end=get_length(L)):
    if start < 0 or end > get_length(L):
        return
    sublist = List()
    if is_empty(L) != True:
        iter = node_at(L, start)
        while iter != None and start != end:
            append(sublist, iter.data)
            iter = iter.next
            start += 1
    return sublist
    
# Reverses the elements in the List
def reverse(L):
    if is_empty(L) != True:
        iter = L.head
        reverse = List()
        reversal(L, reverse, iter)
        clear(L)
        iter2 = reverse.head
        while iter2 != None:
            append(L, iter2.data)
            iter2 = iter2.next
    return
  
def reversal(L, reverse, iter):
    print_list(reverse)
    if iter == L.tail:
        append(reverse, iter.data)
    else:
        reversal(L, reverse, iter.next)
        append(reverse, iter.data)
    return
        
