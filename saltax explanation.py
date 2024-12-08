'''
title:
example for Employee Salary Tax

input:
eid, ename, sal


logic:
tax10=tax20=tax30=tottax=npay=0

if sal > 1000000:
    tax10=25000
    tax20=100000
    tax30=(sal - 1000000) * 30.0/100
elif sal > 500000:
    tax10=25000
    tax20=(sal - 500000) * 20.0/100
elif sal > 250000:
    tax10=(sal - 250000) * 10.0/100

tottax=tax10 + tax20 + tax30
npay=sal - tottax

print('Tax 10%:', tax10)


'''