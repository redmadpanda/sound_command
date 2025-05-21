# нужно установить гугла голосовой помощник
pip install gTTS

# чтобы проигрывать сохраненные звуки от гугла нужна библиотека
# сперва это
pip install --upgrade setuptools wheel
# потом только
pip install playsound

# если не идет, то нужно понизить до playsound 1.2.2. 
pip install playsound==1.2.2 

# для распознования голоса пользователя в текст нужно
pip install SpeechRecognition

# также нужно для микрофона
pip install PyAudio

!!!нужно создать папку audio в исходной директории