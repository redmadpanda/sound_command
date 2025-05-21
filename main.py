def print_hi(name):
	print(f'Hi, {name}')

#-----функции будут здесь---------
def listen_command():
	return input("Скажите вашу команду: ")

def do_this_command(message):
	# переведем введенный текст на нижний регистр
	message = message.lower()
	# если мы напишем "привет" и др, то получим ответ
	if "привет" in message:
		say_message("Привет человек!")
	elif "пока" in message:
		say_message("Пока человек")
	else:
		say_message("команда не распознана!")

def say_message(message):
	print(message)


#---------------------------------

# ниже код выполнится именно при его запуске этого 
# файла с терминала
if __name__ == '__main__':
	while True:
		# ф будет слушать то что говорит человек
		command = listen_command()
		# ф будет обрабатывать эту команду
		do_this_command(command)

