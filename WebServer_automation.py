import os


def startWebServer():
    print("\n\n\t\t ---->>\tSTARTING YOUR APACHE WEB SERVER\t<----\t\t\n\n")
    os.system("systemctl start httpd")
    print("\n\n\t\t ---->>\tWEB SERVER STATUS\t<----\t\t\n\n")
    print("\n\tEnter ---> :q or [ ctrl+c ]<----  to exit\n\n")
    os.system("systemctl status httpd")
    os.system("systemctl stop firewalld")
    return


def hostWebSite():
    print("HERE WE WILL HOST WEB SITE")
    return


def configureApi():
    print("HERE WE WILL HOST API")
    return


def menu():
    os.system("clear")
    webInstalled = input(
        "\n\n\nDo you have apache web server installed [y/n] : ")

    if(webInstalled == 'y'):
        startWebServer()
        reEnter = 'y'
        while(reEnter == 'y'):
            ch = input(
                "\n\n\t\tENTER 1 TO HOST A FILE\nENTER 2 TO CONFIGURE AN API")
            if(ch == 1):
                hostWebSite()

            elif(ch == 2):
                configureApi()

            else:
                print("\n\tYOU HAVE ENTERED WRONG CHOICE\n")
            reEnter = input("\n\tDO YOU WANT TO CONTINUE [y/n] : ")

    else:
        print("\n\n\t\t ---->>\tINSTALLING APACHE SERVER\t<----\t\t\n\n")
        os.system("dnf install httpd")
        print("\n\n\t\t ---->>\tAPACHE WEB SERVER INSTALLED\t<----\t\t\n\n")
        startWebServer()
