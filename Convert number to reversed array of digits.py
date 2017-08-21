'''Convert number to reversed array of digits

Given a random number:

    C#: long;
    C++: unsigned long;

You have to return the digits of this number within an array in reverse order.'''

def digitize(n):
  list=[]
  for i in str(n):
    list += i
    list = [int(i) for i in list]
    return list[::-1]
