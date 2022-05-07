#вариант 1
numbers = [1, 2, 3, 4, 5]
print(numbers.pop(1))
print(numbers.pop())
print(numbers)

#вариант 2
numbers_list_1 = [1,2,3,4,5]
numbers_list_2 =[2,5]
for num in numbers_list_1[::-1]:
    if num in numbers_list_2:
        numbers_list_1.remove(num)
print (numbers_list_1)
