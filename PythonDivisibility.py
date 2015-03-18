#Author: Rain Erika H. Angelito
#Program that ask for a positive integer to list the divisible numbers less
# than it.
x=input('Input an integer:  ')
i=0
if int(x)>0:
        while i<int(x):
                        i=i+1
                        if(int(x)%i==0 and int(x)!=i):
                                print(str(i))
else:
        print('Please input a positive integer')
