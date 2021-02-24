
#averages.py

#create an empty list where user inputted value will be added into 
tol = []
while True:
    num = int(input('Enter an integer: '))
    if num >= 0:
        tol.append(num)
    else: 
        break
        
#calculate the length, sum and average of list         
val = len(tol)
sum_val = sum(tol)
avg = sum_val / val

print(f'{val} values entered with a sum of {sum_val} and average of {avg}')