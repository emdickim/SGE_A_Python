nums = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]
sumaTotalImparells = 0
sumaTotalParells = 0
for num in nums:
    if num % 2 == 0:
        
        sumaTotalParells = sumaTotalParells + num
    else:
        
        sumaTotalImparells = sumaTotalImparells + num

print(f"Imparell: {sumaTotalImparells}")
print(f"Parell: {sumaTotalParells}")
        

