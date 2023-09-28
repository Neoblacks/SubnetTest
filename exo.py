import random

mask_list = [
	"255.0.0.0",
	"255.0.0.0",
	"255.128.0.0",
	"255.192.0.0",
	"255.224.0.0",
	"255.240.0.0",
	"255.248.0.0",
	"255.252.0.0",
	"255.254.0.0",
	"255.255.0.0",
	"255.255.128.0",
	"255.255.192.0",
	"255.255.224.0",
	"255.255.240.0",
	"255.255.248.0",
	"255.255.252.0",
	"255.255.254.0",
	"255.255.255.0",
	"255.255.255.128",
	"255.255.255.192",
	"255.255.255.224",
	"255.255.255.240",
	"255.255.255.248",
	"255.255.255.252"
]

def	gen_random_ipaddress():
	#table of 4 numbers separated by dots
	ipaddress = []
	for i in range(4):
		ipaddress.append(str(random.randint(0, 255)))
	return ".".join(ipaddress)

def	get_random_mask():
	mask = ""
	mask = mask_list[random.randint(0, len(mask_list)-1)]
	return mask

def	network_cal(ip, mask):
	ip = ip.split(".")
	mask = mask.split(".")
	network = []
	ip_octet = []
	for i in range(4):
		ip_octet.append(str(int(ip[i]) & int(mask[i])))
	return ".".join(ip_octet)

def	exercise(ip, mask):
	print("IP address: " + ip)
	print("Mask: " + mask)
	print("What is the network address of this IP address?")
	network = input(">")
	for i in range(2):
		if network_cal(ip, mask) == network:
			print("Correct!")
			return
		else:
			# print("Wrong! Try again. + remaining tries")
			print("Wrong! Try again.")
			print(str(2 - i) + " remaining tries")
			network = input(">")
	print("The correct answer is: " + network_cal(ip, mask))
	return

def	main():
	print("Welcome to the IP address exercise!")
	ip = gen_random_ipaddress()
	mask = get_random_mask()
	exercise(ip, mask)
	return

main()
