# x = 10 
# if(x > 5 ):
#     raise Exception("x 5 den buyuk deger alamaz. ")


# def check_password(psw):
#     import re
#     if len(psw)<8:
#         raise Exception("Parola en az 7 karakter olmalidir.")
#     elif not re.search("[a-z]",psw):
#         raise Exception("Parola kucuk harf icermelidir.")
#     elif not re.search("[a-z]",psw):
#         raise Exception("Parola buyuk harf icermelidir.")
#     elif not re.search("[0-9]",psw):
#         raise Exception("Parola rakam icermelidir.")
#     elif not re.search("[_@$]",psw):
#         raise Exception("Parola alpha numeric karakter icermelidir.")
#     elif re.search("\s",psw):
#         raise Exception("parola bosluk icermemelidir.")

# password = "123456aA#@ "

# try:
#     check_password(password)
# except Exception as ex : 
#     print(ex)
# else:
#     print("Gecerli parola. ")
# finally:
#     print("validation  tamamlandi.")

class Person():
    def __init__(self,name,year):
        if len(name) > 10 : 
            raise Exception("Name alani fazla karakter iceriyor ")
        else : 
            self.name = name
