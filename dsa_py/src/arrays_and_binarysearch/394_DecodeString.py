class Solution:
    def decodeString_mine(self, s: str) -> str:
        print("input",s)
        # "3[a2[c]]"
        
        # if not digit or [] append to ans
        # on first digit dectection ,create flag1(0,1,2) and off flag1 after detecting first [
        # 0 not started, 1 started 2 completed 
        # until flag1 (2), capture all characters into a separate string, add [  to queue and dequeue
        # when dequeued once it empty that is time for evaluating value.
        # if more than 2[ there send it for decodeString

        ans=""
        digit_flag=0
        nested_flag=0
        digital_str=""
        decode_str=""
        b_queue=[]
        for x in s:
            # print(x,digit_flag,nested_flag,digital_str,decode_str,b_queue)
            if str.isdigit(x):
                if digit_flag==0:
                    digit_flag=1
                    digital_str=digital_str+x
                elif digit_flag==1:
                    digital_str=digital_str+x
                else:
                    decode_str=decode_str+x
            elif x=="[":
                if digit_flag==1:
                    digit_flag=2 # digit capture over
                    b_queue.append(x)
                elif digit_flag==2: # nested word
                    nested_flag=1
                    decode_str=decode_str+x
                    b_queue.append(x)
            elif x=="]":
                if nested_flag==1:
                    decode_str=decode_str+x
                b_queue.pop()
                if len(b_queue)==0:
                    # completed capturing decode string
                    if nested_flag==1:
                        ans=ans+(self.decodeString(decode_str[:-1])*int(digital_str))
                    else: # non nested decode Str
                        ans=ans+(decode_str*int(digital_str))
                    digit_flag=0
                    nested_flag=0
                    digital_str=""
                    decode_str=""
                    b_queue=[]
            else:
                if digit_flag==0:
                    ans=ans+x
                else:
                    decode_str=decode_str+x
        # print(ans)
        return ans

    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = ''

        multiplier = 0
        is_nested = False
        cur_str = ''
        for char in s:
            if char.isdigit():
                multiplier = multiplier * 10 + int(char)
            elif char == '[':
                stack.append(multiplier)
                stack.append(cur_str)
                multiplier = 0
                cur_str = ''
            elif char == ']':
                prev_str = stack.pop()
                prev_multiplier = stack.pop()
                cur_str = prev_str + prev_multiplier * cur_str
            else:
                cur_str += char
        
        return cur_str


'''
Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
'''