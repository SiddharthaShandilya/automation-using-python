import os

def service(ch):
        while( exitStatus != "y"):
            ck = input(" \t Enter 1 to start the docker \n\t
                Enter 2 to stop the docker \n\t
                Enter 3 to know the status of docker \n\t
                Enter 4 for running an image \n\t Enter 5 for pulling an image \n \t
                Enter 99 to exit \n")
            ch = int(ck)
            if(ch == 1):
                    os.system("systemctl start docker")
            elif(ch == 2):
                
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
            
            exitStatus = input("Do you want to continue [y/n] \t")
        
        
            
            

def option():
    ck = input(" \t Enter 1 to start the docker \n \t Enter 2 to stop the docker \n \t Enter 3 to know the status of docker \n \t  Enter 4 for running an image \n \t  Enter 5 for pulling an image \n \t Enter 99 to exit \n")
    ch = int(ck)
    return ch
def Rechoice():
    reChoice = input("you have exitted from the service Enter R to re-enter")
    if(reChoice == 'R' ):
            service(option())
    else:
            print("HAPPY CODING")
            exit()
            
print("\t Welcome to dockers below are the list of options to use docker \t!!")


service(option())
Rechoice()


