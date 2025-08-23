class singnode :  
    head = None
    tail = None
    def __init__(self,val=None):
        self.val = val
        self.next=None
        if singnode.head == None :
            singnode.head = self
            singnode.tail = self
        else :
            singnode.tail.next = self 
            singnode.tail = self

i=1
while i < 6:
    obj = singnode(i)
    i += 1


def traverse (head) :
    cur = head 
    elem = []
    while cur :
        elem.append(cur.val)
        cur = cur.next

    return elem , len(elem)

def search (head,t) :
    
    cur = head 
    while cur :
        if t == cur.val :
            return True
        cur = cur.next 
    
    return False

def merge (head1,head2)  :
    cur = head1 
    
    if not cur :
        return head2
    
    while cur.next :
        cur = cur.next

    else :
        cur.next = head2
    return head1

def deletion(head,target) :
    cur = head
    dum = singnode()
    dum.next = head
    rev = dum
    while cur :
        if cur.val == target  :
            prev.next = cur.next
            break
        prev=cur
        cur = cur.next
    return dum.next

print(traverse(singnode.head))