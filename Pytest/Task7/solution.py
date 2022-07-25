class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def tab2list(t):
    n = len(t)
    p = None
    for i in range(n-1,-1,-1):
        q = Node(None)
        q.val = t[i]
        q.next = p
        p = q
    return p

def list2tab(l):
    t = []
    while l!=None:
        t.append(l.val)
        l = l.next
    return t

def linked_list_sort(head_ref):
  
    sorted = None
  
    current = head_ref
    while (current != None):
      
        next = current.next
  
        sorted = sortedInsert(sorted, current)
  
        current = next
      
    head_ref = sorted
    return head_ref
  
def sortedInsert(head_ref, new_node):
  
    current = None
      
    if (head_ref == None or (head_ref).val >= new_node.val):
      
        new_node.next = head_ref
        head_ref = new_node
      
    else:
      
        current = head_ref
        while (current.next != None and current.next.val < new_node.val):
          
            current = current.next
          
        new_node.next = current.next
        current.next = new_node
          
    return head_ref
