# Given an array of strings strs, group the anagrams together. You can return 
# the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
#  Input: strs = ["eat","tea","tan","ate","nat","bat"] 
#  
# 
#  Output: [["bat"],["nat","tan"],["ate","eat","tea"]] 
# 
#  Explanation: 
# 
#  
#  There is no string in strs that can be rearranged to form "bat". 
#  The strings "nat" and "tan" are anagrams as they can be rearranged to form 
# each other. 
#  The strings "ate", "eat", and "tea" are anagrams as they can be rearranged 
# to form each other. 
#  
# 
#  Example 2: 
# 
#  
#  Input: strs = [""] 
#  
# 
#  Output: [[""]] 
# 
#  Example 3: 
# 
#  
#  Input: strs = ["a"] 
#  
# 
#  Output: [["a"]] 
# 
#  
#  Constraints: 
# 
#  
#  1 <= strs.length <= 10⁴ 
#  0 <= strs[i].length <= 100 
#  strs[i] consists of lowercase English letters. 
#  
# 
#  Related Topics Array Hash Table String Sorting 👍 21117 👎 723
from collections import defaultdict

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = defaultdict(list)
        for i, word in enumerate(strs):
            data[''.join(sorted(word))].append(strs[i])

        return list(data.values())

# leetcode submit region end(Prohibit modification and deletion)
