numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_num_count = 0;

for num in numbers:
    print(num)
    if num > 0:
        positive_num_count +=1
        
print("Positive Number in numbers: ",positive_num_count)
