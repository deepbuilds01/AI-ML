# salary= int(input("Entere your salary :")) 

# if(salary<30000):
#     finaltax = salary * 5 / 100
#     print(finaltax)
# elif(salary>=30000 and salary<=70000):
#     finaltax = salary * 15 / 100
#     print(finaltax)
# else:
#     finaltax = salary * 25 / 100
#     print(finaltax)




# 2. Write a function that takes two integers and and prints all even
#numbers between them 

# a = int(input("Enter num :"))
# b = int(input("Enter num :"))

# for i in range(a,b):
#     if (i%2==0):
#         print(i)




# 3. 
# n = int(input("Enter the number :"))
# def digits(n):
#     while(n!=0):
#         ans = n%10
#         print(ans)
#         n = int(n/10)

# digits(n)



# .Q4 Write a function to return the the number of digits in a number, n.

# n = int(input("Enter the num :"))
# def element(n):
#     count = 0
#     while(n!=0):
#         n = n//10
#         count += 1

#     print(count)

# element(n)


# 05

# n = int(input("enter the num :"))
# def digit(n):
#     sum = 0
#     while n!=0 :
#         sum += n%10
#         n = n//10
#     return sum

# print(digit(n))




# Prime or not

n = int(input("Enter the num :"))
def isprime(n):
    count = 0
    for i in range(1,n+1):
        if(n % i == 0 ):
            count+=1

    if(count == 2):
        print("true")
    else:
        print("false")

isprime(n)