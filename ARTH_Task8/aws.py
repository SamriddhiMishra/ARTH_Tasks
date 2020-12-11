import os
def color(n):
        os.system("tput setaf {}".format(n))
def aws():
    color(6)    
    os.system('aws configure')

    while True:
        os.system("clear")
        color(6)
        choice = input('''Choose one of the options below :-
        1) Create a key pair
        2) Create security group
        3) Add inbound rules to security group
        4) Launch an instance
        5) Create an EBS Volume and
        6) Attach EBS Volume to as Instance
     ''')

        if choice > '6' or choice < '1':
            color(1)
            print("not supported")
            break
        choice = int(choice)
        if choice == 1:
            color(3)
            kname = input("Enter the key name :-")
            color(6)
            os.system("aws ec2 create-key-pair --key-name {}".format(kname))
            color(2)
            print("#### Created Key-Pair ####")
        elif choice == 2:
            color(3)
            sgname = input("Enter the Security Group name :-")
            descp = input("Enter Security Group description :-")
            color(6)
            os.system('aws ec2 create-security-group --group-name {} --description "{}"'.format(sgname,descp))
            color(2)
            print("#### Create Security Group ####")
        elif choice == 3:
            color(3)
            sgname = input("Enter the Security Group name :-")
            protocol = input("Enter the Protocol :-")
            port = input("Enter the Port No :-")
            ip = input("Enter the IP address you want to allow :-")
            color(6)
            os.system("aws ec2 authorize-security-group-ingress --group-name {} --protocol {} --port {} --cidr {}/0".format(sgname,protocol,port,ip))
            color(2)
            print("#### Added rules to SG ####")
        elif choice == 4:
            color(3)
            c = int(input('''\nSelect one of the free tier Image Ids for the instance launch :-
            1) Amazon Linux 2 AMI (HVM), SSD Volume
            2) Red Hat Enterprise Linux 8 (HVM), SSD Volume
            3) Ubuntu Server 20.04 LTS (HVM), SSD Volume
            4) Microsoft Windows Server 2019 Base
            5) Give Your Image ID\n
     '''))
            if c == 1:
                ami = 'ami-03657b56516ab7912'
            elif c == 2:
                ami = 'ami-0a54aef4ef3b5f881'
            elif c == 3:
                ami = 'ami-07efac79022b86107'
            elif c == 4:
                ami = 'ami-0354df7841220296c'
            else:
                ami = c
            osname = input("Give name to the Instance :- ")
            az = input("Enter the AZ :- ")
            itype = input("Enter the Instance Type (default t2.micro):- ")
            kname = input("Enter the key name :- ")
            sgname = input("Enter the Security Group name :- ")
            color(6)
            if itype == "":
                itype = "t2.micro"
            az = "--placement " + '"AvailabilityZone='+ az + '"'
            name = "--tag-specifications " + '"ResourceType = instance , Tags = [{Key=\"Name\",Value=\"' + osname+'"}]"'
            os.system("aws ec2 run-instances --image-id {0} --instance-type {1} --key-name {2} --security-group-ids {3} {4} {5}".format(ami,itype,kname,sgname,name,az))
            color(2)
            print("#### Launched Instance ####")
        elif choice == 5:
            color(3)
            az = input("Enter AZ name to locate new EBS Volume :- ")
            size = input("Enter the size in GB :-")
            color(6)
            os.system('aws ec2 create-volume --availability-zone "{}" --size {}'.format(az,size))
            color(2)
            print("#### Created EBS Volume in AZ -{} ####".format(az))
        elif choice == 6:
            color(3)
            vid = input("Enter the Volume Id of EBS volume :- ")
            iid = input("Enter the Instance ID you want EBS to get attached :- ")
            name = input("Enter name to give to EBS Volume on attachment :- ")
            color(6)
            os.system("aws ec2 attach-volume --instance-id {} --volume-id {} --device {}".format(iid,vid,name))
            color(2)
            print("#### Attached EBS Volume - {} ####".format(name))
        input("Press Enter to continue....")
    
