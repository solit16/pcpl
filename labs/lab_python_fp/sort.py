data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == "__main__":
    result = [abs(x) if x < 0 else x sorted()]
    print(result)

    result_with_lambda = sorted(data, key = lambda x: abs(x), reverse = True)
    print(result_with_lambda)
