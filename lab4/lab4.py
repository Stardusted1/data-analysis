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
	input_file = sr.AudioFile(filename)
	with input_file as source:
		audio = r.record(source)
		text = google(audio)
		file = open("result.txt", mode="w")
		file.writelines(text)
		file.close()


def from_mic():
	mic = sr.Microphone(device_index=1)
	with mic as source:
		while True:
			audio = r.record(source, duration=5)
			print(r.recognize_google(audio, language="ru-RU"))
			a = input("exit? y/n")
			if a == "y":
				break


def main():
	from_file("sample1.wav")
	# from_mic()


if __name__ == '__main__':
	main()
