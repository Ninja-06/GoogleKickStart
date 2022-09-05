# Google Kick Start 2020 Coding Practice with Kick Start Session #1 Sample Problem

# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4332/0000000000942404

def remainingCandy(T):
    (candyBags, num_kids) = list(map(int, input().split()))
    c = list(map(int, input().split()))

    Sum = 0
    for i in range(candyBags):
        Sum = c[i] + Sum

    res = Sum % num_kids
    print("Case #{}: {}".format(T, res))


num_testcases = int(input())
for j in range(num_testcases):
    remainingCandy(j + 1)
