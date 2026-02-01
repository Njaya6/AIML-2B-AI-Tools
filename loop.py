# display even numbers from 0 to n
n= int(input("enter range: "))
for i in range(0,n):
    if i%2 =0 : print(i, end=" ")

# Break function
 my_list= [56, 5 8 ,90, 7 ,48]
 x=56
 for i in my_list:
    if i =x :
        print("Number found at index ",i)
        break():
    else :
      print("Number not found!")

# continue function
  for i in my_list:
    if my_list[i]> my_list[i+1] :
        continue():
    print(my_list[i] end= "\t") 

# A program in pythoh to check palindrome
y = int (input("enter a number: "))
rev=0
temp=y
while y>0 :
    rem = y % 10
    rev = rev*10 + rem
    y=int(y/10)
y=temp    
if rev ==y :
    print("f{y} is palindrome")
else : print("f{y} is not paliindrome")
       

   
