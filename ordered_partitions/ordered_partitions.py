def f(n):
    answer = set()
    if n % 2 == 1:
        answer.add((n, ))
    for number in range(1, n, 2):
        for partition in f(n - number):
            answer.add((number, ) + partition)
    return answer


for i in range(30):
    print(len(f(i)))