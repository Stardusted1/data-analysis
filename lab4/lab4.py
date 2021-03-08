import speech_recognition as sr

global r
r = sr.Recognizer()


def google(audio):
	try:
		return r.recognize_google(audio, language="ru-RU")
	except Exception:
		print("Google could not understand")
		print(Exception.with_traceback())
		return "None"


def from_file(filename):
	harvard = sr.AudioFile(filename)
	with harvard as source:
		audio = r.record(source)
		text = google(audio)
		file = open("result.txt", mode="w")
		file.writelines(text)
		file.close()


def from_mic():
	mic = sr.Microphone(device_index=1)
	with mic as source:
		audio = r.record(source, duration=5)
		print(r.recognize_google(audio, language="ru-RU"))


def main():
	print(sr.Microphone.list_microphone_names())
	# from_file("hello.wav")
	from_mic()


if __name__ == '__main__':
	main()
