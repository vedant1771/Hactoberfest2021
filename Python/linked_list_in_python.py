class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begin(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node 

    def insert_at_end(self,data):
        n = self.head
        if n==None:
            self.head = Node(data)
            return
        while n.next!=None:
            n = n.next
        n.next = Node(data)

    def insert_after(self,data,x):
        n = self.head
        while n.data!=x:
            n = n.next
            if n==None:
                print(x,"is not in the list")
                return
                
        new_node = Node(data)
        new_node.next = n.next
        n.next = new_node

    def insert_before(self,data,x):
        n = self.head
        while n.next.data!=x:
            n = n.next
            if n.next==None:
                print(x,"is not in the list")
                return
        self.insert_after(data,n.data)


    def delete_begin(self):
        if self.head:
            self.head = self.head.next
        else:
            print("List is empty")

    def delete_end(self):
        if not self.head:
            print("List is Empty")
            return
        n = self.head
        while n.next.next!=None:
            n = n.next
        n.next = None
    def printlist(self):
        if self.head==None:
            print("List is Empty")
            return 
        temp = self.head
        while temp!=None:
            print(temp.data)
            temp = temp.next
    def sort_ones_zeroes(self,A):
        if A==None:
            return
        count1 = 0;
        count0 = 0;
        temp = A
        while temp:
            if temp.data==1:
                count1+=1
            if temp.data==0:
                count0+=1
            temp = temp.next
        head = A
        while count0!=0:
            if A:
                A.data=0
                A=A.next
            else:
                A = Node(0)
                A = A.next
            count0-=1
        while count1!=0:
            if A:
                A.data=1
                A=A.next
            else:
                A = Node(1)
                A = A.next
            count1-=1
        return head


    def partition(self, A, B):
        first, second = None, None
        smallhead = None
        highhead = None
        head = A
        while head is not None:
            if head.data < B:
                if first is None:
                    first = head
                    smallhead = first
                else:
                    first.next =  head
                    first = first.next
            else:
                if second is None:
                    second = head
                    highhead = second
                else:
                    second.next = head
                    second = second.next
            head = head.next
        second.next = None
        if smallhead is not None:
            first.next = highhead
            return smallhead
        else:
            return highhead


    def delete_node(self, head, val):
        node = Node(0)
        node.next=head
        head = node
        currentNode = head
        while currentNode:
            nextNode = currentNode.next
            while nextNode and nextNode.data==val: 
                currentNode.next = nextNode.next
                nextNode = nextNode.next
            currentNode = nextNode 
        return head.next


lkdlist = linkedlist()
lkdlist.insert_at_end(1)
lkdlist.insert_at_end(1)
lkdlist.insert_at_end(2)
lkdlist.insert_at_end(6)
lkdlist.insert_at_end(2)
lkdlist.insert_at_end(2)

# head = lkdlist.partition(lkdlist.head,3)
# lkdlist.printlist()

head = lkdlist.delete_node(lkdlist.head,6)
while head:
    print(head.data)
    head = head.next
# lkdlist.printlist()
          
