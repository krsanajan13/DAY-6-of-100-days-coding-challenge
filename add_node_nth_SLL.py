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

    def addNewNode_nth(self,val,n):
        new_n=Node(val)

        if n<=0:
            print("N should be greater than 0")
            return
        if n==1:
            new_n.next = self.root
            self.root=new_n
            return

        temp=self.root
        count=1

        while temp!=None and count<n-1:
            temp=temp.next
            count+=1

        if temp==None:
            print("Position is out of bound")
            return
        new_n.next=temp.next
        temp.next=new_n

    def display(self):
        temp=self.root
        while temp!=None:
            print(temp.val,end=' ')
            temp=temp.next




s=SingleLinkedList()
s.addNewNode(10)
s.addNewNode(20)
s.addNewNode(30)
s.addNewNode(40)
s.addNewNode_nth(50,1)
s.display()

