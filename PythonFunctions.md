# Python
	
	map
	zip

# functions ascii
```python
from bitstring import BitArray
bin()
chr()
unicode()
ord()

BitArray(bin=bString).init
isalnum()

```
# heap
```python
import heapq
queue=[]
heapq.heappush(queue,3)
heapq.heappush(queue,4)
heapq.heappop(queue)
```
# collections
```python
from collections import deque
from collections import Counter # Counter(str) [map contains each character and no of times it appeared]
```

# Range and Slicing
```python

for x in range(10,-1,-1):
	print(x) # Prints from 10 to 0

numbers=[x for x in range(11)]

for num in nums[::-1]:
	print(num) # Print 10 to 0

for num in nums[-2::-1]:
	print(num) # Print from 9 to zero
