import socket

ip = input("Digite o IP Alvo: ")

for PORTS in range(1,10000):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = s.connect_ex((ip, PORTS))
	
	if result == 0:
		print("{} open/aberta".format(PORTS))
	else:
		pass

