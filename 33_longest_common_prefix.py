
def longestCommonPrefix(strs: list[str]) -> str:
    """ This function finds the longest common prefix string amongts a list of strign.
    
    Args:
        - list [str]: A list of strings to search for the longest commond prefix.
        
    Returns:
        - str: The longest commond prefix string among the input strings.

    Example:

        >>> strs = ["flower", "flow", "flight"]
        'fl' 
    """
    if not strs:
        return ""
    print(strs)
    prefix = ""
    
    min_len = min([len(s) for s in strs])
    #print(min_len)
    for i in range(min_len):
        #print(prefix)
        curr_char = strs[0][i]
        #print(curr_char)
        for j in range(1, len(strs)):
            if strs[j][i] != curr_char:
                return prefix
        prefix += curr_char
    return prefix


strs = ["flower","flow","flight","flflfl"]
lol = longestCommonPrefix(strs)
print(lol)

















""" 
This solution uses the fact that the longest common prefix 
of a set of strings must be a prefix of the shortest string 
in the set. It first checks if the input array is empty, and 
returns an empty string if it is. It then initializes an empty 
string prefix and finds the length of the shortest string in the 
array using min() and a list comprehension.

Next, the solution iterates over the characters of the shortest 
string, and checks if the same character appears in the same 
position of all other strings in the array. If it does, the 
character is added to the prefix, and the iteration continues 
to the next character. If not, the prefix found so far is 
returned. If the loop completes successfully, the entire 
shortest string is the common prefix, and is returned as 
the result.

Write a function to find the longest common prefix string 
amongst an array of strings. If there is no common prefix, 
return an empty string "".

Example 1:

    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:

    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.
"""