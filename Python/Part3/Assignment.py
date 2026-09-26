# 1.palindrone

# str = input("Enter the word :")         
# i=0
# j=len(str)-1
# ans = True
# while(i<j):
#     if(str[i]!=str[j]):
#         ans = False
#         break
#     i+=1
#     j-=1

# if(ans == True):
#     print("this is palindrom !")
# else:
#     print("this is not palindrom !")



# 2.sum of list

# lis = [1,2,3,4,5,6,7]
# def Elementsum(lis):
#     sum = 0
#     for i in lis:
#         sum+=i

#     return sum

# print(Elementsum(lis))



# 3.merge two list and sort 

# list1 = list(map(int, input("Enter numbers: ").split()))
# list2 = list(map(int, input("Enter numbers: ").split()))

# result = []
# for i in list1:
#     result.append(i)

# for i in list2:
#     result.append(i)

# result.sort()
# print(result)


# 4.
# 6.

# words = ["apple", "banana", "kiwi", "cherry", "mango"]

# dis = {}

# for key in words:
#     newitem = {key:len(key)}
#     dis.update(newitem)

# print(dis)


# 7. count of space
str = input("enter the sentence :")
count = 0
for i in str:
    if(i == " "):
        count+=1

print(count)







