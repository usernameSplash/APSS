import sys
def input(): return sys.stdin.readline().rstrip()


block_types = [
    [[0, 0], [1, 0], [0, 1]],
    [[0, 0], [0, 1], [1, 1]],
    [[0, 0], [1, 0], [1, 1]],
    [[0, 0], [1, 0], [1, -1]]
]

# x,y 위치에 bolck_type로 덮을 수 있다면 True를, 그렇지 않으면 False를 반환
# delta가 1이면 덮기, -1이면 치우기


def check(data, y, x, block_type, delta):
    result = True
    max_y = len(data)
    max_x = len(data[0])

    for i in range(3):
        dy = y + block_types[block_type][i][0]
        dx = x + block_types[block_type][i][1]

        if dy < 0 or dy >= max_y or dx < 0 or dx >= max_x:
            result = False
        else:
            data[dy][dx] += delta
            if data[dy][dx] > 1:
                result = False

    return result


def solve(data):
    x = -1
    y = -1
    result = 0

    # 가장 좌상단에 있는 흰 칸의 위치를 조사한다.
    for yy in range(len(data)):
        for xx in range(len(data[yy])):
            if data[yy][xx] == 0:
                y = yy
                x = xx
                break
        if y != -1:
            break

    # 보드를 모두 덮었으면 1을 반환한다.
    if y == -1:
        return 1

    for t in range(4):
        if check(data, y, x, t, 1):
            result += solve(data)

        check(data, y, x, t, -1)
    return result


def main():
    C = int(input())

    for _ in range(C):
        # 학생들간의 관계를 나타내는 배열, areFriend[i][j] = 1이면 i와 j는 친구, 0이면 친구 아님
        h, w = [int(v) for v in input().split()]

        board = []
        data = [[0 for _ in range(w)] for __ in range(h)]

        for _ in range(h):
            board.append(input())

        N = 0
        boardToData = {'.': 0, '#': 1}

        for y in range(h):
            for x in range(w):
                data[y][x] = boardToData[board[y][x]]

        if N % 3 != 0:
            print(0)
            continue

        print(solve(data))


if __name__ == "__main__":
    main()
