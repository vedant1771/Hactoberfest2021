
class Node:
   # Single node
   def __init__(self,data):
      self.data = data
      self.next = None


class LinkedList:

   def __init__(self) -> None:
      self.head = None
  
  
   def first(self,data):
      #  insert at first 
      if self.head:
         new_node = Node(data)
         new_node.next = self.head
         self.head = new_node
         return data
      self.head = Node(data)
      return data

   def middle(self,data,pos):
      # insert at middle
      if pos < 1 or self.head==None:
         self.first(data)
         return data


      current_node = self.head
      current_pos = 0

      while current_node.next:
         
         current_pos += 1
         if pos == current_pos:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
            return data
         current_node=current_node.next
      return self.last(data)
      
   
   def last(self,data):
      #  insert at last
      if self.head:
         current_node = self.head
         while current_node.next:
            current_node = current_node.next
         current_node.next = Node(data)
         return data
      self.head = Node(data)
      return data


   def rfirst(self):
      #  remove first Node
      if self.head:
         data = self.head.data
         self.head = self.head.next
         return data
      raise Exception('List is Empty')


   def rmiddle(self,pos):
      # remove from middle
      if not self.head:
         raise Exception('List is Empty')
      if pos < 1:
         self.rfirst()
      current_node = self.head
      current_pos = 0
      while current_node.next:
         current_pos += 1
         if pos == current_pos:
            data = current_node.next.next.data
            current_node.next = current_node.next.next
            return data
         current_node = current_node.next
      self.rlast()


   def rlast(self):
      # remove from last
      if self.head == None:
         raise Exception('List is Empty')
      
      current_node = self.head
      while current_node.next:
         if current_node.next.next == None:
            data = current_node.next.data
            current_node.next = None
            return data
         current_node = current_node.next

   def reverse(self):
      # reverse linked list
      if not self.head:
         raise Exception('List is Empty')
      if not self.head.next:
         return
      current_node = self.head
      prev_node = None
      next_node = None

      while current_node:
         next_node = current_node.next
         current_node.next = prev_node
         prev_node = current_node
         current_node = next_node
      self.head = prev_node

   
   def __iter__(self):
      self._iter = self.head
      return self

   def __next__(self):
      if not self._iter:
         raise StopIteration
      data = self._iter
      self._iter = self._iter.next
      return data
      
   def view(self):
      # view linked list
      current_node = self.head
      while current_node:
         print(current_node.data,end=" -> ")
         current_node = current_node.next
      print(None)


_list = LinkedList()

_list.middle(1,0)
_list.last(2)
_list.last(3)
_list.last(5)
_list.first(0)
_list.middle(4,4)
_list.middle(6,6)
_list.view()
_list.rfirst()
_list.rlast()
_list.view()
_list.rmiddle(3)
_list.view()

for i in iter(_list):
   if (i.data==2):
      i.data=12
_list.view()

print('===== reverse list =======')
evens = LinkedList()
evens.last(2)
evens.last(4)
evens.last(6)
evens.last(8)
evens.last(10)
evens.view()
evens.reverse()
evens.view()
