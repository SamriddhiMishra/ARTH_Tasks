#!/usr/bin/python3

print("content-type: text/html")
print()

print('''<style>
pre{
  color: black;
  font-weight: bold;
  font-size: 20px;
}
</style>
''')
import subprocess as sp
import cgi

fs = cgi.FieldStorage()

cmd = fs.getvalue("command")
output = sp.getoutput("sudo "+cmd)
print("<body style='padding: 40px;'>")
print('<h1 style="color:#df405a;" >Output</h1>')
print("<pre>{}</pre>".format(output))
print("</body>")
