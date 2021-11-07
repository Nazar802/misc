import telnetlib

Host='localhost'
password='root'
username='root'

tn=telnetlib.Telnet(Host)
tn.read_until(b"Username:")
tn.write(username.encode("ascii")+b"\n")
tn.read_until(b"Password:")
tn.write(password.encode("ascii")+b"\n")