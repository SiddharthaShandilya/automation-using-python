import os
import Docker_automation as da
import Linux_Automation as la
import Hadoop_Automation as ha
os.system("clear")
os.system("tput setaf 3")

print("\t\t\t\tWelcome welcome welcome\t\t\n\n")

os.system("tput setaf 5")

print("\n\n\t\t\t\tWelcome to my menu program")




# ------------------->> MENU PART <<------------
def menu():
    m = """
Press 1: To create a partition
Press 2: To format the disk
Press 3: To mount the disk
Press 4: To configure yum
Press 5: To configure apache web server
Press 6: To create a Lvm Storage
Press 7: To create a namenode on hadoop
Press 8: To create a datanode on hadoop
Press 9: To create a client on hadoop
press10: To Install Hadoop on the system
press11: To exit from the Menu Program
press12: For configring Docker
"""
    print(m)

    ch = int(input("Input Your Choice: "))
    if ch == 1:
        la.create_partition()

    elif(ch == 2):
        la.format_disk()

    elif(ch == 3):
        la.mount_disk()

    elif(ch == 4):
        la.configure_yum()

    elif(ch == 5):
        la.configure_appache_web_server()

    elif(ch == 6):
        la.create_lvm_storage()

    elif(ch == 7):
        ha.create_namenode_hadoop()

    elif(ch == 8):
        ha.create_datanode_hadoop()

    elif(ch == 9):
        ha.create_hadoop_client()

    elif(ch == 10):
        ha.install_hadoop()

    elif(ch == 11):
        print("\n\t\t EXITING ...\t\t\n")
        exit()
    elif(ch == 12):
        
        da.docker()
    else:
        print("\n\t\tYOU HAVE ENTERED WRONG OPTION \n")

# the program need to re-run everytime a task is completed need to put the tasks in a infinite loop

# need to clear the screen before displaying the message as it looks more tidy


print("Do you want to run? Local/Remote")

ch2 = input("l-local and r-remote: ")

if ch2 == 'l':

    menu()
#  does not work for aws as it requires passkey <<-- needs to be taken care of


elif(ch2 == 'r'):
    imp3 = input("Enter the target's IP: ")

    os.system("scp /root/arth_projects/menu1.py "+imp3+":/root")

    os.system("(echo 'l' ; echo &ch) | ssh "+imp3+" python3 menu1.py")
