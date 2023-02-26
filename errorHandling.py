# error handling 
# try: 
#     x = int(input("x : "))
#     y = int(input("y : "))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as e :
#     print(' Yanlis deger girdiniz!!!  ')
#     print(e)

# try: 
#     x = int(input("x : "))
#     y = int(input("y : "))
#     print(x/y)
# except:
#     print(' Yanlis deger girdiniz!!!  ')

while True:

    try: 
        x = int(input("x : "))
        y = int(input("y : "))
        print(x/y)
    except Exception as e :
        print(' Yanlis deger girdiniz!!!  ')
        print(e)
    else:
        break
    finally: 
        print('try except sonlandi. ')   




