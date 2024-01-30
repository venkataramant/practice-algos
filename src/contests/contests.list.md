# problem 1 -- 100206. Find the Maximum Number of Elements in Subset
    You are given an array of positive integers nums.

    You need to select a subset of nums which satisfies the following condition:

        You can place the selected elements in a 0-indexed array such that it follows the pattern: [x, x2, x4, ..., xk/2, xk, xk/2, ..., x4, x2, x] (Note that k can be be any non-negative power of 2). For example, [2, 4, 16, 4, 2] and [3, 9, 3] follow the pattern while [2, 4, 8, 4, 2] does not.

    Return the maximum number of elements in a subset that satisfies these conditions.

    

    Example 1:

    Input: nums = [5,4,1,2,2]
    Output: 3
    Explanation: We can select the subset {4,2,2}, which can be placed in the array as [2,4,2] which follows the pattern and 22 == 4. Hence the answer is 3.

    Example 2:

    Input: nums = [1,3,2,4]
    Output: 1
    Explanation: We can select the subset {1}, which can be placed in the array as [1] which follows the pattern. Hence the answer is 1. Note that we could have also selected the subsets {2}, {4}, or {3}, there may be multiple subsets which provide the same answer. 

# problem 2 - 100195. Alice and Bob Playing Flower Game
    100195. Alice and Bob Playing Flower Game

        User Accepted: 430
        User Tried: 676
        Total Accepted: 434
        Total Submissions: 904
        Difficulty: Medium

    Alice and Bob are playing a turn-based game on a circular field surrounded by flowers. The circle represents the field, and there are x flowers in the clockwise direction between Alice and Bob, and y flowers in the anti-clockwise direction between them.

    The game proceeds as follows:

        Alice takes the first turn.
        In each turn, a player must choose either the clockwise or anti-clockwise direction and pick one flower from that side.
        At the end of the turn, if there are no flowers left at all, the current player captures their opponent and wins the game.

    Given two integers, n and m, the task is to compute the number of possible pairs (x, y) that satisfy the conditions:

        Alice must win the game according to the described rules.
        The number of flowers x in the clockwise direction must be in the range [1,n].
        The number of flowers y in the anti-clockwise direction must be in the range [1,m].

    Return the number of possible pairs (x, y) that satisfy the conditions mentioned in the statement.

    

    Example 1:

    Input: n = 3, m = 2
    Output: 3
    Explanation: The following pairs satisfy conditions described in the statement: (1,2), (3,2), (2,1).

    Example 2:

    Input: n = 1, m = 1
    Output: 0
    Explanation: No pairs satisfy the conditions described in the statement.

    

    Constraints:

        1 <= n, m <= 105


# problem 3 -- 100215. Number of Changing Keys
    You are given a 0-indexed string s typed by a user. Changing a key is defined as using a key different from the last used key. For example, s = "ab" has a change of a key while s = "bBBb" does not have any.

    Return the number of times the user had to change the key.

    Note: Modifiers like shift or caps lock won't be counted in changing the key that is if a user typed the letter 'a' and then the letter 'A' then it will not be considered as a changing of key.

    

    Example 1:

    Input: s = "aAbBcC"
    Output: 2
    Explanation: 
    From s[0] = 'a' to s[1] = 'A', there is no change of key as caps lock or shift is not counted.
    From s[1] = 'A' to s[2] = 'b', there is a change of key.
    From s[2] = 'b' to s[3] = 'B', there is no change of key as caps lock or shift is not counted.
    From s[3] = 'B' to s[4] = 'c', there is a change of key.
    From s[4] = 'c' to s[5] = 'C', there is no change of key as caps lock or shift is not counted.

    Example 2:

    Input: s = "AaAaAaaA"
    Output: 0
    Explanation: There is no change of key since only the letters 'a' and 'A' are pressed which does not require change of key.

# problem 4 100179. Minimize OR of Remaining Elements Using Operations



    You are given a 0-indexed integer array nums and an integer k.

    In one operation, you can pick any index i of nums such that 0 <= i < nums.length - 1 and replace nums[i] and nums[i + 1] with a single occurrence of nums[i] & nums[i + 1], where & represents the bitwise AND operator.

    Return the minimum possible value of the bitwise OR of the remaining elements of nums after applying at most k operations.

    

    Example 1:

    Input: nums = [3,5,3,2,7], k = 2
    Output: 3
    Explanation: Let's do the following operations:
    1. Replace nums[0] and nums[1] with (nums[0] & nums[1]) so that nums becomes equal to [1,3,2,7].
    2. Replace nums[2] and nums[3] with (nums[2] & nums[3]) so that nums becomes equal to [1,3,2].
    The bitwise-or of the final array is 3.
    It can be shown that 3 is the minimum possible value of the bitwise OR of the remaining elements of nums after applying at most k operations.

    Example 2:

    Input: nums = [7,3,15,14,2,8], k = 4
    Output: 2
    Explanation: Let's do the following operations:
    1. Replace nums[0] and nums[1] with (nums[0] & nums[1]) so that nums becomes equal to [3,15,14,2,8]. 
    2. Replace nums[0] and nums[1] with (nums[0] & nums[1]) so that nums becomes equal to [3,14,2,8].
    3. Replace nums[0] and nums[1] with (nums[0] & nums[1]) so that nums becomes equal to [2,2,8].
    4. Replace nums[1] and nums[2] with (nums[1] & nums[2]) so that nums becomes equal to [2,0].
    The bitwise-or of the final array is 2.
    It can be shown that 2 is the minimum possible value of the bitwise OR of the remaining elements of nums after applying at most k operations.

    Example 3:

    Input: nums = [10,7,10,3,9,14,9,4], k = 1
    Output: 15
    Explanation: Without applying any operations, the bitwise-or of nums is 15.
    It can be shown that 15 is the minimum possible value of the bitwise OR of the remaining elements of nums after applying at most k operations.

    

    Constraints:

        1 <= nums.length <= 105
        0 <= nums[i] < 230
        0 <= k < nums.length

