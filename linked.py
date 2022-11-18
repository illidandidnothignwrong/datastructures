class Node: # defining class node
    def __init__(self,data):
        self.data = data
        self.next= None
        self.prev =  None
        
class linkedlist:#defining and creating class linked list using class Node
    def __init__(self):
        self.head =None
    def append1(self,data):
        if self.head == None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node  =Node(data) 
            cur = self.head
            while cur.next != None:
                cur =  cur.next
            cur.next = new_node
            new_node.next  = None
            new_node.prev = cur
    def print_node(self):
        list1 = []
        cur = self.head
        while cur !=None:
            list1.append(cur.data)
            cur =cur.next
        print(list1)
listt = linkedlist()
listt.append1(5)
listt.append1(3)
listt.append1(4)
listt.print_node()
