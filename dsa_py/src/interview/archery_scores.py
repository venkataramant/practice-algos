"""
Suppose you are required to right a solution for an archery competition (or dart or any similar sports).

The rule of the competition is as follow:
- each attempt has different score given to the player before he/she begins
- each attempt is either hit or miss (no partial hit)
- if the player hits the mark then gets the points allocated for that attempt otherwise gets 0 (no partial score)

Write a method that returns list of total possible scores given list of scores announced for each attempt.
"""

"""
input_scores =[2,3,1]
possibilies 
Attempts        possibilites
1                   2 or 0
2                   3 or 0
3                   1 or 0
4                   5 or 0
-------------
0, 2, 3 ,5 ,1 3  4 6
5  7 10 15 8 10 9 10
2*2*2*2*2 (2^n)

both time and space (2^n)
"""

def score_calculator(nums):
    ans=set()
    ans.add(0)
    if not nums:
        return ans
    for num in nums:
        temp_set=set()
        for old_score in ans:
            temp_set.add(old_score+num)
        ans=ans.union(temp_set)
    return sorted(ans)

scores = [x for x in range(4)]
print("input:: ",scores ,"output::",score_calculator(scores))
        