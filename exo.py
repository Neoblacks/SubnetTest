import random
from simple_term_menu import TerminalMenu
import os
from colorama import Fore, Back, Style, init

init()

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


def		exercise_default(n_retry):
	ip = gen_random_ipaddress()
	mask = get_random_mask()
	n_fail = 0
	print("IP address: " + ip)
	print("Mask: " + mask)
	print("What is the network address of this IP address?")
	while n_fail <= n_retry:
		network = input(">")
		if network_cal(ip, mask) == network:
			print(Fore.WHITE + Style.NORMAL + Back.GREEN +"\nCorrect \o/\n" + Fore.RESET + Back.RESET)
			return True
		else:
			print(str(n_retry - n_fail) + " remaining tries\n")
			n_fail += 1
	if n_retry == 0:
		show_answer(ip, mask)
	return False, ip, mask


def	explanation():
	print("Explanation")#TODO add explanation of the exercise and the answer
	return

def	show_answer(ip, mask):
	print("The correct answer is: " + network_cal(ip, mask))
	input("Press enter to back to menu")

def	series_challenge():
	nb_correct_answer = 0
	while exercise_default(0) != False:
		nb_correct_answer += 1
	input(f"Your score are {nb_correct_answer} \n") #TODO a ameliorer
	return


def	exercise():
	list = ["Retry", "Explanation", "Back"]
	list_func = [exercise, explanation, menu_choice]
	list2 = ["Retry", "Explanation", "Show Answer", "Back"]
	list_func2 = [exercise, explanation, show_answer, menu_choice]
	succes, ip, mask = exercise_default(2)
	if succes == True:
		menu = TerminalMenu(list)
		menu_index = menu.show()
		if menu_index < len(list_func) and menu_index >= 0:
			list_func[menu_index]()
		else:
			print("Wrong input")
	else:
		menu = TerminalMenu(list2)
		menu_index = menu.show()
		if menu_index == 0:
			os.system("clear")
			exercise()
		elif menu_index == 1:
			os.system("clear")
			explanation()
		elif menu_index == 2:
			os.system("clear")
			show_answer(ip, mask)
		elif menu_index == 3:
			os.system("clear")
			menu_choice()
		else:
			print("Wrong input")
	return

def	menu_choice():
	option = ["Exercise", "Series challenge", "Timer Challenge", "Quit"]
	menu = TerminalMenu(option, title="Subnet training")
	os.system("clear")
	menu_index = menu.show()
	if menu_index == 0:
		os.system("clear")
		exercise()
	elif menu_index == 1:
		os.system("clear")
		series_challenge()
	elif menu_index == 2:
		os.system("clear")
		print("Timer Challenge")
	elif menu_index == 3:
		os.system("clear")

def	main():
	print("Welcome to the IP address exercise!")
	menu_choice()
	return

main()
