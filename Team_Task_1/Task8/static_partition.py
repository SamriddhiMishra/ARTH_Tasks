import os

def color(n):
    os.system("tput setaf {}".format(n))
def static_partition():
    while True:
        os.system("clear")
        color(3)
        print("\n\t ###### Linux Static Partition Operations ######\n")
        color(6)
        choice = input('''\tChoose one of the options :-
        1) See all the attached storage devices
        2) See all the devices and their partitions
        3) Create a partition in storage device
        4) Extend the partition
        5) Shrink the partition
    ''')
        if choice <'1' or choice>'5':
            color(1)
            print("Not supported")
            break
        choice = int(choice)
        if choice == 1:
            os.system("fdisk -l")
        elif choice == 2:
            os.system("df -h")
            os.system("lsblk")
        elif choice == 3:
            color(3)
            hd = input("Enter name of the device :- ")
            folder = input("Enter the folder full path, on which partition will be mounted :- ")
            color(6)
            os.system("fdisk {}".format(hd))
            partno = input("Enter the partion number just created :- ")
            os.system("mkfs.ext4 {}".format(hd+partno))
            os.system("rm -rf {}".format(folder))
            os.system("mkdir {}".format(folder))
            os.system("mount {} {}".format(hd+partno,folder))
            color(2)
            print("#### Created and Mounted the partition to {} ####".format(folder))
        elif choice == 4:
            color(3)
            part = input("Enter name of the partition :- ")
            folder = input("Enter the folder name, on which partition will be mounted again:- ")
            color(6)
            os.system("umount {}".format(part))
            color(3)
            print("\n###### Delete the created partition.. ######")
            color(6)
            os.system("fdisk {}".format(str(part[:-1])))
            color(3)
            print("\n###### Create new partition with extendend size and don't wipe signature.. ######")
            os.system("fdisk {}".format(part[:-1]))
            color(6)
            os.system("e2fsck -f {}".format(part))
            os.system("resize2fs {}".format(part))
            os.system("mount {} {}".format(part,folder))
            color(2)
            print("#### Extended and Mounted the partition to {} ####".format(part[:-1]))
        elif choice == 5:
            color(3)
            part = input("Enter name of the partition :- ")
            folder = input("Enter the folder name, on which partition will be mounted again:- ")
            size = input("Enter final reduced size of partition :- ")
            color(6)
            os.system("umount {}".format(part))
            os.system("e2fsck -f {}".format(part))
            os.system("resize2fs {} {}".format(part,size))
            color(3)
            print("\n###### Delete the created partition.. ######")
            color(6)
            os.system("fdisk {}".format(part[:-1]))
            color(3)
            print("\n###### Create new partition with reduced size and don't wipe signature.. ######")
            color(6)
            os.system("fdisk {}".format(part[:-1]))
            os.system("rm -rf {}".format(folder))
            os.system("mkdir {}".format(folder))
            os.system("mount {} {}".format(part,folder))
            color(2)
            print("#### Reduced and Mounted the partition to {} ####".format(part[:-1]))
        else:
            color(1)
            print("Not Supported")
            break
        input("Press Enter to continue....")
    
    
    
