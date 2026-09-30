#++++++++ Perform read opration on file ++++++++#

# f = open("Python/Part5/Sample.txt", "r")

# data = f.read()
# print(data)
# print(type(data))

# f.close()



#++++++++ Perform write opration on file ++++++++#

# f = open("Python/Part5/Sample.txt", "w")
# f.write("Hello World!")

# f.close()



#++++++++ Add new contend at the end +++++++#

# f = open("Python/Part5/Sample.txt", "a")
# f.write("\nNew content")

# f.close()



#++++++++++ Create a new file ++++++++#

# f = open("Python/Part5/Sample2.txt", "x")
# f.write(" I am creating a new file!")

# f.close()



#++++++++ '+' ++++++++#

#  r+

f = open("Python/Part5/Sample.txt", "r+")

f.write("Hello")
print(f.read())

f.close()





