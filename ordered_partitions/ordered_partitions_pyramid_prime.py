#Working on a solution for Mathematics Magazine Problem #2154

def f(n):
    answer = set()
    if n % 2 == 1:
        answer.add((n, ))
    for number in range(1, n, 2):
        for partition in f(n - number):
            answer.add((number, ) + partition)
    return answer

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True


num = int(input("Enter number of elements to compute:"));


for i in range(1,num):
    pyramid = [0] * num
    for perm in f(i):
        index = len(perm)
        pyramid[index] = pyramid[index] + 1; 
    for j in (range(1,num)):
        if (is_prime(pyramid[j]) and pyramid[j] != 0):
            print('{:>5}]'.format(pyramid[j]), end =" ");
        else:
            print('{:>5} '.format(pyramid[j]), end =" ");
    print('\n');
