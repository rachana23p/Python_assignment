#Implement a program to create a list with two tuple of fruits and vegetables. Access fruits separately and vegetables separately. 
List = [('papaya','mango','apple'),('brinjal','carrot','raddish')]
FrV=input("enter whether fruits or vegetables");
if(FrV=='fruits'):
    print("fruits", List[0])
elif(FrV=='vegetables'):
    print("vegetables", List[1])
else:
    print("enter as 'fruits' or 'vegetables'.")


