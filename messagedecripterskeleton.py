def main():
    useroutput = (" ")
    for i in range (7):

        useroutputbackup = useroutput
        userinput = input("prima lettera")
        if userinput == ("a"):
            useroutput = (useroutputbackup + "d")
            useroutputbackup = useroutput
            print (useroutputbackup)

main()