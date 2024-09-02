def solution(n, file_types, name_lengths):
    n_dels = 0
    n_file_y = len([f for f in file_types if f == 'y'])
    deleted = set()

    l, r = 0, 0
    while r < n:
        for i in range(1, n):
            if file_types[i] == 'y' and file_types[i - 1] == 'n':
                l = i - 1
            break
        for i in range(l + 1, n):
            if file_types[i] == 'n' and file_types[i - 1] == 'y':
                r = i
            break
        

    while len(deleted) < n_file_y:
        high_y_len = 0
        high_y_pos = 0
        for i in range(n):
            if file_types[i] == 'y' and name_lengths[i] > high_y_len and i not in deleted:
                high_y_len = name_lengths[i]
                high_y_pos = i

        # Find the left and right boundaries
        for i in range(high_y_pos, -1, -1):
            l = i
            if file_types[i] == "n" and name_lengths[i] >= high_y_len:
                break
        for i in range(high_y_pos, n):
            r = i
            if file_types[i] == "n" and name_lengths[i] >= high_y_len:
                break

        # Find the longest file cannot be deleted in the interval (l, r)
        high_n_len = 0
        for i in range(l + 1, r):
            if file_types[i] == "n" and name_lengths[i] > high_n_len:
                high_n_len = name_lengths[i]

        # Delete files in the interval [l, r]
        for i in range(l, r + 1):
            if file_types[i] == "y" and name_lengths[i] > high_n_len and i not in deleted:
                deleted.add(i)

        # Finish one deletion
        n_dels += 1

    return n_dels


if __name__ == "__main__":
    n = int(input().strip())    # Number of test cases
    file_types = []
    name_lengths = []
    for i in range(n):
        ci, ai = input().strip().split() # Read int array
        file_types.append(ci)
        name_lengths.append(int(ai))
    print(solution(n, file_types, name_lengths))