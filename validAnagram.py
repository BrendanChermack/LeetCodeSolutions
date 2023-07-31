class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #hashmap approach 2 hash maps(one for each string) with letters counter for the string
        #then compare the hashmaps counts to see if they are equal
        #O(s+t) aka O(n)
        #memory is s+t seocnd solution solves this
        countT, countS = {}, {}
        if len(s) != len(t):
            return False
        
        #builds hashmaps
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        #compare the hashmaps counts to see if they are equal
        for c in countS:
            if countS[c] != countT.get([c]):
                return False
        
        return True
    
    # The other solution is to sort the letters in alphabetical order then compare them itf they are the same they will be an anagram of each other however 
    # it is assumed this doesnt take extra emory but it does and it depend on the algo for how much best case consant memory
        #the solution for the second way
        return sorted(t) == sorted(s)
