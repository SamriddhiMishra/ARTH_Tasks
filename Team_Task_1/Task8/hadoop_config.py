import os

def color(n):
	os.system("tput setaf {}".format(n))
def hadoop_config():
        color(3)
        print("\t###### Configuring Hadoop ######\n")
        color(6)
        os.system("rpm -ivh jdk-8u171-linux-x64.rpm")
        os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")
        os.system("echo 3 > /proc/sys/vm/drop_caches ")
        os.system("rm -rf /n")
        os.system("mkdir /n")
        os.system("cd /etc/hadoop")
        color(2)
        print("\n############### Installation Done ###########\n")
        color(6)
        choice =  input("How you want system to configure as masternode/datanode (M/D) :- ")

        if choice == "M":
            ip = "0.0.0.0"
            node="name"
            
        elif choice == "D":
            ip = input("Please input IP addresss of Master node :-")
            node="data"
        else:
            color(1)
            print("Not supported")


        core ='''<?xml version='1.0'?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n</configuration>'''

        hdfs = '''<?xml version='1.0'?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.{}.dir</name>\n<value>/n</value>\n</property>\n</configuration>'''


        hdfs = hdfs.format(node)
        core = core.format(ip)


        os.system("rm -rf /etc/hadoop/hdfs-site.xml")
        os.system("rm -rf /etc/hadoop/core-site.xml")


        os.system('echo "{}" > /etc/hadoop/hdfs-site.xml'.format(hdfs))
        os.system('echo "{}" > /etc/hadoop/core-site.xml'.format(core))
        color(2)
        print("\n############### Configuration Done #############\n")
        color(6)
        if node == 'name':
            os.system('hadoop namenode -format')
            color(2)
            print("\n############ Formatting of NameNode Done #############\n")
            color(6)
        os.system('hadoop-daemon.sh start {}node'.format(node))
        os.system("jps")
        color(2)
        print("\n############ {} Service Started ###########\n".format(node.upper()))
        color(3)
        input("Press Enter to see filesystem report :-")
        print("\n########## Filesystem Report ##########\n")
        os.system("hadoop dfsadmin -report | less")

