import os
import getpass

def color(n):
        os.system('tput setaf {}'.format(n))    

while True:
        os.system('clear')
        color(3)
        print("\n\t\t ###### Docker Opeartions ######\n")
        color(6)
        choice =  input('''\n\tChoose any option to perform specific action-
                Choose 1 - Install and start Docker services
                Choose 2 - Start services permanantly
                Choose 3 - See the Docker services status

                Choose 4 - List all Images
                Choose 5 - List all Containers
                Choose 6 - List all running Containers
                Choose 7 - Pull an image from docker hub
                Choose 8 - Launch a docker container
                Choose 9 - Create a custom docker image
		Choose 10 - Stop a container
                Choose 11 - Start a container

                Choose 12 - Remove an image (or all)
                Choose 13 - Remove a Container (or all)
  ''')
        try:
                choice = int(choice)
        except :
                color(1)
                print("Action not supported")
                color(6)
                break
        if choice == 1:
                color(2)
                dock_yum = '''[docker1]
baseurl = https://download.docker.com/linux/centos/7/x86_64/stable/
gpgcheck=0
'''
                os.system('echo "{}" > /etc/yum.repos.d/dock.repo'.format(dock_yum))
                os.system("yum install docker-ce --nobest")
                os.system("systemctl start docker")
                color(6)
        elif choice == 2:
                color(2)
                os.system('systemctl enable docker')
                color(6)
        elif choice == 3:
                color(2)
                os.system('systemctl status docker')
                color(6)
        elif choice == 4:
                color(2)
                os.system('docker images')
                color(6)
        elif choice == 5:
                color(2)
                os.system('docker ps -a')
                color(6)
        elif choice == 6:
                color(2)
                os.system('docker ps')
                color(6)
        elif choice == 7:
                image = input("Enter the image name : ")
                tag = input('Enter the tag (default latest) : ')
                color(4)
                if tag == "":
                        tag = "latest"
                os.system('docker pull {}:{}'.format(image,tag))
                color(2)
                print('Image Pulling Done!!!')
                color(6)
        elif choice == 8:
                name = input("Give a name to container : ")
                image = input("Enter the image name : ")
                tag = input('Enter the tag (default latest) : ')
                if tag == "":
                        tag = "latest"
                color(4)
                os.system('docker run -dit --name {} {}:{}'.format(name,image,tag))
                color(2)
                print('Launched a container named -> {}'.format(name))
                color(6)
        elif choice == 9:
                name = input("Give the name of container to make it an Image : ")
                image = input("Give name to your image : ")
                tag = input('Enter the tag (default latest) : ')
                if tag == "":
                        tag = "latest"
                color(4)
                os.system('docker commit {} {}:{}'.format(name,image,tag))
                color(2)
                print('Created a custom image named -> {}'.format(name))
                color(6)
        elif choice == 10:
                name = input("Enter name of container you want to Start : ")
                color(4)
                os.system('docker start {}'.format(name))
                color(2)
                print('Started container named -> {}'.format(name))
                color(6)
        elif choice == 11:
                name = input("Enter name of container you want to Stop : ")
                color(4)
                os.system('docker stop {}'.format(name))
                color(2)
                print('Stopped container named -> {}'.format(name))
                color(6)
        elif choice == 12:
                image = input("Give name of image you want to remove (Enter all to remove all images): ")
                if image == "all":
                        color(4)
                        os.system('docker rmi `docker images -a -q`')
                        color(2)
                        print('Removed all images')
                else:
                        tag = input('Enter the tag (default latest) : ')
                        if tag == "":
                                tag = "latest"
                        color(4)
                        os.system('docker rmi {}:{}'.format(image,tag))
                        color(2)
                        print('Removed image named -> {}'.format(image))
                color(6)
        elif choice == 13:
                name = input("Give the name of the container you want to remove (Enter all to remove all containers): ")
                if name == "all":
                        color(4)
                        os.system('docker rm `docker ps -a -q`')
                        color(2)
                        print('Removed all containers')
                else:
                        color(4)
                        os.system('docker rm {}'.format(name))
                        color(2)
                        print('Removed container named -> {}'.format(name))
                        color(6)
        input("Press Enter to continue ....")
