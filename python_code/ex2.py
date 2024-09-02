def solution(a, b):
    if (a + b)%2 == 0:
        return "Bob"
    else:
        return "Alice"


if __name__ == "__main__":
    t = int(input().strip())    # Number of test cases
    for i in range(t):
        a, b = list(map(int, input().strip().split())) # Read int array
        print(solution(a, b))
        