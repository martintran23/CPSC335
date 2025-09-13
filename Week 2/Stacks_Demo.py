# Stack (LIFO) implementation

# Create an empty stack
stack = []

# Push elements (append adds to the top)
stack.append("homepage")
stack.append("news")
stack.append("article")
print("Stack after pushes:", stack) # shows current stack state

# Pop the top element (LIFO)
last = stack.pop()
print("Popped:", last)
print("Top Now:", stack[-1])

# Reverse a string using a stack
s = "hello"
st = [] # Stack for characters
for ch in s:
    st.append(ch)
rev_chars = []
while st:
    rev_chars.append(st.pop()) # Pop characters (reverse order)
rev = "".join(rev_chars) # Joining characters into a string
print("Reversed:", rev)