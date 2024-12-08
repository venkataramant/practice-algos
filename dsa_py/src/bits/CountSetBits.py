def countSetBits(num):
    countsMap=dict()
    countsMap[0]=0
    countsMap[1]=1
    countsMap[2]=1
    for newNumber in range(3,num+1):
        val1=newNumber//2
        val2=newNumber%2
        countsMap[newNumber]=countsMap[val1]+val2
    print(countsMap)
    return sum(countsMap.values())
    
def find1CountOfNum(num,countsMap):
 
    val1=newNumber//2
    val2=newNumber%2
    countsMap[num]=countsMpa[val1]+val2

print(countSetBits(64))
        
'''
01: 1
02: 1
03: 2, 4: 1
05: 2, 6: 2, 7: 3, 8: 1
09: 2, 10: 2, 11: 3, 12: 2, 13: 3, 14: 3, 15: 4, 16: 1
17: 2, 18: 2, 19: 3, 20: 2, 21: 3, 22: 3, 23: 4, 24: 2,25: 3, 26: 3, 27: 4, 28: 3, 29: 4, 30: 4, 31: 5, 32: 1
33: 2, 34: 2, 35: 3, 36: 2, 37: 3, 38: 3, 39: 4, 40: 2,41: 3, 42: 3, 43: 4, 44: 3, 45: 4, 46: 4, 47: 5, 48: 2,49: 3, 50: 3, 51: 4, 52: 3, 53: 4, 54: 4, 55: 5, 56: 3,57: 4, 58: 4, 59: 5, 60: 4, 61: 5, 62: 5, 63: 6, 64: 1}
there is pattern here to solve to use it
'''
    
    