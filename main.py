# для преобразования текста в звук
from gtts import gTTS
# для генерации разного имени файла при сохранении звука
import random
# и время 
import time 


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
		# выйдем с программы
		exit()
	else:
		say_message("команда не распознана!")

def say_message(message):
	# получим текст и приобразуем в звук
	voice = gTTS(message, lang= "ru")
	# определим случайное название для аудиофайла
	file_voice_name = "_audio_"+str(time.time())+"_"+str(random.randint(0,100000))+".mp3"
	# сохраним звук чтобы потом проиграть, задав случайное имя 
	voice.save(file_voice_name)
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

