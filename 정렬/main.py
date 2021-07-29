# 백준 정렬 1015번 수열 정렬
# 내 풀이. 다른 사람들 풀이와 비교하면 나는 ans를 만들어 런타임에러가 났나 보다.
# 변수를 많이 만든 탓인가 싶다...?!
# 그도 그러네.. 정렬 문제인데 정렬을 안 썼다ㅠ 멍청이냐고..

def sort_1(n, b):
    A = list(range(n))
    ans = []

    for i in range(n):
        ans.append(str(A[b[i]-1]))

    ans = ' '.join(ans)

    print(ans)

n = int(input())
b = list(map(int, input().split()))
n = 3
b = [2, 3, 1]

sort_1(n, b)

# 런타임 에러 뜬 풀이 (출력은 잘 되지만)
n = int(input())
b = list(map(int, input().split()))

A = list(range(n))
ans = []

for i in range(n):
    ans.append(str(A[b[i]-1]))

ans = ' '.join(ans)

print(ans)

# 맞는 풀이
n = int(input())
t = list(map(int, input().split())) # t = [2, 3, 1]
s_li = sorted(t) # s_li = [1, 2, 3]
li = []
for i in range(n):
    idx = s_li.index(t[i]) # idx = s_li.index(2) -> idx = 1
    li.append(idx) # li = [1] ---> [1, 2, 0]
    s_li[idx] = -1 # s_li[1] = -1 -> s_li = [1, -1, 3]
print(*li) # 포인터를 쓰면 리스트 요소들만 출력받을 수 있다. [2, 1, 3] -> 2 1 3


# 백준 알고리즘 1026번 보물
# 우왁!!! 한 번에 맞았어ㅠ 기분 증말 좋다...
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0

a = sorted(a)
b = sorted(b, reverse=True)

for i in range(n):
    ans += a[i] * b[i]

print(ans)

#  백준 알고리즘 1202번 보석 도둑
# 막혀서 오래 고민하다가 내일 풀기로 결정...!

from operator import itemgetter

n, k = map(int, input().split())

fm=[list(map(int, input().split())) for _ in range(n)]
fk = [int(input()) for _ in range(k)]
ans = 0
a = 0
fm.sort(key=itemgetter(1), reverse=True)


