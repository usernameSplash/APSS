import sys
def input(): return sys.stdin.readline().rstrip()


def solve(taken, areFriend):
    n = len(taken)
    firstFree = -1
    for i in range(len(taken)):
        if not taken[i]:
            firstFree = i
            break

    if firstFree == -1:
        return 1

    result = 0

    for i in range(firstFree+1, n):
        if not taken[i] and areFriend[firstFree][i]:
            taken[firstFree] = True
            taken[i] = True
            result += solve(taken, areFriend)
            taken[firstFree] = False
            taken[i] = False

    return result


def main():
    C = int(input())

    for _ in range(C):
        # 학생들간의 관계를 나타내는 배열, areFriend[i][j] = 1이면 i와 j는 친구, 0이면 친구 아님
        areFriend = [[0 for _ in range(10)] for __ in range(10)]

        n, m = [int(v) for v in input().split()]

        data = [int(v) for v in input().split()]

        for i in range(0, len(data), 2):
            areFriend[data[i]][data[i+1]] = 1
            areFriend[data[i+1]][data[i]] = 1

        print(solve([False for _ in range(n)], areFriend))


if __name__ == "__main__":
    main()
