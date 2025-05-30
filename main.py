# для преобразования текста в звук
from gtts import gTTS
# для генерации разного имени файла при сохранении звука
import random
# и время 
import time 
# чтобы проиграть звуки нужна библиотека
# если не работает, посмотри readme.txt
import playsound
# чтобы распознать голос в текст
import speech_recognition as sr


#-----функции будут здесь---------

# ф получает аудио из микрофона и переводит в текст 
# использовали гугл библиотеку 
def listen_command():
	# получаем аудио из микрофона
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Скажите вашу команду!")
		audio = r.listen(source)

	# добавим код из документации speech_recognition для гугл распознования
	# также есть другие распознователи такие как Sphinx, Whisper и тд
	# recognize speech using Google Speech Recognition
	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
	    # чтобы вывести на консоль
	    #print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
		# сохраним наше аудио на русском языке
		our_speech = r.recognize_google(audio, language = "ru")
		print("Вы сказали " + our_speech);
		return our_speech
	# далее идет обработчики ошибок	    
	except sr.UnknownValueError:
	    #print("ошибка1 Google Speech Recognition could not understand audio")
	    # когда долго молчишь, выходит ошибка наверху
	    # поэтому попробуем так, когда долго молчим, отправим текст 'молчу'
		return 'молчу'
	except sr.RequestError as e:
	    print("ошибка2 Could not request results from Google Speech Recognition service; {0}".format(e))

	# уже не неужен
	#return input("Скажите вашу команду: ")

# ф отвечает разным ответом на определенный текст
def do_this_command(message):
	# переведем введенный текст на нижний регистр
	message = message.lower()
	# если мы напишем "привет" и др, то получим ответ
	# используя in ищем именно часть текста в message
	if "привет" in message:
		say_message("Привет человек!")
	elif "пока" in message:
		say_message("Пока человек")
		# выйдем с программы
		exit()
	# получаем слово 'молчу' если в ф listen_command ошибка 
	# UnknownValueError, те когда тишина
	elif "молчу" in message:
		print("Жду")
	elif "кто такой зайд" in message:
		say_message("Бессмертный робот") 
	else:
		say_message("команда не распознана!")

# ф используя gTTS для преобразует текст в звук и сохранит в локальную папку и проиграет
def say_message(message):
	# получим текст и преобразуем в звук
	voice = gTTS(message, lang= "ru")
	# определим папку и название для аудиофайла
	file_voice_name = "./audio/" + "_audio_"+str(time.time())+"_"+str(random.randint(0,100000))+".mp3"
	# сохраним звук чтобы потом проиграть, задав случайное имя 
	voice.save(file_voice_name)
	# проиграем созраненный звук
	playsound.playsound(file_voice_name)
	print("Говорит голосовой ассистент: " + message)


#---------------------------------

# ниже код выполнится именно при его запуске этого 
# файла с терминала
if __name__ == '__main__':
	while True:
		# ф будет слушать то что говорит человек на 
		# микрофон и переводить в текст
		command = listen_command()
		# ф будет обрабатывать эту команду
		do_this_command(command)

