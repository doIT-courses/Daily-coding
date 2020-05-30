# Given a list of numbers arr and a number k, return whether any two numbers from the list arr add up to k
# Дан массив чисел arr и число k - выясните, есть ли в массиве arr 2 числа, сумма которых была бы равна k

k = 15
arr = [10, 15, 3, 7, 1, 9, 13, 2]
n = len(arr)

result = False
result_a, result_b = None, None

# Naive solution: time - O(n^2), space - O(1)
# for i in range(n-1):
#     for j in range(i+1, n):
#         if arr[i] + arr[j] == k:
#             result = True
#             result_a, result_b = arr[i], arr[j]
#             break
#     if result:
#         break

# Better solution: time - O(n*log(n)), space - 
# sorted_arr = sorted(arr)
# left = 0
# right = n-1
# while left < right:
#     a_b_sum = sorted_arr[left] + sorted_arr[right]
#     if a_b_sum < k:
#         left += 1
#     elif a_b_sum > k:
#         right -= 1
#     else:
#         result = True
#         result_a, result_b = sorted_arr[left], sorted_arr[right]
#         break

# Best solution: time - O(n), space - O(n)
s = set() # assume using hash set - contains() - O(1)
for el in arr:
    if k-el in s:
        result = True
        result_a, result_b = k-el, el
        break
    s.add(el)


print(result, result_a, result_b)