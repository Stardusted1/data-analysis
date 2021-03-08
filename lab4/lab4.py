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


def main():
	harvard = sr.AudioFile('hello.wav')
	with harvard as source:
		audio = r.record(source)
		text = google(audio)
		file = open("result.txt", mode="w")
		file.writelines(text)
		file.close()


if __name__ == '__main__':
	main()
