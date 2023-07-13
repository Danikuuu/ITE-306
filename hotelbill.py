
print("COMPUTING HOTEL BILL") #print hotel bill

#Hotel fee
rate_perday = 1500 #rate per day
aircon_fee = 500 # aircon fee
interet = 300 #internet fee
tv = 100 #tv fee
vat = 0.12 #vat

#initializing the fee and input
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -") #print a broken line

print("Rate per day: ", rate_perday) #rate per day
print("Aircon Fee: ", aircon_fee) # aircon fee
print("Interet Fee: ", interet) #internet fee
print("TV Fee: ", tv) #tv fee
print("EVAT: ", vat) #vat

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -") #print a broken line
print("\n") #print new line

#get input to the users
num_days = int(input("Enter the number of days : ")) #get the number of days from user

print("\n") #print new line

#compute for the bill
amount = rate_perday * num_days #get the total amount dependig on the days
total = amount + aircon_fee + interet + tv #total fees
tax = total * vat #getting the tax
bill = total + tax #total bill including the tax

#initialize the updated bill according to the user input
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -") #print a broken line

print("Number Of Days", num_days) #print num of days
print("Total amount for", num_days, " days : ", amount) # amount
print("Additional Fees: ", total) #total fees
print("Tax: ", tax) #total tax

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -") #print a broken line

#final bill
print("Final Bill: ", bill)#final bill