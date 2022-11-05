# Working on a solution for Mathematics Magazine Problem #2154
#
# Given user input n, prints out the number of ordered partitions of n with only odd parts with
# m terms from 1 to n.
# So since 5 can be written as 5, 1+1+3, 1+3+1, 3+1+1, or 1+1+1+1+ 1, the 5 row will print 
# out 1 0 3 0 5. This is because five has 1 single integer partition, 0 two integer partitions, 3 three
# integer partitions, 4 four integer partitions, and 1 five integer partition.

def f(n):
    answer = set()
    if n % 2 == 1:
        answer.add((n, ))
    for number in range(1, n, 2):
        for partition in f(n - number):
            answer.add((number, ) + partition)
    return answer


num = int(input("Enter number of elements to compute:"));

for i in range(1,num):
    pyramid = [0] * num
    for perm in f(i):
        index = len(perm)
        pyramid[index] = pyramid[index] + 1; 
    for j in (range(1,num)):
        print('{:>5}'.format(pyramid[j]), end =" ");
    print('\n');
