# A stack is a unique collection of elements with the unique feature being that they are last in first out

# 3 operations: push, pop, peek
# push adds a new element to the top of the stack
# pop removes the top element from the stack
# peek looks at the top element of the stack
# time complexity O(1), or constant time, which is why they are optimal for certain problems

# stack initialized as an empty list
# stack = []
# add elements by appending to the list
# stack.append(1)
# stack.append(6)
# pop is pretty straightforward
# stack.pop()
# peek is done like this
# stack[-1]

# stacks are useful in problems with matching or validating parentheses (LC 20 and 2116)
# because you need to make sure that the most recent opening bracket is closed before any of the other brackets
# questions involving nested equations or things that needs to be solved in a certain order (LC 150 and 224)
# any question where you have to undo something or look at the history (LC 1472)

# Leetcode 20
close_to_open = {
    ")": "(",
    "}": "{",
    "]": "["
}
stack = []

for bracket in s:
    if bracket in close_to_open:
        if not stack:
            return False
        top = stack.pop()  # closing bracket
        if close_to_open[bracket] != top:
            return False
    else:
        stack.append(bracket)  # open bracket

if stack:
    return False
else:
    return True

# Monotonic stack
# This is a stack that follows a specific pattern in ordering the elements, either increasing or decreasing from
# bottom to top
# This is often used to optimize algorithms by efficently finding the next element that satisfies a certain
# condition in a sequence
# Creating monotonic stack is O(n) where sort is O(n logn)
# LC 739 is an example of where you can use a monotonic stack