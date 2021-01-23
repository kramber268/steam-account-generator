import random
import time
import datetime

chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'

mail_domains = ['@gmail.com', '@yahoo.com', '@hotmail.com', '@mail.ru', '@yandex.ru', '@outlook.com', '@rambler.ru']
mail_names = ['Rnonniel', 'Haranian', 'Urerydrv', 'Kontobri', 'Gebielai', 'Janudrow', 'Zjotivrg', 'Iouturle', 'Xiniarud', 'Oramalyd', 'Gnerylow', 'Vidronah', 'Usthrime']
steam_first_names = ['Crunchy', 'Delicious', 'Immature', 'Footling', 'Little', 'Bad', 'Ugly', 'Beautiful', 'Dirty']
steam_second_names = ['brownella', 'brownie', 'browna', 'adib', 'brown', 'frog', 'cat', 'dog', 'pirat', 'alien' ]
add_mail_second_name = [True, True, True, True, False, False, False, False, False, False]
add_steam_numbers =    [True, True, True, True, True, True, True, False, False, False]

def localtime():
    time = datetime.datetime.now()
    return f'[{time.strftime("%H:%M:%S")}]'

def generate_password():
	password = ''
	for char in range(random.randint(8, 16)):
		password += random.choice(chars)
	return password

def generate_mail():
	mail = ''
	mail += random.choice(mail_names)

	if random.choice(add_mail_second_name) == True:
		mail += random.choice(steam_second_names)
	else:
		pass

	mail += random.choice(mail_domains)

	return mail

def generate_steam():
	name = f'{random.choice(steam_first_names)}{random.choice(steam_second_names)}'

	if random.choice(add_steam_numbers) == True:
		name += str(random.randint(0, 1000))

	return name

def generator(number: int):
	if number < 0:
		number *= -1
	elif number == 0:
		number = 1
	else:
		pass

	for account_num in range(1, number+1):
		time.sleep(0.6)
		print('='*50)
		print(f'Account-number  {account_num} {localtime()}')
		print(f'Steam-Login:    {generate_steam()}')
		print(f'Steam-Password: {generate_password()}')
		print(f'Email-Login:    {generate_mail()}')
		print(f'Email-Password: {generate_password()}')
		print('='*50+'\n')

def main():
	usr_input = int(input('>>> '))
	generator(usr_input)
	main()
	

if __name__ == '__main__':
	print('steam-account-generator')
	print('How many steam accounts do you need?')
	main()