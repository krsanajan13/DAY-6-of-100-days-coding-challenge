class Node:
    def __init__(self,val ):
        self.val=val
        self.next=None

class SingleLinkedList:
    def __init__(self):
        self.root=None

    def addNewNode(self,val):
        n=Node(val)
        if self.root==None:
            self.root=n
            return
        temp=self.root
        while temp.next!=None:
            temp=temp.next
        temp.next=n


    def display(self):
        temp=self.root
        while temp!=None:
            print(temp.val,end=' ')
            temp=temp.next

    def delete_nth_node(self,n):
        if n<=0:
            print("n should be greater than zero")
            return
        if n == 1:
            self.root = self.root.next
            return
        temp=self.root
        count=1

        while temp != None and count <n-1:
            temp = temp.next
            count += 1
        temp.next=temp.next.next




s=SingleLinkedList()
s.addNewNode(10)
s.addNewNode(20)
s.addNewNode(30)
s.addNewNode(40)
s.addNewNode(50)
s.delete_nth_node(2)
s.display()

