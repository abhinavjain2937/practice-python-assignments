def removeDuplicates(s: str) -> str:
    """
    Removes all adjacent duplicates from a string using a stack-like approach.
    """
    # A Python list can be used as a stack.
    stack = []
    
    # 1. Iterate through each character in the input string.
    for char in s:
        # 2. Check if the stack is not empty AND 
        #    if the current character matches the character at the top of the stack.
        if stack and stack[-1] == char:
            # 3. If they match, it's an adjacent duplicate. Pop the stack.
            stack.pop()
        else:
            # 4. If they don't match, push the current character onto the stack.
            stack.append(char)
            
    # 5. Join the characters remaining in the stack to form the final string.
    return "".join(stack)

# --- Running the Examples ---

# Example 1:
input1 = "abbaca"
output1 = removeDuplicates(input1)
print(f"Input: \"{input1}\"")
print(f"Output: \"{output1}\"\n") # Expected: "ca"

# Example 2:
input2 = "azxxzy"
output2 = removeDuplicates(input2)
print(f"Input: \"{input2}\"")
print(f"Output: \"{output2}\"\n") # Expected: "ay"

# Example 3:
input3 = "aaaaaaaaa" # All duplicates
output3 = removeDuplicates(input3)
print(f"Input: \"{input3}\"")
print(f"Output: \"{output3}\"") # Expected: "a" (if odd) or "" (if even)