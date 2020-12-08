#! /usr/bin/python3

print("content-type: text/html")
print()

print('''<style>
pre{
  color: #654ea3;
  font-weight: bold;
  font-size: 20px;
}
span{
  color: #e5abc6;
  font-weight: bold;
  font-size: 26px;
}
</style>
''')


print('<body style="padding: 40px;">')
print('<h1 style="color:#e5abc6;" >Output</h1>')

import cgi
import subprocess as sp

fs = cgi.FieldStorage()

#---
choice = fs.getvalue("choice")
#---
show_pv = fs.getvalue("show_pv")
#---
show_vg = fs.getvalue("show_vg")
#---
show_lv = fs.getvalue("show_lv")
#---
create_pv = fs.getvalue("create_pv")
#---
create_vg = fs.getvalue("create_vg")
vg_pv1 = fs.getvalue("vg_pv1")
vg_pv2 = fs.getvalue("vg_pv2")
#---
create_lv = fs.getvalue("create_lv")
create_lv_size = fs.getvalue("create_lv_size")
create_lv_vg = fs.getvalue("create_lv_vg")
create_lv_mount = fs.getvalue("create_lv_mount")
#---
extend_lv = fs.getvalue("extend_lv")
extend_lv_vg = fs.getvalue("extend_lv_vg")
extend_lv_size = fs.getvalue("extend_lv_size")
#---
reduce_lv = fs.getvalue("reduce_lv")
reduce_lv_vg = fs.getvalue("reduce_lv_vg")
reduce_lv_size = fs.getvalue("reduce_lv_size")
reduce_lv_mount = fs.getvalue("reduce_lv_mount")
#---
extend_vg = fs.getvalue("extend_vg")
extend_vg_pv = fs.getvalue("extend_vg_pv")
#---
reduce_vg = fs.getvalue("reduce_vg")
reduce_vg_pv = fs.getvalue("reduce_vg_pv")
#---
lv_remove_path = fs.getvalue("lv_remove_path")
#---
vg_remove = fs.getvalue("vg_remove")
#---
pv_remove = fs.getvalue("pv_remove")
#---
create_file = fs.getvalue("create_file")
file_text = fs.getvalue("file_text")
file_folder = fs.getvalue("file_folder")

choice = int(choice)

if choice == 1:
        output = sp.getoutput('sudo fdisk -l')
        print("<pre>{}</pre>".format(output))
elif choice == 2:
        if show_pv == None:
                show_pv = ""
        output = sp.getoutput('sudo pvdisplay '+show_pv)
        print("<span><br>#### Physical Volume/s -> {} ####<br></span>".format(show_pv))
        print("<pre>{}</pre>".format(output))
elif choice == 3:
        if show_vg == None:
                show_vg = ""
        output = sp.getoutput('sudo vgdisplay '+show_vg)
        print("<span><br>#### Volume Group/s -> {} ####</span><br>".format(show_vg))
        print("<pre>{}</pre>".format(output))
elif choice == 4:
        if show_lv == None:
                show_lv = ""
        output = sp.getoutput('sudo lvdisplay '+show_lv)
        print("<span><br>#### Logical Volume/s -> {} ####</span><br>".format(show_lv))
        print("<pre>{}</pre>".format(output))
elif choice == 5:
        output = sp.getoutput('sudo pvcreate '+create_pv)
        print("<span><br>#### Created Physical Volume -> {} ####</span><br>".format(create_pv))
        print("<pre>{}</pre>".format(output))
elif choice == 6:
        output = sp.getoutput('sudo vgcreate '+create_vg+' '+vg_pv1+' '+vg_pv2)
        print("<span><br>#### Created Volume Group -> {} ####</span><br>".format(create_vg))
        print("<pre>{}</pre>".format(output))
