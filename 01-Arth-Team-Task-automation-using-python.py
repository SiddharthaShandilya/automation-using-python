import os

def option():
    ck = input(" \t Enter 1 to start the docker \n \t Enter 2 to stop the docker \n \t Enter 3 to know the status of docker \n \t  Enter 4 for running an image \n \t  Enter 5 for pulling an image \n \t\n")
    ch = int(ck)
    return ch

def Rechoice():
    reChoice = input("you have exitted from the service Enter R to re-enter")
    if(reChoice == 'R' ):
            service()
    else:
            print("you have choosen to withdraw \n \t\tHAPPY CODING")
           

def service():
        exitStatus = "dumycode"
        while( exitStatus != "N"):
            ch = option()
            if(ch == 1):
                    print("\t \t Starting Docker \t\t\n")
                    os.system("systemctl start docker")
            elif(ch == 2):
                print("stopping docker")
                os.system("systemctl stop docker")
            elif(ch == 3):
                os.system("systemctl status docker")
            elif(ch == 4):

                # ==========>>>>>>> here we will ask the user details about the image it wants to run
                print("you have chosen option 4\n")
                


            elif(ch == 5):
                # ==================>>>>>>>>Here we will ask the user details about the image it wants to pull

                    imgPull = input("Please input the name of the image  ")
                    os.system("docker pull {}".format(imgPull))
            else:
                    print("You have entered wrong choice")
            
            exitStatus = input("Enter y to continue and N  to exit [y/n] \t")
        


def docker():
    print("\t Welcome to dockers below are the list of options to use docker \t!!")
    service()
    Rechoice()

docker()
