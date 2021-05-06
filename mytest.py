import string

def huiwen(text):
    return text==text[::-1]


####方法一：暴力解法
def maxhuiwen(mytext):
    maxlen=0
    huiwenzichuan=''
    for i in range(1,len(mytext)+1):
        for j in range(0,len(mytext)-i+1):
            if huiwen(mytext[j:j+i]):
                maxlen=i
                huiwenzichuan=mytext[j:j+i]
                break
    return maxlen,huiwenzichuan

##方法二，中心法？
def expand(text, left, right):
    while left >= 0 and right < len(text) and text[left] == text[right]:
        left -= 1
        right += 1
    return left + 1, right - 1

def maxhuiwen2(mytext):
    start, end = 0, 0
    for i in range(len(mytext)):
        l1, r1 = expand(mytext, i, i + 1)
        l2, r2 = expand(mytext, i, i)
        if r1-l1>end-start:
            start, end = l1, r1
        elif r2-l2>end-start:
            start, end = l2, r2
    return end-start+1,mytext[start: end+1]
######

if __name__ == "__main__":
    print(maxhuiwen('abbaabb'))
    print(maxhuiwen2('abbaabb'))