elif choice == 7:
        output = sp.getoutput('sudo lvcreate --size {} --name {} {}'.format(create_lv_size,create_lv,create_lv_vg))
        output = sp.getoutput('sudo mkfs.ext4 /dev/{}/{}'.format(create_lv_vg,create_lv))
        output = sp.getoutput('sudo rm -rf {}'.format(create_lv_mount))
        output = sp.getoutput('sudo mkdir {}'.format(create_lv_mount))
        output = sp.getoutput('sudo chown apache {}'.format(create_lv_mount))
        output = sp.getoutput('sudo -u root  mount /dev/{}/{} {}'.format(create_lv_vg,create_lv,create_lv_mount))
        print("</span><br>#### 'Created LV! Ready to store files. Mounted to folder {} ####</span><br>".format(create_lv_mount))
        print("<pre>{}</pre>".format(output))
elif choice == 8:
        output = sp.getoutput('sudo lvextend --size {} /dev/{}/{}'.format(extend_lv_size,extend_lv_vg,extend_lv))
        output = sp.getoutput('sudo resize2fs /dev/{}/{}'.format(extend_lv_vg,extend_lv))
        print("</span><br>#### Extended LV size -> {} ####</span><br>".format(extend_lv))
        print("<pre>{}</pre>".format(output))
elif choice == 9:
        output = sp.getoutput('sudo umount /dev/{}/{}'.format(reduce_lv_vg,reduce_lv))
        output = sp.getoutput('sudo e2fsck -f /dev/{}/{}'.format(reduce_lv_vg,reduce_lv))
        output = sp.getoutput('sudo resize2fs -f /dev/{}/{} {}'.format(reduce_lv_vg,reduce_lv,reduce_lv_size))      
        print("<span><br>#### Reduced LV size -> {} ####</span><br>".format(reduce_lv))        
        print("<pre>{}</pre>".format(output))
        output = sp.getoutput('sudo lvreduce -f --size {} /dev/{}/{}'.format(reduce_lv_size,reduce_lv_vg,reduce_lv))
        print("<pre>{}</pre>".format(output))
        output = sp.getoutput('sudo mount /dev/{}/{} {}'.format(reduce_lv_vg,reduce_lv,reduce_lv_mount))
        print("<pre>{}</pre>".format(output))
elif choice == 10:
        output = sp.getoutput('sudo vgextend {} {}'.format(extend_vg,extend_vg_pv))
        print("<span><br>#### Extended VG size ####</span><br>")
        print("<pre>{}</pre>".format(output))
elif choice == 11:
        output = sp.getoutput('sudo pvmove {}'.format(reduce_vg_pv))
        output = sp.getoutput('sudo vgreduce {} {}'.format(reduce_vg,reduce_vg_pv))
        print("<span><br>#### Reduced VG size ####</span><br>")
        print("<pre>{}</pre>".format(output))
elif choice == 12:
        output = sp.getoutput('sudo umount {}'.format(lv_remove_path))
        output = sp.getoutput('sudo lvremove {} -y'.format(lv_remove_path))
        print("<span><br>#### LV Removed -> {} ####</span><br>".format(lv_remove_path))
        print("<pre>{}</pre>".format(output))
elif choice == 13:
        output = sp.getoutput('sudo vgremove {} -y'.format(vg_remove))
        print("<span><br>#### VG Removed -> {} ####</span><br>".format(vg_remove))
        print("<pre>{}</pre>".format(output))
elif choice == 14:
        output = sp.getoutput('sudo pvremove {} -y'.format(pv_remove))
        print("<span><br>#### PV Removed -> {} ####</span><br>".format(pv_remove))
        print("<pre>{}</pre>".format(output))
elif choice == 15:
        output = sp.getoutput("sudo chown apache /var/www/cgi-bin")
        f = open("{}".format(create_file),'w')
        f.write(file_text)
        f.close()
        output = sp.getoutput("sudo cp {} {}".format(create_file,file_folder))
        print("<span><br>#### File Created ####</span><br>")
print("</body>")
