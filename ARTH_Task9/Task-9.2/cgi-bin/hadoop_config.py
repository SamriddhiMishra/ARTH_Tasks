#! /usr/bin/python3

print("content-type: text/html")
print()

print('''<style>
pre{
  color: #ffb78c;
  font-weight: bold;
  font-size: 20px;
}
span{
  color: #ffb78c;
  font-weight: bold;
  font-size: 26px;
}
</style>
''')


print('<body style="padding: 40px;">')
print('<h1 style="color: #71daeb;" >Output</h1>')


import cgi
import subprocess as sp
import webbrowser

fs = cgi.FieldStorage()

#---
choice = fs.getvalue("choice")
#---
node = fs.getvalue("node")
#---
ip_master = fs.getvalue("ip_master")
#---
action = fs.getvalue("action")
#---
list_folder = fs.getvalue("list_folder")
#---
read_folder = fs.getvalue("read_folder")
read_file = fs.getvalue("read_file")
#---
create_folder = fs.getvalue("create_folder")
#---
file_folder = fs.getvalue("file_folder")
create_file = fs.getvalue("create_file")
file_text = fs.getvalue("file_text")
#---
file_folder_emp = fs.getvalue("file_folder_emp")
create_file_emp = fs.getvalue("create_file_emp")
#---
remove_file_folder = fs.getvalue("remove_file_folder")
remove_file = fs.getvalue("remove_file")
#---
remove_folder = fs.getvalue("remove_folder")
#---

if choice == "1":
        output = sp.getoutput("sudo rm -rf /etc/hadoop")
        output = sp.getoutput("sudo rpm -ivh jdk-8u171-linux-x64.rpm")
        output = sp.getoutput("sudo rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")
        output = sp.getoutput("sudo echo 3 > /proc/sys/vm/drop_caches ")
        output = sp.getoutput("sudo rm -rf /n")
        output = sp.getoutput("sudo mkdir /n")

        if node == "1":
        	ip_master = "0.0.0.0"
        	node= "name"
        else:
        	node= "data"

        hdfs = '''<?xml version='1.0'?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.{}.dir</name>\n<value>/n</value>\n</property>\n</configuration>'''
        core = '''<?xml version='1.0'?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n</configuration>'''        
	
        hdfs = hdfs.format(node)
        core = core.format(ip_master)

        
        output = sp.getoutput("sudo chmod +rwx /etc/hadoop")        
        output = sp.getoutput("sudo chmod +rwx /etc/hadoop/hdfs-site.xml")
        output = sp.getoutput("sudo chmod +rwx /etc/hadoop/core-site.xml")
        output = sp.getoutput("sudo chown apache /etc/hadoop/hdfs-site.xml")
        output = sp.getoutput("sudo chown apache /etc/hadoop/core-site.xml")
        
        f = open("/etc/hadoop/hdfs-site.xml",'w')
        f.write(hdfs)
        f.close()

        f = open("/etc/hadoop/core-site.xml",'w')
        f.write(core)
        f.close()
        
        if node == "name":
                output = sp.getoutput("sudo hadoop namenode  -format -force -nonInteractive")   

        print("<span><br>##### {} Service Started #####</span><br>".format(node.upper()))
             
        output = sp.getoutput('sudo hadoop-daemon.sh start {}node'.format(node))
        print("<pre>{}</pre>".format(output))
        
        output = sp.getoutput("sudo jps")
        print("<pre>{}</pre>".format(output))
        
        print("<span><br>##### Filesystem Report #####</span><br>")
        
        output = sp.getoutput("sudo hadoop dfsadmin -report | less")
        print("<pre>{}</pre>".format(output))
elif choice == "2":
        print("<span><br>##### Filesystem Report #####</span><br>")
        output = sp.getoutput("sudo hadoop dfsadmin -report | less")
        print("<pre>{}</pre>".format(output))
elif choice == "3":
        if node == "1":
                node = "name"
        elif node == "2":
                node = "data"
        print("<span><br>##### {}ed {}NODE Services #####</span><br>".format(action,node.upper()))
        if action == "Start":
                action = "start"
        elif action == "Stop":
                action = "stop"
        output = sp.getoutput("sudo hadoop-daemon.sh {} {}node".format(action,node))
        print("<pre>{}</pre>".format(output))
elif choice == "4":
        print("<span><br>##### Visit Here :- #####</span><br>")
        print("<pre>http://{}:50070</pre>".format(ip_master))
elif choice == "5":
        if list_folder == None:
                list_folder = ""
        output = sp.getoutput("sudo hadoop fs -ls /{}".format(list_folder))
        print("<span><br>##### Hadoop Cluster FileSystem #####</span><br>")
        print("<pre>{}</pre>".format(output))
elif choice == "6":
        if read_folder == None:
                read_folder = ""
                output = sp.getoutput("sudo hadoop fs -cat /{}".format(read_file))
        else:
                output = sp.getoutput("sudo hadoop fs -cat /{}/{}".format(read_folder,read_file))
        print("<span><br>##### File Content #####</span><br>")
        print("<pre>{}</pre>".format(output))
elif choice == "7":
        output = sp.getoutput("sudo hadoop fs -mkdir /{}".format(create_folder))
        print("<span><br>##### Folder Created #####</span><br>")
        print("<pre>{}</pre>".format(output))
elif choice == "8":
        output = sp.getoutput("sudo chown apache /var/www/cgi-bin")
        f = open("{}".format(create_file),'w')
        f.write(file_text)
        f.close()
        if file_folder == None:
                file_folder = ""
                output = sp.getoutput("sudo hadoop fs -put {} /{}".format(create_file,file_folder))
        else:
                output = sp.getoutput("sudo hadoop fs -put {} /{}/".format(create_file,file_folder))
        print("<span><br>#### File Uploaded ####<\span><br>")
elif choice == "9":
        if file_folder_emp == None:
                output = sp.getoutput("sudo hadoop fs -touchz /{}".format(create_file_emp))
        else:
                output = sp.getoutput("sudo hadoop fs -touchz /{}/{}".format(file_folder_emp,create_file_emp))
        print("<span><br>#### File Created ####<\span><br>")
elif choice == "10":
        if remove_file_folder == None:
                remove_file_folder = ""
                output = sp.getoutput("sudo hadoop fs -rm /{}".format(remove_file))
        else:
                output = sp.getoutput("sudo hadoop fs -rm /{}/{}".format(remove_file_folder,remove_file))
        print("<span><br>#### File Removed ####<\span><br>")
elif choice == "11":
        output = sp.getoutput("sudo hadoop fs -rmr /{}".format(remove_folder))
        print("<span><br>#### Folder Removed ####<\span><br>")
