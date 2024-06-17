# CIS_ZachAlderete_lab4
# Date: 6/17/2024
# Description:Program to calculate store and employee bonuses based on monthly store sales
# Store bonus based on monthly sales
# Employee bonus based on sales percent increase

# declare local variables
monthlySales = 0 # monthly sales amount
storeAmount = 0 # store bonus amount
empAmount = 0 # employee bonus amount
salesIncrease = 0 # percent of sales increase
prompt_ms = 'Enter monthly sales $'
prompt_si = 'Enter percent of sales increase:'

# declare prompts 
monthlySales =  float(input(prompt_ms)) # prompt to obtain montly sales amount
salesIncrease = float(input(prompt_si)) #prompt to obtain sales increase amount
salesIncrease = salesIncrease / 100

# calculate store bonus amount
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else: storeAmount = 0

# prompt to determine percent of sales increase
if salesIncrease >= 0.05:
    empAmount = 75
elif salesIncrease >= 0.04:
    empAmount = 50
elif salesIncrease >= 0.03:
    empAmount = 40
else: empAmount = 0    

# This code will print the store bonus and employee bonus amount
print ("The store bonus amount is $", storeAmount)
print ("The employee bonus amount is $", empAmount)

if (storeAmount == 6000 ) and (empAmount == 75):
    print('Congrats! You have reached the highest bonus amounts possible! ')