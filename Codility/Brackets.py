'''
String S = consisting N characters (0<= N <= 200,000);

    conditions that makes S TRUE
        - S is empty
        - properly nested strings: S has the from "(U)" | "[U]" | "{U}" | "VW" | "{[()()]}"
   -> return 1

   conditions that makes S FALSE
        - "( [) () ]"
    -> return 0

Goal: Check S to be properly nested
'''

'''
- Use concept of stack
- left-brackets = ["(", "{", "["]
- right-brackets = [ ")","}","]"]

0. for s in S
    1.  if recent s have left-bracket push to stack
    2.  if recent s meet right-bracket,
        check whether it corresponding well with left-braket, which is most recently pushed element from the stack.
        If Yes, pop the recent element from stack. and continue.
        If No, return 0
return 1

Task Score 100%  Correctness 100%  Performance 100%
'''

def pair_braekts(left, right):
    if left == '(' and right == ')':
        return True
    if left == '[' and right == ']':
        return True
    if left == '{' and right == '}':
        return True
    return False

def solution(S):
    stack = ["BOTTOM"]
    for s in S:
        if s == "(" or s =="{" or s =="[":
            stack += [s]
        else:
            if stack[-1] == "BOTTOM":
                return 0
            recent = stack.pop()
            if not pair_braekts(recent, s):
                return 0

    if stack[-1] != "BOTTOM":
        return 0

    return 1



'''
I got 
Task Score 75%  Correctness 100%  Performance 60%
when I use slice inside of for loop.

list.pop(i) takes O(n), but list.pop() takes O(1)
'''