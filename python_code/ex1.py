def solution(a, b, x):
    return 3*x - a - b


if __name__ == "__main__":
    a, b, x = list(map(int, input().strip().split())) # Read int array
    print(solution(a, b, x))
