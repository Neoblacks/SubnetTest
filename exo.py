import random
from simple_term_menu import TerminalMenu
import os
from colorama import Fore, Back, Style, init
import fontstyle


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
			return True , ip, mask
		elif network == "back":
			return False, None, None
		else:
			print(str(n_retry - n_fail) + " remaining tries\n")
			n_fail += 1
	# if n_retry == 0:
	# 	show_answer(ip, mask)
	return False, ip, mask


def	explanation():
	print("Explanation")#TODO add explanation of the exercise and the answer
	return

def	show_answer(ip, mask):
	print("The correct answer is: " + network_cal(ip, mask))
	input("Press enter to back to menu")
	menu_choice()

def series_challenge():
	nb_correct_answer = 0
	while True:  # Boucle infinie jusqu'à ce que l'utilisateur échoue
		success, ip, mask = exercise_default(0)
		if success:
			#Add power 2 to nb_correct_answer
			if nb_correct_answer == 0:
				nb_correct_answer = 1
			else:
				nb_correct_answer *= 2
			print(f"Your score is {nb_correct_answer}\n")
		else:
			break  # Sort de la boucle si l'utilisateur échoue
	print(f"Your score is {nb_correct_answer}\n")
	show_answer(ip, mask)


def	exercise():
	list = ["Retry", "Explanation", "Back"]
	list_func = [exercise, explanation, menu_choice]
	list2 = ["Retry", "Explanation", "Show Answer", "Back"]
	succes, ip, mask = exercise_default(2)
	if succes == True:
		menu = TerminalMenu(list)
		menu_index = menu.show()
		if menu_index == 0:
			os.system("clear")
			exercise()
		elif menu_index == 1:
			os.system("clear")
			explanation()
		elif menu_index == 2:
			os.system("clear")
			menu_choice()
	elif ip == None and mask == None:
		os.system("clear")
		menu_choice()
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
	print("Welcome to the IP address exercise!\n")
	# text = fontstyle.apply('GEEKSFORGEEKS', 'bold/Italic/red/GREEN_BG')
	# print(text)
	print(fontstyle.apply('Welcome to the IP address exercise!', 'bold/Italic/yellow/GRAY_BG'))
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
		return

def	main():
	menu_choice()
	os.system("clear")
	return

main()
