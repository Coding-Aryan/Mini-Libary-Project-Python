#Authors: Python Aryan
import time
class Libary():

    def displaybook(self):
        with open("books.txt") as op:
            for i in op:
                print(i, end="")
        return "Hope you like them !!, If you want to lend a book from our libary so you can run the program to do so !!"

    def lend(self):
        print("If You want to lend a book from our libary so kindly mention your name and book's name which you want to lend And hit y for yes and n for no")
        yn = input()
        if yn=="y":
            print("Pls Enter Your Name:")
            lendn = input()
            f = open("Info.txt", "r+")
            f.read()
            f.write("\nName of the person: ")
            f.write(lendn)
            print("Pls Enter Book's Name:")
            lendb = input()
            f = open("Info.txt", "r+")
            f.read()
            f.write("\nName of the book: ")
            f.write(lendb)

            localtime = time.asctime(time.localtime(time.time()))
            f = open("Info.txt", "r+")
            f.read()
            f.write("\nThe time at which the book was lend from the libary: \n")
            f.write(localtime)
            f.close()
            return (f"Your Name is {lendn} And the Book you have lend from us Is {lendb}")

        else:
            return ("Ok")


    def addbook(self):
        print("If Your wish is is to add a book to our libary then first a fall we would like to Thank you for your contribution\n" \
              "Please Mention Your name:")
        addn = input()
        print("Please Mention Your Book's name:")
        addb = input()
        print(f"Confirmation Your Name is {addn} And the Book Name Is {addb}\n"
         f"If You want to proceed further then press y to confirm the order and n for cancelling it.")
        yorn = input()
        if yorn=="y":
            print("Your Info and book is saved to our libary\n")
            f = open("Bookadd.txt", "r+")
            f.read()
            f.write(f"\nRecently A Book Was Added to our libary. Name Of Book Is *{addb}*, And Name of the person who had added the book is {addn}")
            localtime = time.asctime(time.localtime(time.time()))
            f.write("\nThe time at which the book was lend from the libary: \n")
            f.write(localtime)

            return "Thank You !!"

        else:
           return ("Your Order was Cancelled !!")




    def retbook(self):
        print("Hope you have enjoyed reading our book, And you have come here to return them so we request you to mention you name and the book's name")
        print("Please Mention Your name:")
        rnam = input()
        print("Please Mention Your Book's name:")
        rbok = input()
        print(f"Confirmation Your Name is {rnam} And the Book Name Is {rbok}")
        print("Press y to confirm the return or Press n to cancel")
        yorc = input()

        if yorc=="y":
            print("Your Info and book is saved to our libary\n")
            f = open("bookret.txt", "r+")
            f.read()
            f.write(f"\nRecently A Book Was Returned to our libary. Name Of Book Is *{rbok}*, And Name of the person who had returned the book is {rnam}")

            localtime = time.asctime(time.localtime(time.time()))
            f.write("\nThe time at which the book was returned to the libary: \n")
            f.write(localtime)
            return "Thank You !!"

        else:
            return ("Your Return was Cancelled !!")


    def finduser(self):
        print("Please Enter the Name of the book:")
        d1 = {"Harry Potter and the Sorcerer's Stone":"Aryan", "Harry Potter and the Chamber of Secrets":"Sarvesh",
        "Harry Potter and the Prisoner of Azkaban":"Vedant",
        "Harry Potter and the Goblet of Fire":"Vidhan",
        "Harry Potter and the Order of the Phoenix":"Yash",
        "Harry Potter and the Half-Blood Prince":"Awadh",
        "Harry Potter and the Deathly Hallows":"Ashwad"}
        xyz = input()
        return (d1[xyz])



var = Libary()
print(var.finduser())
