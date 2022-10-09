print('Mode\t\tDiscount\n1.Credit Card\t10% of discount\n2.Debit Card\t5% of discount\n3.Net Banking\t2% of discount\n4.Otherwise\t0% of discount')
a=int(input('Enter the bill amount:'))
b=int(input('Enter mode of payment: '))
if b==1:
    discount=(a*10)/100
elif b==2:
    discount=(a*5)/100
elif b==3:
    discount=(a*2)/100
else:
    discount=0
print(f'Discount amount is {discount}\nNet Payable Amount is {a-discount}')
