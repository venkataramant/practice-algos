from typing import DefaultDict
from collections import defaultdict
class Solution:
    def closeStrings_2(self, word1: str, word2: str) -> bool:
        n1 = len(word1)
        n2 = len(word2)

        if n1 != n2:
            return False

        if word1 == word2:
            return True
        def c_c(word):
                a=dict()
                for c in word:
                    a[c]=a.get(c,0)+1
                return a
        return sorted(c_c(word1).values())==sorted(c_c(word2).values()) and sorted(c_c(word1).keys())==sorted(c_c(word2).keys())
    def closeStrings_best(self, word1: str, word2: str) -> bool:
        if len(word1)==len(word2):
            word_count=defaultdict(int)
            for char in set(word1):
                word_count[word1.count(char)]+=1
                word_count[word2.count(char)]-=1
            for value in word_count.values():
                if value!=0:
                    return False
            return True
              
        return False
      