# 6장 문자열 조작

# 1. 유효한 팰린드

# 나의 문제 풀이.
def isPalindrome(a):
    a = a.lower()
    b = []
    for i in range(len(a)):
        if a[i].isalnum():
            b.append(a[i])

    c = b[::-1]

    if b == c:
        print("true")
    else:
        print("false")


isPalindrome("race a car")


# 데크 자료형을 이용한 최적화.
# deque를 명시적으로 선언하면 속도를 더 높일 수 있다.
import collections;
from typing import Deque


def isPalindrome(s):
    # 자료형 데크로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # 프로그램의 성능을 위해 하나씩 검수하여 false가 나오는 경우의 성능을 높이자.
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            print("false")
            return False

    print("true")

isPalindrome("A man, a plan, a canal: Panama")


# 슬라이싱 사용
import re
def isPalindrome(s):
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    if s == s[::-1]:
        print("true")
    else:
        print("false")
isPalindrome("A man, a plan, a canal: Panama")

# 2. 문자열 뒤집기

# 나의 풀이
def reverseString(s):
    reverse_s = s[::-1]
    print(reverse_s)

s = ["h", "e", "l", "l", "o"]
reverseString(s)
#
# 투 포인터를 이용한 스왑
def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    print(s)
s = ["h", "e", "l", "l", "o"]
reverseString(s)
#
# 파이썬다운 방식
def reverseString(s):
    s.reverse()
    print(s)
s = ["h", "e", "l", "l", "o"]
reverseString(s)

# 3. 가장 흔한 단어
import re

def mostCommonWord(s, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', s) # 정규식에서 w는 단어 문자를 뜻하며, ^은 not을 의미. 따라서 단어 문자가 아닌 모든 문자를 공백으로 치환.
             .lower().split() # 기호들을 지웠고, 문자를 소문자로 통일하고 split으로 나누어 저장.
                if word not in banned] # 리스트 조건절에는 banned에 포함되지 않은 단어만을 words에 저장.

    counts = collections.Counter(words) # counter를 통해 각 단어의 빈도수를 저장한다.
    # 위 counts 결과: Counter({'ball': 2, 'bob': 1, 'a': 1, 'the': 1, 'flew': 1, 'far': 1, 'after': 1, 'it': 1, 'was': 1})
    print(counts.most_common(1)[0][0]) # 가장 흔히 등장하는 단어 첫 번쨰 값을 most_common(1)로 추출, 이는 [('ball', 2)]로 출력, [0][0]을 붙여 ball만 나오게 한다.


s = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ['hit']
mostCommonWord(s, banned)

#4. 그룹 애너그램
# 정렬하여 딕셔너리에 추가
import collections

def groupAnagram(s):
    anagrams = collections.defaultdict(list) # 존재하지 않는 키를 삽입하려할 경우 keyerror가 발생하므로 에러가 나지 않도록 다음과 같이 항상 디폴트를 생성하는 defaultdict() 선언.

    for word in s:
        anagrams[''.join(sorted(word))].append(word) # 문자열을 잘 정렬하여 결과를 리스트 형태로 리턴, join으로 합쳐 키로 사용하는 딕셔너리로 구성, 에너그램끼리는 같은 키를 갖게 되고 여기에 append하는 형태가 된다.
        #키/값 해시 테이블


    print(anagrams.values())

s = ["eat", "tea", "tan", "ate", "nat", "bat"]
groupAnagram(s)

n = int(input())
a = []

for i in range(n):
    a.append(input())
base = list(a[0])
print(base)

for file in a[1:]:
    for j in range(len(file)):
        if base[j] == "?":
            pass
        elif base[j] != file[j]:
            base[j] = "?"
print(''.join(base))

n, k = map(int, input().split())

a = []
list_a = []
base = []

for i in range(n):
    a.append(input())

# {'n', 'c', 'r', 'a', 'i', 't'}

for j in range(len(a)):
    set_a = set(list(a[j]))
    list_a.append(set_a)

print(list_a)

for h in range(len(list_a)):
    if k == len(list_a[h]):
        base.append(list_a[h])
print(base)

for b in range(len(base)):
    for c in range(k):
        base[b][c]

# 백준 문자열 반복
t = int(input())
s = []

for i in range(t):
    s.append(input().split())

# [['3', 'ABC'], ['5', '/HTP']]

for j in range(len(s)):
    k_sen = ''
    kk = s[j][1]
    a = s[j][0]

    for k in kk:
        repeat = k * int(a)
        k_sen += repeat
    print(k_sen)


# 백준 단어 공부
# import collections

a = input()

a = list(a)
b = collections.Counter(a)
most = b.most_common()
if len(most) <= 1:
    print(most[0][0].upper())

elif most[0][1] == most[1][1]:
    print("?")
else:
    print(most[0][0].upper())

a = input()
a = a.lower()
a = list(a)
a = sorted(a)
b = []
c = set(a)
c = list(c)

print(a)
c = sorted(c)
print(c)

if len(a) == 1:
    print(a[0].upper())
    pass

for i in range(len(c)):
    count_a = a.count(c[i])
    c.append(count_a)

print(c)

# if len(a) > 1:
#     if b[-1] == b[-2]:
#         print("?")
#     else:
#         print(c[-1].upper())






















