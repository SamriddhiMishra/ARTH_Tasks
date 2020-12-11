#! /usr/bin/python3

print("content-type: text/html")
print()

print('''<style>
pre{
  color: #02aab0;
  font-weight: bold;
  font-size: 20px;
}
span{
  color: #8ac69e;
  font-weight: bold;
  font-size: 26px;
}
</style>
''')


print('<body style="padding: 40px;">')
print('<h1 style="color: #8ac69e;" >Output</h1>')

import cgi
import subprocess as sp

fs = cgi.FieldStorage()

#---
choice = fs.getvalue("choice")
#---
pull_image = fs.getvalue("pull_image")
pull_tag = fs.getvalue("pull_tag")
#---
launch_name = fs.getvalue("launch_name")
launch_image = fs.getvalue("launch_image")
launch_tag = fs.getvalue("launch_tag")
#---
create_img_name = fs.getvalue("create_img_name")
create_img_image = fs.getvalue("create_img_image")
create_img_tag = fs.getvalue("create_img_tag")
#---
stop_name = fs.getvalue("stop_name")
#---
start_name = fs.getvalue("start_name")
#---
remove_image = fs.getvalue("remove_image")
remove_tag = fs.getvalue("remove_tag")
#---
remove_name = fs.getvalue("remove_name")
#---

choice = int(choice)

if choice == 1:
        dock_yum = '''[docker1]
baseurl = https://download.docker.com/linux/centos/7/x86_64/stable/
gpgcheck=0
'''
        output = sp.getoutput("sudo setenforce 0")
        output = sp.getoutput("sudo touch dock.repo")
        output = sp.getoutput("sudo chown apache dock.repo") 
        output = sp.getoutput("sudo chmod +rwx dock.repo")
        f = open("dock.repo","w")
        f.write(dock_yum)
        f.close()        
        output = sp.getoutput("sudo cp dock.repo /etc/yum.repos.d/dock.repo")
        output = sp.getoutput("sudo yum install docker-ce --nobest -y")
        output = sp.getoutput("sudo systemctl start docker")
        print("<span><br>#### Started Docker Services ####</span><br>")
        print("<pre>{}</pre>".format(output))
elif choice == 2:
        output = sp.getoutput('sudo systemctl enable docker')
        print("<span><br>#### Made services permanent ####</span><br>")
        print("<pre>{}</pre>".format(output))
elif choice == 3:
        output = sp.getoutput('sudo systemctl status docker')
        print("<span><br>#### Docker Services Status ####</span><br>")
        print("<pre>{}</pre>".format(output))
elif choice == 4:
        output = sp.getoutput('sudo docker images')
        print("<span><br>#### Docker Images Available ####</span><br>")
        print("<pre>{}</pre>".format(output))
elif choice == 5:
        output = sp.getoutput('sudo docker ps -a')
        print("<span><br>#### All Containers ####</span><br>")
        print("<pre>{}</pre>".format(output))
elif choice == 6:
        output = sp.getoutput('sudo docker ps')
        print("<span><br>#### All Running Containers ####</span><br>")
        print("<pre>{}</pre>".format(output))
elif choice == 7:
        if pull_tag == None:
                pull_tag = "latest"
        output = sp.getoutput('sudo docker pull {}:{}'.format(pull_image,pull_tag))
        print("<span><br>#### Image Pulling Done!!! ####</span><br>")
        print("<pre>{}</pre>".format(output))
elif choice == 8:
        if launch_tag == None:
                launch_tag = "latest"
        output = sp.getoutput('sudo docker run -dit --name {} {}:{}'.format(launch_name,launch_image,launch_tag))
        print("<span><br>#### Launched a container named -> {} ####</span><br>".format(launch_name))
        print("<pre>{}</pre>".format(output))
elif choice == 9:
        if create_img_tag == None:
                create_img_tag = "latest"
        output = sp.getoutput('sudo docker commit {} {}:{}'.format(create_img_name,create_img_image,create_img_tag))
        print("<span><br>#### Created a custom image named -> {} ####</span><br>".format(create_img_name))
        print("<pre>{}</pre>".format(output))
elif choice == 10:
        output = sp.getoutput('sudo docker start {}'.format(start_name))
        print('<span><br>#### Started container named -> {} ####</span><br>'.format(start_name))
elif choice == 11:
        output = sp.getoutput('sudo docker stop {}'.format(stop_name))
        print('<span><br>#### Stopped container named -> {} ####</span><br>'.format(stop_name))
elif choice == 12:
        if remove_image == "all":
                output = sp.getoutput('sudo docker rmi `docker images -a -q`')
                print("<span><br>#### Removed all images!!! ####</span><br>")
        else:
                if remove_tag == None:
                        remove_tag = "latest"
                output = sp.getoutput('sudo docker rmi {}:{}'.format(remove_image,remove_tag))
                print('<span><br>#### Removed image named -> {} ####</span><br>'.format(remove_image))
elif choice == 13:
        if remove_name == "all":
                output = sp.getoutput('sudo docker rm `docker ps -a -q`')
                print("<span><br>#### Removed all containers!!! ####</span><br>")
        else:
                output = sp.getoutput('sudo docker rm {}'.format(remove_name))
                print('<span><br>#### Removed container named -> {} ####</span><br>'.format(remove_name))
