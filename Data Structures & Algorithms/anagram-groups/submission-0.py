class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str = [''.join(sorted(s)) for s in strs]
        final_list = []
        visited = set()

        for i in range(len(strs)):
            if i in visited:         
                continue
            new_list = [strs[i]]
            for j in range(i + 1, len(strs)):
                if j not in visited and sorted_str[i] == sorted_str[j]:
                    new_list.append(strs[j])
                    visited.add(j)    
            final_list.append(new_list)

        return final_list