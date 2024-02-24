'''
Given an integer(+ve or -ve) consisting of at least one 5 in its digits(can have more than one 5). Return the maximum value by deleting exactly one 5 from its digit.
Ex: N = 1598 => result = 198(remove the only 5 from the sequence)
N = 150,958 => result = 15,098(we wanna return the maximum value 15,098 > 10,958)
N = -5859 => result = -589 ( -589>- 859)

'''


def deleteoneFive(num):
    index = 0
    found = False
    while(num // pow(10, index) > 0):
            if num // pow(10, index) % 10 == 5:
                break
            index += 1
            
    print("index", index, num // pow(10, index) % 10)
    if num // pow(10, index) % 10 == 5:
        print(num // pow(10, index+1)*pow(10,index)+num % pow(10, index))
    else:
        return num


if __name__ == "__main__":
    num = 150958
    deletedValue = deleteoneFive(num)
    print(num, "-->", deletedValue)
