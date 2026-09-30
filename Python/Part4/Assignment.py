# class Bank_Account:
#     def __init__(self, Owner_name, Acc_number, Balance):
#         self.Owner_name = Owner_name
#         self.Acc_number = Acc_number
#         self.Balance = Balance
#         # print("hello guess")


#     #  Deposit
#     def get_deposit(self, addAmount):
#         self.Balance += addAmount


#     # withdraw
#     def get_withdraw(self, withdraw_amount):
#         if self.Balance < withdraw_amount:
#             print("Inseficiant amount!")
#         else:
#             self.Balance -= withdraw_amount



#     def get_info(self):
#         print(f"Account Owner name : {self.Owner_name} ,\nAccount number : {self.Acc_number} ans \nAccount balance is : {self.Balance}")


# csm1 = Bank_Account("DEEP KUMAR", "123ABC", 10000)
# # csm1.get_info()

# csm1.get_deposit(100)
# # csm1.get_info()

# # csm1.get_withdraw(12221)

# print(csm1.Balance)



    




# class Book: 
    # def __init__(self, title, author_name):
    #     self.title = title
    #     self.author_name = author_name
    #     self.review = []


    # def add_review(self, new_review):
    #     self.review.append(new_review)
    

    # def display_review(self):
    #     for i in self.review:
    #         print(i)

    # def get_info(self):
    #     print(f"Book name is : {self.title}, auther name is : {self.author_name} and review is : {self.review}")

# b1 = Book("Doglapn", "Aswnir grover")
# # b1.get_info()

# b1.add_review(" very best")
# b1.add_review("  best")
# b1.add_review(" very best")
# b1.add_review(" excilant")
# b1.add_review(" v,excilant")
# b1.add_review(" very best")

# b1.display_review()






# 
class Student:
    def __init__ (self, name , roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    def get_name(self):
        return self.__name

    def set_name(self, newname):
        self.__name = newname

    def get_rollno(self):
        return self.__roll_no

    def set_rollno(self, newrollnumber):
        self.__roll_no = newrollnumber
        

    def get_marks(self):
        return self.__marks

    def set_marks(self, newmarks):
        if newmarks >= 0 and newmarks <= 100:
            self.__marks = newmarks
        else:
            print("Invalid marks!")


st1 = Student("DEEP KUMAR" , 123, 98)

# print(st1.get_name())
st1.set_name("DEEP KUMAR GUPTA")
# print(st1.get_name())

# print(st1.get_rollno())
st1.set_rollno(123456)
# print(st1.get_rollno())

print(st1.get_marks())
st1.set_marks(2345)
print(st1.get_marks())



