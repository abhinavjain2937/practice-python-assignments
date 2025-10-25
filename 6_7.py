def countConsistentStrings(allowed: str, words: list[str]) -> int:
    """
    Counts the number of consistent strings in an array.
    A string is consistent if all its characters are in the 'allowed' string.
    """
    # 1. Convert the allowed string into a set. 
    #    This provides O(1) average time lookups, which is very efficient.
    allowed_set = set(allowed)
    consistent_count = 0
    
    # 2. Iterate through each word in the input list.
    for word in words:
        is_consistent = True
        # 3. Check each character of the current word.
        for char in word:
            # 4. If a character is not in the allowed set, the word is not consistent.
            if char not in allowed_set:
                is_consistent = False
                break # Optimization: No need to check the rest of the characters.
        
        # 5. If the inner loop completed without finding any invalid characters,
        #    increment the counter.
        if is_consistent:
            consistent_count += 1
            
    return consistent_count

# --- Running the Examples ---

# Example 1:
allowed1 = "ab"
words1 = ["ad","bd","aaab","baa","badab"]
output1 = countConsistentStrings(allowed1, words1)
print(f"Input: allowed = \"{allowed1}\", words = {words1}")
print(f"Output: {output1}\n") # Expected: 2

# Example 2:
allowed2 = "abc"
words2 = ["a","b","c","ab","ac","bc","abc"]
output2 = countConsistentStrings(allowed2, words2)
print(f"Input: allowed = \"{allowed2}\", words = {words2}")
print(f"Output: {output2}\n") # Expected: 7

# Example 3:
allowed3 = "cad"
words3 = ["cc","acd","b","ba","bac","bad","ac","d"]
output3 = countConsistentStrings(allowed3, words3)
print(f"Input: allowed = \"{allowed3}\", words = {words3}")
print(f"Output: {output3}") # Expected: 4