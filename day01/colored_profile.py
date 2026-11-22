from colorama import Fore, Style

first_name = input(f"Имя: ")
last_name = input(f"Фамилия: ")
group = input(f"Группа: ")

print(Fore.CYAN + Style.BRIGHT + "=== ПРОФИЛЬ СТУДЕНТА ===")
print(Fore.GREEN + f"Имя: {first_name}")
print(Fore.GREEN + f"Фамилия: {last_name}")
print(Fore.GREEN + f"Группа: {group}")
print(Style.RESET_ALL, end="")