class Solution:

    def asteroidCollision_working1(self, asteroids: List[int]) -> List[int]:

        queue=[]
        for c_asteroid in asteroids:
            # Previous one is Positive and latest one is Negative collide
            while(len(queue)>0 and queue[len(queue)-1]>0 and c_asteroid<0):
                last_a=queue[len(queue)-1]
                if queue[len(queue)-1]==abs(c_asteroid):
                    # Neutral remove positive and break
                    queue.pop()
                    c_asteroid=None
                    break
                elif queue[len(queue)-1]>abs(c_asteroid):
                    # big positive wins do nothing,break
                    c_asteroid=None
                    break
                else:
                    # negative c_asteroid wins, pop and check with lest one
                    queue.pop()
                    continue

            if c_asteroid:
                queue.append(c_asteroid)
        return queue

'''
Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
'''
                