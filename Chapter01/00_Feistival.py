'''
Author : Kyeongmin Kim

하루에 한 팀의 밴드가 콘서트,
이미 L개의 밴드는 섭외 완료,

앞으로 N일동안의 공연장 대여비용을 알고 있고, 이 중 L일 이상을 연속하여 대여하되 평균 비용을 최소화하기

M : 공연장 대여비용
'''

import sys
input = sys.stdin.readline


'''
0~(N-1)의 범위를 갖는 정수 i에 대해, 모든 M[i:L]을 구해본다.
그 다음, L~(N-1-i)의 범위를 갖는 정수 j에 대해, 모든 M[i:j]의 값을 구해보고
그 중 최소값을 반환한다.
'''


def solve(N, L, M):
    result = 999999999999
    table = [0] * (N+1)

    table[0] = 0

    for i in range(1, N+1):
        table[i] = table[i-1] + M[i]

    for i in range(0, N+1):
        for j in range(i+L, N+1):
            result = min(result, (table[j] - table[i]) / (j-i))

    return result


def main():
    c = int(input())

    for _ in range(c):
        N, L = [int(v) for v in input().split()]
        M = [0] + [int(v) for v in input().split()]
        print(solve(N, L, M))


if __name__ == "__main__":
    main()
