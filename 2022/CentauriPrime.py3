# Google Kick Start 2020 Coding Practice with Kick Start Session #1 Centauri Prime

# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4332/0000000000941ec5

# centuari prime

import re


# get_ruler function

def get_ruler(kingdom):
    ruler = ''
    vowel = '(a|e|i|o|u|A|E|I|O|U)$'
    y = '(y|Y)$'

    # to determine the ruler of the kingdom

    if re.search(vowel, kingdom):
        ruler = "Alice"
    else:
        if re.search(y, kingdom):
            ruler = "nobody"
        else:
            ruler = "bob"
    return ruler


def main():
    # Get the number of test cases

    T = int(input())
    for t in range(T):
        # Get the kingdom

        kingdom = input()
        print('Case #%d: %s is ruled by %s.' % (t + 1, kingdom, get_ruler(kingdom)))


if __name__ == '__main__':
    main()
