from aws import aws
from hadoop_config import hadoop_config
from hadoop_rw import hadoop_rw
from static_partition import static_partition
from LVM_partition import LVM_partition
from ML_model import model
from docker_auto import docker,configuredocker,configureyum
from web_config import web,host
import os
import getpass

def color(n):
    os.system("tput setaf {}".format(n))
    
color(3)
pwd = getpass.getpass('\nPlease enter the password to access menu:- ')
if pwd != '':
    color(1)
    print("Wrong Password! Can't proceed ahead.")
    color(6)
    exit()
    
color(6)
while True:
    os.system("clear")
    color(3)
    print("\n\t    ####### Welcome to our Python Automation Main Menu #######")
    print("\t##################################################################\n") 
    color(6)
    choice = input('''\tChoose one of the options :- 
        1) Press 1 for Hadoop Configuration :
        2) Press 2 for Data Upload and Read from cluster FileSystem :
        3) Press 3 for Linux Partition Static :
        4) Press 4 for LVM Partitions :
        5) Press 5 for Linear Regression Model able to predict : 
        6) Press 6 for Configure webserver : 
        7) Press 7 for Creating webpages that auto host on webserver(But webserver must be configured) :
        8) Press 8 for AWS CLI : 
	9) Press 9 for Docker :
  ''')
    if choice <'1' or choice > '9':
        color(1)
        print("Not Supported")
        break
    choice = int(choice)
    if choice == 1:
        hadoop_config()
    elif choice == 2:
        hadoop_rw()
    elif choice == 3:
        static_partition()
    elif choice == 4:
        LVM_partition()
    elif choice == 5:
        model()
    elif choice == 7:
        host()
    elif choice == 6:
        web()
    elif choice == 8:
        aws()
    elif choice == 9:
        docker()
		
    color(2)    
    input("Press Enter to continue...")    

