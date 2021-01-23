#HEALTH MANAGEMENT SYSTEM
#LOGIN ID IS HMS
#PASSWORD IS HELP

print("****************************************************************")
print("WELCOME TO HEALTH MANAGEMENT PORTAL CREATED BY SRISHTI AND AMBUJ ")
print("****************************************************************")
def submit(k):
    if k==1:
        c=int(input("Enter 1 for Exercise and and Enter 2 for Food\n"))
        if c==1:
            w=input("Enter details\n")
            with open("divyansh.txt","a") as op:
                op.write("EXERCISE SUGGESTED: "+w+"\n")
            print("Excercise submitted")
        elif(c==2):
            w = input("Enter details\n")
            with open("divyansh.txt", "a") as op:
                op.write("FOOD TO BE TAKEN: "+w + "\n")
            print("Food submitted")
    elif k==2:
        c=int(input("Enter 1 for Exercise and and Enter 2 for Food\n"))
        if c==1:
            w=input("Enter details\n")
            with open("Srishti.txt","a") as op:
                op.write("EXERCISE SUGGESTED: "+w+"\n")
            print("Excercise submitted")
        elif(c==2):
            w = input("Enter details\n")
            with open("Srishti.txt", "a") as op:
                op.write("FOOD TO BE TAKEN: "+w + "\n")
            print("Food submitted")
    elif k==3:
        c=int(input("Enter 1 for Exercise and and Enter 2 for Food\n"))
        if c==1:
            w=input("Enter details\n")
            with open("Ambuj.txt","a") as op:
                op.write("EXERCISE SUGGESTED: "+w +"\n")
            print("Excercise submitted")
        elif(c==2):
            w = input("Enter details\n")
            with open("Ambuj.txt", "a") as op:
                op.write("FOOD TO BE TAKEN: "+w + "\n")
            print("Food submitted")
    elif k==4:
        c=int(input("Enter 1 for Exercise and and Enter 2 for Food\n"))
        if c==1:
            w=input("Enter details\n")
            with open("Manish.txt","a") as op:
                op.write("EXERCISE SUGGESTED: "+w +"\n")
            print("Excercise submitted")
        elif(c==2):
            w = input("Enter details\n")
            with open("Manish.txt", "a") as op:
                op.write("FOOD TO BE TAKEN: "+w + "\n")
            print("Food submitted")
    elif k==5:
        c=int(input("Enter 1 for Exercise and and Enter 2 for Food\n"))
        if c==1:
            w=input("Enter details\n")
            with open("Aditya.txt","a") as op:
                op.write("EXERCISE SUGGESTED: "+w +"\n")
            print("Excercise submitted")
        elif(c==2):
            w = input("Enter details\n")
            with open("Aditya.txt", "a") as op:
                op.write("FOOD TO BE TAKEN: "+w + "\n")
            print("Food submitted")
    else:
        print("You Entered Wrong Input")

def readfile(k):
    if k=="HELP":
        c=int(input("Enter\n 1 for Divyansh\n 2 for Srishti\n 3 for Ambuj\n 4 for Manish\n 5 for Aditya\n"))
        if c==1:
            with open("divyansh.txt", "r") as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open("Srishti.txt", "r") as op:
                for i in op:
                    print(i,end="")
        elif c==3:
            with open("Ambuj.txt", "r") as op:
                for i in op:
                    print(i,end="")
        elif c==4:
            with open("Manish.txt", "r") as op:
                for i in op:
                    print(i,end="")
        elif c==5:
            with open("Aditya.txt", "r") as op:
                for i in op:
                    print(i,end="")
    else:
        print("you entered wrong details")

print("Enter your Login ID")
s=input()
print("Enter your Password")
p=input()
if s=="HMS" and p=="HELP":

    q=int(input("Enter 1 for Entering the data and 2 for Viewing the data \n"))
    if q==1:
        t=int(input("Enter\n 1 for Divyansh\n 2 for Srishti\n 3 for Ambuj\n 4 for Manish\n 5 for Aditya\n"))
        submit(t)
    else:
        t = input("Please Re-enter your  Password for Viewing the Data\n")
        readfile(t)

else:
    print("Invalid ID/password ,Try Agian!")
