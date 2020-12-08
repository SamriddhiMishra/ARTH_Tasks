#! /usr/bin/python3

print("content-type: text/html")
print()

print('''<style>
pre{
  color: #de6262;
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
print('<h1 style="color: #ffb78c;" >Output</h1>')


import cgi
import subprocess as sp

fs = cgi.FieldStorage()

#---
choice = fs.getvalue("choice")
#---
new_kname = fs.getvalue("new_kname")
#---
new_sgname = fs.getvalue("new_sgname")
descp = fs.getvalue("descp")
#---
rule_sgname = fs.getvalue("rule_sgname")
protocol = fs.getvalue("protocol")
port = fs.getvalue("port")
ip = fs.getvalue("ip")
#---
ami = fs.getvalue("ami")
osname = fs.getvalue("osname")
ec2_az = fs.getvalue("ec2_az")
itype = fs.getvalue("itype")
ec2_kname = fs.getvalue("ec2_kname")
ec2_sgname = fs.getvalue("ec2_sgname")
#---
vol_az = fs.getvalue("vol_az")
size = fs.getvalue("size")
#---
vid = fs.getvalue("vid")
iid = fs.getvalue("iid")
vol_name = fs.getvalue("vol_name")
#---

choice = int(choice)

if choice == 1:
    output = sp.getoutput("sudo aws ec2 create-key-pair --key-name {}".format(new_kname))
    print("<span><br>#### Created Key-Pair ####</span><br>")
    print("<pre>{}</pre>".format(output))
elif choice == 2:
    output = sp.getoutput('sudo aws ec2 create-security-group --group-name {} --description "{}"'.format(new_sgname,descp))
    print("<span><br>#### Created Security Group ####</span><br>")
    print("<pre>{}</pre>".format(output))
elif choice == 3:
    output = sp.getoutput("sudo aws ec2 authorize-security-group-ingress --group-name {} --protocol {} --port {} --cidr {}/0".format(rule_sgname,protocol,port,ip))
    print("<span><br>#### Added rules to SG ####</span><br>")
    print("<pre>{}</pre>".format(output))
elif choice == 4:
    ami = int(ami)
    if ami == 1:
        ami = 'ami-04d29b6f966df1537'
    elif ami == 2:
        ami = 'ami-096fda3c22c1c990a'
    elif ami == 3:
        ami = 'ami-0885b1f6bd170450c'
    elif ami == 4:
        ami = 'ami-02b5cd5aa444bee23'
    if itype == "":
        itype = "t2.micro"
    ec2_az = "--placement " + '"AvailabilityZone='+ ec2_az + '"'
    name = "--tag-specifications " + '"ResourceType = instance , Tags = [{Key=\"Name\",Value=\"' + osname+'"}]"'
    output = sp.getoutput("sudo aws ec2 run-instances --image-id {0} --instance-type {1} --key-name {2} --security-group-ids {3} {4} {5}".format(ami,itype,ec2_kname,ec2_sgname,name,ec2_az))
    print("<span><br>#### Launched Instance ####</span><br>")
    print("<pre>{}</pre>".format(output))
elif choice == 5:
    output = sp.getoutput('sudo aws ec2 create-volume --availability-zone "{}" --size {}'.format(vol_az,size))
    print("<span><br>#### Created EBS Volume in AZ -{} ####</span><br>".format(vol_az))
    print("<pre>{}</pre>".format(output))
elif choice == 6:
    output = sp.getoutput("sudo aws ec2 attach-volume --instance-id {} --volume-id {} --device {}".format(iid,vid,vol_name))
    print("<span><br>#### Attached EBS Volume - {} ####</span><br>".format(vol_name))
    print("<pre>{}</pre>".format(output))
