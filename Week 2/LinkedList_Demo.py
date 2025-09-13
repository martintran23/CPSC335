# Single Linked List

class Node:
    def __init__(self, val, nxt=None):
        self.val = val # Store data payload
        self.next = nxt # Pointer to next node (or None)
        
class LinkedList:
    def __init__(self):
        self.head = None # Start with an empty list (no head)
        
    def push_front(self, val):
        # Inserting a new node at the front
        new_node = Node(val, self.head)
        self.head = new_node # Head now becomes the new node
        
    def append(self, val):
        # Inserting new node towards the end
        if not self.head: # If list is empty
            self.head = Node(val) # Create head with this value
            return
        cur = self.head # Otherwise, start at the head value
        while cur.next: # Traverse until we reach last node
            cur = cur.next # Move to the next node
        cur.next = Node(val) # List last node to the new node
        
    def delete_value(self, val):
        # Delete the first node whos value == val
        cur = self.head # Start at the head
        prev = None # Keep track of previous node
        while cur:
            if cur.val == val: # If we found the value
                if prev is None: # Traverse while node remain
                    self.head = cur.next # Remove head forward
                else:
                    prev.next = cur.next # Bypass the current node
                return True # Indicate the deletion success
            prev = cur # Advance previous node to the current one
            cur = cur.next # Advance current to the next one
        return False # Value not found, deletion failed
    
    def to_list(self):
        # Collect values into a Python List
        out = []
        cur = self.head
        while cur:
            out.append(cur.val)
            cur = cur.next
        return out # Returnng the collected values
    
# Demo
ll = LinkedList()
ll.push_front("B")
ll.push_front("A")
ll.append("C")
print(ll.to_list())

ll.delete_value("B")
print(ll.to_list())