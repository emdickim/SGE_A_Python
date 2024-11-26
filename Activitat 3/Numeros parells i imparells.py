nums = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]
parells = []
imparells = []
for num in nums:
    if num % 2 == 0:
        parells.append(num)
    else:
        imparells.append(num)
print(f"Parell: {parells}")
print(f"Imparell: {imparells}")