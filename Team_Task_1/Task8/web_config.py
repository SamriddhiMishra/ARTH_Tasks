import os

def color(n):
    os.system("tput setaf {}".format(n))

def host():
    file = input("Enter the file name :- ")
    color(3)
    print("#### Enter the content ####")
    print('Press ENTER then Ctrl + D to Stop')
    color(6)
    os.system("cat > /var/www/html/{}.html".format(file))
    color(2)
    print("#### File Created ####")
    color(6)
    return file
    
def web():
    color(3)
    print("\n\t ###### APACHE Webserver Configuration ######\n")
    color(6)
    os.system("yum install net-tools")
    color(3)
    print("#### Note your IP Address ####")
    color(6)
    os.system("ifconfig")
    os.system("yum install httpd")
    file = host()
    os.system("systemctl stop firewalld")
    os.system("systemctl start httpd")
    color(2)
    print("#### Web Server Configured ####")
    print("Enter http://<Your_IP>/{}.html To view your Webpage".format(file))

