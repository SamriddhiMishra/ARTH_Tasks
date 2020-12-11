import os
import getpass

def color(n):
	os.system('tput setaf {}'.format(n))	

def LVM_partition():
        while True:
                os.system('clear')
                color(3)
                print("\n\t ###### LVM Partition Operations ######\n")
                color(6)
                choice =  input('''\n\tChoose any option to perform specific action-
                Choose 1 - Display all available storage devices attached
                Choose 2 - Display information about Physical Volumes(PVs)
                Choose 3 - Display information about Volume Groups(VGs)
                Choose 4 - Display information about Logical Volumes(LVs)

                Choose 5 - Create Physical Volume(PV)
                Choose 6 - Create Volume Group(VG)
                Choose 7 - Create Logical Volume(LV)

                Choose 8 - Resize Logical Volume(LV)
                Choose 9 - Resize Volume Group(VG)

                Choose 10 - Remove Logical Volume(LV)
                Choose 11 - Remove Volume Group(VG)
                Choose 12 - Remove Physical Volume(PV)

                Choose 13 - Create file and display
                Choose 14 - Display file content
  ''')

                if choice>'9' or choice<'1':
                        color(1)
                        print("Action not supported")
                        color(6)
                        break
                choice = int(choice)
                if choice == 1:
                        color(2)
                        os.system('fdisk -l')
                        color(6)
                elif choice == 2:
                        pv = input('Choose one particular PV (default all): ')
                        color(2)
                        os.system('pvdisplay '+pv)
                        color(6)
                elif choice == 3:
                        vg = input('Choose one particular VG (default all): ')
                        color(2)
                        os.system('vgdisplay '+vg)
                        color(6)
                elif choice == 4:
                        lv = input('Choose one particular LV (default all): ')
                        color(2)
                        os.system('lvdisplay '+lv)
                        color(6)
                elif choice == 5:
                        pv = input("Enter the storage device name you want to convert to PV : ")
                        color(4)
                        os.system('pvcreate '+pv)
                        color(2)
                        print("Created PV!")
                        color(6)
                elif choice == 6:
                        vg = input('Enter the name of VG you want to create : ')
                        pv1 = input('Enter the name of PV1 : ')
                        pv2 = input('Enter the name of PV2 : ')
                        color(4)
                        os.system('vgcreate '+vg+' '+pv1+' '+pv2)
                        color(2)
                        print('Created VG!')
                        color(6)
                elif choice == 7:
                        lv = input('Enter the name of LV you want to create : ')
                        size = input('Enter the size of LV: ')
                        vg = input('Enter name of the VG in which you want to create LV: ')
                        path = input('Enter the path to the folder you want to mount on the LV created: ')
                        color(4)
                        os.system('lvcreate --size {} --name {} {}'.format(size,lv,vg))
                        os.system('mkfs.ext4 /dev/{}/{}'.format(vg,lv))
                        os.system('mkdir {}'.format(path))
                        os.system('mount /dev/{}/{} {}'.format(vg,lv,path))
                        color(2)
                        print('Created LV! Ready to store files. Mounted to folder {}'.format(path))
                        color(6)
                elif choice == 8:
                        c = input("Enter the choice- Reduce/Extend the LV (R/E) :")
                        vg = input('Enter name of the VG in which  LV created: ')
                        lv = input('Enter the name of LV you want to resize: ')
                        if c == 'E':
                                c='extend'
                                s='+'
                                size = input('Enter the size by which you want to extend LV size: ')
                                os.system('lv{} --size {}{} /dev/{}/{}'.format(c,s,size,vg,lv))
                                os.system('resize2fs /dev/{}/{}'.format(vg,lv))
                        else:
                                size = input('Enter the size by which you want to change LV size: ')
                                size2 = input('Enter the final reduced size of LV desired: ')
                                path = input('enter path to folder on which LV was mounted:')
                                c='reduce'
                                s='-'
                                os.system('umount /dev/{}/{}'.format(vg,lv))
                                os.system('e2fsck -f /dev/{}/{}'.format(vg,lv))
                                os.system('resize2fs /dev/{}/{} {}'.format(vg,lv,size2))
                                os.system('lv{} --size {}{} /dev/{}/{}'.format(c,s,size,vg,lv))
                                os.system('mount /dev/{}/{} {}'.format(vg,lv,path))
                        color(2)
                        print('LV resized!')
                        color(6)
                elif choice == 9:
                        c = input("Enter the choice- Reduce/Extend the VG (R/E) :")
                        vg = input('Enter name of the VG you want to resize: ')
                        color(4)
                        if c == 'E':
                                pv = input('Enter name of the PV you want to add to VG: ')
                                os.system('vgextend {} {}'.format(vg,pv))
                        else:
                                pv = input('Enter name of the PV you want to remove from VG: ')
                                os.system('pvmove {}'.format(pv))
                                os.system('vgreduce {} {}'.format(vg,pv))
                        color(2)
                        print('VG resized!')
                        color(6)
                elif choice == 10:
                        path = input('Enter path to LV you want to remove: ')
                        color(2)
                        os.system('umount {}'.format(path))
                        os.system('lvremove {}'.format(path))
                        color(6)
                elif choice == 11:
                        vg = input('Enter name of VG you want to remove: ')
                        color(2)
                        os.system('vgremove {}'.format(vg))
                        color(6)
                elif choice == 12:
                        path = input('Enter path to PV you want to remove: ')
                        color(2)
                        os.system('pvremove {}'.format(path))
                        color(6)
                elif choice == 13:
                        path = input('Enter the path to folder: ')
                        file = input('Enter the filename: ')
                        color(4)
                        os.system('cat > {}/{}'.format(path,file))
                        color(2)
                        print('\nFile Created!')
                        os.system('cat {}/{}'.format(path,file))
                        color(6)
                elif choice == 14:
                        path = input('Enter the path to folder: ')
                        file = input('Enter the filename: ')
                        color(2)
                        os.system('cat {}/{}'.format(path,file))
                        print()
                        color(6)	
                input("Press Enter to continue..")
