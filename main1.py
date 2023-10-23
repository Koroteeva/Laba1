numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
sub_list = numbers [:4] + numbers [5:]
x = sum(sub_list) / len(numbers)
numbers[4] = x
print(f"Измененный список: {numbers}")