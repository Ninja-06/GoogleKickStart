#Google Kick Start 2020 Coding Practice with Kick Start Session #1 H-index 

# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4332/0000000000941e56

# H_index using heap

from heapq import heapify, heappush, heappop


def h_index(n, c):
    arr = []
    h = 1
    heapify(arr)
    ans = []

    # to get the H-Index scores after each paper

    for i in range(len(c)):

        if c[i] >= h:
            heappush(arr, c[i])

        while arr and arr[0] <= h:
            heappop(arr)
        if len(arr) == h + 1:
            h = h + 1
        ans.append(h)

    return ans


if __name__ == '__main__':
    t = int(input())

    for test_case in range(1, t + 1):
        n = int(input())  # The number of papers

        citations = list(map(int, input().split()))  # The number of citations for each paper

        h_index_scores = h_index(n, citations)
        print("Case #" + str(test_case) + ": " + ' '.join(map(str, h_index_scores)))
