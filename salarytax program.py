print('Enter following inputs for find employee salary tax\n')
eid=int(input("ID:"))
sal=float(input("Salary:"))

tax10=tax20=tax30=tottax=npay=0

if sal>1000000:
    tax10=25000
    tax20=100000
    tax30=(sal-1000000)*30.0/100
elif sal>500000:
    tax10=25000
    tax20=(sal-500000)*20.0/100
elif sal>250000:
    tax10=(sal-250000)*10.0/100
    
tottax=tax10+tax20+tax30
npay=sal-tottax

if tax10>0:
    print('\nTax 10%%: %.02f'%(tax10))

if tax20>0:
    print('\nTax 20%%: %.02f'%(tax20))

if tax30>0:
    print('\nTax 30%%: %.02f'%(tax30))
    
print()#make a new line

if tottax>0:
    print('Total tax amount:%.02f'%(tottax))
    
print('Net pay:%.02f'%(npay))

'''
outputs:

input-1:
Enter following inputs for find employee salary tax

ID:1001
Salary:200000

Net pay:200000.00

input-2:
Enter following inputs for find employee salary tax

ID:1002
Salary:400000

Tax 10%: 15000.00

Total tax amount:15000.00
Net pay:385000.00


input-3:
Enter following inputs for find employee salary tax

ID:1003
Salary:800000

Tax 10%: 25000.00

Tax 20%: 60000.00

Total tax amount:85000.00
Net pay:715000.00

input-4:
Enter following inputs for find employee salary tax

ID:1004
Salary:1600000

Tax 10%: 25000.00

Tax 20%: 100000.00

Tax 30%: 180000.00

Total tax amount:305000.00
Net pay:1295000.00
'''