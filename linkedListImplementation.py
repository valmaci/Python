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
        
# Append: Inserts Node at end of List
def Append(L, n):
    node = Node(n)
    if IsEmpty(L):
        L.head = node
        L.tail = L.head
    else:
        L.tail.next = node
        L.tail = L.tail.next
    return

# Prepend: Inserts Node at start of List
def Prepend(L, n):
    node = Node(n)
    if IsEmpty(L):
        L.head = node
        L.tail = L.head
    else:
        temp = L.head
        L.head = node
        L.head.next = temp
    return

# InsertAfter: Inserts m data after n data if it exists
def InsertAfter(L, n, m):
    if Search(L, n) != None and IsEmpty(L) != True:
        node = Node(m)
        if L.tail.data == n:
            Append(L, m)
            return
        else:
            iter = L.head
            while iter.data != n:
                iter = iter.next
            temp = iter.next
            iter.next = node
            node.next = temp
    return

# InsertAfterNode: Inserts m data after a particular Node, if it exists
def InsertAfterNode(L, node, m):
    if node != None and IsEmpty(L) != True:
        newNode = Node(m)
        if node == L.tail:
            Append(L, m)
            return
        else:
            iter = L.head
            while iter != node:
                iter = iter.next
            temp = iter.next
            iter.next = newNode
            newNode.next = temp
    return

# Remove: Removes the first Node containing n data
def Remove(L, n):
    if IsEmpty(L) != True or Search(L, n) != None:
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

# RemoveNode: Removes a Node
def RemoveNode(L, node):
    if IsEmpty(L) != True:
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

# Search: Data is returned if found, else None is returned
def Search(L, data):
    if IsEmpty(L):
        return None
    iter = L.head
    while iter != None:
        if iter.data == data:
            return data
        iter = iter.next
    return None

# Print: Prints List Nodes in order
def Print(L):
    if IsEmpty(L) != True:
        iter = L.head
        while iter != None:
            print(iter.data, end=' ')
            iter = iter.next
        print()
    return

# PrintReverse: Prints List in reverse order
def PrintReverse(L):
    if IsEmpty(L) != True:
        iter = L.head
        PrintReversal(L, iter)
        print()
    return

# PrintReversal: Recursive function that assists the Print Reverse function
def PrintReversal(L, iter):
    if iter == L.tail:
        print(iter.data, end=' ')
    else:
        PrintReversal(L, iter.next)
        print(iter.data, end=' ')
    return

# Sort: Sorts the list Nodes in ascending order
def Sort(L):
    if GetLength(L) >= 2:
        preIter = L.head
        iter = L.head.next
        while iter != None:
            position = InsertPosition(L, iter.data)
            
            if position == preIter:
                preIter = iter
            else:
                RemoveNode(L, iter)
                if position == None:
                    Prepend(L, iter.data)
                else:
                    InsertAfterNode(L, position, iter.data)
            iter = iter.next
    return

# InsertPosition: Finds position to insert for sort function
def InsertPosition(L, data):
    iter1 = None
    iter2 = L.head
    while iter2 != None and data > iter2.data:
        iter1 = iter2
        iter2 = iter2.next
    return iter1

# IsEmpty: Returns true if there are no Nodes in the List
def IsEmpty(L):
    return L.head == None and L.tail == None

# GetLength: Returns the number of nodes in the List
def GetLength(L):
    if IsEmpty(L):
        return 0
    iter = L.head
    count = 0
    while iter != None:
        iter = iter.next
        count += 1
    return count

# Copy: Builds and returns a copy of the List
def Copy(L):
    copy = List()
    if L.head != None:
        iter = L.head
        while iter != None:
            Append(copy, iter.data)
            iter = iter.next
    return copy
    
# ItemAt: Returns the data item at position i in List
def ItemAt(L, i):
    if IsEmpty(L) != True and i < GetLength(L):
        iter = L.head
        for j in range(i):
            iter = iter.next
            j += 1
        return iter.data
    return
    
def NodeAt(L, i):
    if IsEmpty(L) != True and i < GetLength(L):
        iter = L.head
        for j in range(i):
            iter = iter.next
            j += 1
        return iter
    return None

# Pop: Removes the item at position i in List. If i is not specified, it removes the first item in theList
def Pop(L, i=0):
    node = NodeAt(L, i)
    if IsEmpty != True and node != None:
        RemoveNode(L, node)
    return
    
# Count: Returns the number of items x appears in the List
def Count(L, x):
    if IsEmpty(L) != True:
        count = 0
        iter = L.head
        while iter != None:
            if iter.data == x:
                count += 1
            iter = iter.next
        return count
    return
    
# Index: Returns the index of the first item whose value is equal to x in the List
def Index(L, x):
    if IsEmpty(L) != True:
        iter = L.head
        index = 0
        while iter != None:
            if iter.data == x:
                return index
            else:
                index += 1
                iter = iter.next
    return
    
# Clear: Removes all items from the List
def Clear(L):
    if IsEmpty(L) != True:
        L.head = None
        L.tail = None
    return
    
# Sublist: Builds and returns a sublist of the List from element start to elemend end, not inclusive
def Sublist(L, start=0, end=GetLength(L)):
    if start < 0 or end > GetLength(L):
        return
    sublist = List()
    if IsEmpty(L) != True:
        iter = NodeAt(L, start)
        while iter != None and start != end:
            Append(sublist, iter.data)
            iter = iter.next
            start += 1
    return sublist
    
# Reverse: Reverses the elements in the List
def Reverse(L):
    if IsEmpty(L) != True:
        iter = L.head
        reverse = List()
        Reversal(L, reverse, iter)
        Clear(L)
        iter2 = reverse.head
        while iter2 != None:
            Append(L, iter2.data)
            iter2 = iter2.next
    return
  
def Reversal(L, reverse, iter):
    Print(reverse)
    if iter == L.tail:
        Append(reverse, iter.data)
    else:
        Reversal(L, reverse, iter.next)
        Append(reverse, iter.data)
    return
        
