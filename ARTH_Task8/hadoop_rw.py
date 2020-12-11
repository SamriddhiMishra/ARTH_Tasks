import os

def color(n):
    os.system("tput setaf {}".format(n))
def hadoop_rw():    
    while True:
        os.system("clear")
        color(3)
        print("\n\t###### Read and Write files on Hadoop Cluster ######\n")
        color(6)
        choice = input('''\tChoose one of the options below :-
        1) List all the files and folders in a directory (default /)
        2) Read a file
        3) Create a folder
        4) Create a new file
        5) Create a new empty file
        6) Remove a file
        7) Remove a folder
    ''')
        if choice > '7' or choice < '1':
            color(1)
            print("Not supported")
            break
        choice = int(choice)
        if choice == 1:
            folder = input("Enter the folder name (default /) :- ")
            color(3)
            os.system("hadoop fs -ls /{}".format(folder))
        elif choice == 2:
            folder = input("Enter the folder name (default /) :- ")
            file = input("Enter the file name with extension :- ")
            color(3)
            if folder == "":
                os.system("hadoop fs -cat /{}".format(file))
            else:
                os.system("hadoop fs -cat /{}/{}".format(folder,file))
        elif choice == 3:
            folder = input("Enter the folder name (default /) :- ")
            color(3)
            os.system("hadoop fs -mkdir /{}".format(folder))
        elif choice == 4:
            folder = input("Enter the folder name (default /) :- ")
            file = input("Enter the file name with extension :- ")
            color(3)
            print("Enter the file content, Press Enter then CTRL+D to stop ")
            color(6)
            os.system("cat > {}".format(file))
            os.system("hadoop fs -put {} /{}/".format(file,folder))
            color(2)
            print("\n#### File Uploaded ####\n")
        elif choice == 5:
            folder = input("Enter the folder name (default /) :- ")
            file = input("Enter the file name with extension :- ")
            color(3)
            if folder == "":
                os.system("hadoop fs -touchz /{}".format(file))
            else:
                os.system("hadoop fs -touchz /{}/{}".format(folder,file))
            color(2)
            print("\n#### File Created ####\n")
        elif choice ==6:
            folder = input("Enter the folder name (default /) :- ")
            file = input("Enter the file name with extension :- ")
            color(3)
            if folder == "":
                os.system("hadoop fs -rm /{}".format(file))
            else:
                os.system("hadoop fs -rm /{}/{}".format(folder,file))
            color(2)
            print("\n#### File Removed ####\n")
        elif choice == 7:
            folder = input("Enter the folder name (default /) :- ")
            color(3)
            os.system("hadoop fs -rmr /{}".format(folder))
            color(2)
            print("\n#### Folder Removed ####\n")
        else:
            print("Not supported")
            color(3)
            print("\n#### Thank You ####")
            break
        input("Press Enter to continue... ")
