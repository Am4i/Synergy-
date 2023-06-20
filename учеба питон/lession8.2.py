N = int(input())
array = list(map(int, input().split()))

new_array = array[-1:] + array[:-1]

print(*new_array)