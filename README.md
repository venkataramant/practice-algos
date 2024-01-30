# practice-algos

    1. Think what data to store, how type of data structure and how many of them
    2. Findout  patterns
    3. Create a Graph for a Series of Numbers and explore relation between Ans and Graph
# Categories
    0. O(n^2) solutions
    1. Two Pointer approach
        Decide which pointer has to move based upon Greedy*
            Max Profit
    2. Stack (Push and retrieve in some order)
        2.1  2 stacks/arrays
    3. Sorting and Greedy [Min/Max guides which of 2 available one have to discard]
        1. minimum number
        2. Maximum number*
    4. Dynamic Programming
        - Top Down [With Cache]
            DFS and Use Exit conditions and Cache to explore further options
        - Bottom Up [Remember]
            Bottom up- Constructing the answer for smaller set/value and use this information[Cache] to findout the answer for bigger set/value 
            Ans[N]=max/min(choice(1 to chn-1)+ANS[N-Choice]) CAHCE->ANS[0...N-1]

  
# Well Known Problesm
    A. HashMap
        1. Sum of 2 Numbers - O(n)
    B. 2 Pointer Problem /Sliding Window
        1. Sellig Stocks (Move left if value is less, keep track of max profit -- Greedy)
        2. Long substring Without Repeating [Use Set, move left to and check duplicate,no then add right character]
        3. Minimum Window Substring  [Extra 2 HashMaps and variables] [Determine how to know all conditions are met without repeating again and again]
        4. Water tank
    C. 2 extra arrays or 2 HashMap or 2 Heaps
        1. Array product except self.
        2. Anagram
        3. Find out Median of Numbers
        4. K Top Frequent numbers
    D. Sort and Calculate
        1. Anagram
    E. Backtracking (Brute Force)[DFS]
        1. word Search -1 [r *c 4^len_word]
    F. Dynamic Programming [Limited]
        1. Longest Increasing* SubSequence[Relative Order]
    G. Dynamic Programming (Unlimited)
        1. Coin Change - Dynamic Programming Bottom Up 
    H. Greedy


# Definitions
    1. Anagram
         2 words are anagram if they contains same number of characters and values (in any order)
            world == rowld
            map =/= mat
    2. SubString [all characters between 2 ponters and Ordered]
        part of any String [in ORDER]
        world 
            Correct - wor,worl, world 
            Wrong   - (word,row,lord)
    3. SubSequence (any characters between 2 pointers and maintained relative positions)
        part of any String (Need not be in order)

           


# **Big-O Notation**

# 1 O(1) Constant Time

    Array
        Access/Insert At end/Remove At end
    Map 
        Access/Insert/Update/Remove
# 2 O(log n) 
    2^x=n
    x=log(n)
    Binary Search Time
    Every Iteration size becomes into half
# 3 o(sqrt(n))
# 4 O(n) Linear

    Looping Array/List/Set
# 5 O(nlog(n))
    Merge Sort
    Heap Sort
    Heapify
    n+ n log(n) ==> n*log(n)
#  6 O(n^2) O(n^3) O(n^k) 

    Looping 2/3..k times
    Matrics Travelling
    Sorting Algorithms
     Bubble
     Selection
     Insertion

#  7 O(n,m)
    Matric of N rows, M columns

# 8 2^n (2 Non-Polynomial)

    every time, size becomes double/recurrions

    fibonacci Series
# n! Factorial

    Permutations
    Saleperson/Graph problems

# 9 k^n (k Non-Polynomial)
