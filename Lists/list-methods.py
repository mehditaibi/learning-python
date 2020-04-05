first_list = [1, 2, 3, 4]
second_list = [1, 2, 3, 4]

first_list.append(5)  # [1, 2, 3, 4, 5]

first_list.extend([6, 7, 8, 9])  # [1, 2, 3, 4, 5, 6, 7 , 8, 9]

first_list.insert(10, 10)  # [1, 2, 3, 4, 5, 6, 7 , 8, 9, 10]
first_list.insert(0, 0)  # [0, 1, 2, 3, 4, 5, 6, 7 , 8, 9, 10]

second_list.pop()  # 4
second_list.pop(1)  # 2
second_list.remove(1)
# [3], if try to remove something not present we are getting an error

second_list.clear()  # []

third_list = [1, 2, 3, 4, 5]

third_list.index(2)  # 1
third_list.index(4)  # 3
third_list.index(2, 0, 4)  # can specify start & end as 2nd and 3rd param

duplicates = [1, 1, 1, 1]
duplicates.count(1)  # 4

ordered = [1, 2, 3, 4]
ordered.reverse()  # [4, 3, 2, 1]

unsorted = [2, 1, 4, 3, 5]
sorted_list = unsorted.sort()  # [1, 2, 3, 4, 5]

words = ["hello", 'there']
' '.join(words) # "hello there"