import sys
memoized_vals = {}


def get_result(n, b, x, k):
    i = hash(str(n)+str(b)+str(x)+str(k))
    # memoization to fetch the same values
    if i in memoized_vals:
        return memoized_vals[i]
    if n <= 0:
        return 0
    if b < 0:
        return 0
    if x > k:
        return 0
    if b == 0:
        return 1
    memoized_vals[i] = get_result(n, b-1, x+1, k)+get_result(n-1, b, 0, k)
    return memoized_vals[i]


def robot_stack_func(b, n, k):
    return get_result(n, b, 0, k)


if __name__ == "__main__":
    input_file = sys.argv[1]
    with open(input_file) as f:
        input_data = f.readlines()
        for data in input_data:
            # print(data)
            b, n, k = (int(x) for x in data.split())
            print(f"({b},{n},{k}) = ", robot_stack_func(b, n, k))