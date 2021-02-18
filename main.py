from colorama import Back, Fore

str_len = 2
spam_str = "spam!"
non_spam_str = "not spam"


def create_dict(data):
	words = []
	overall = list(filter(lambda x: len(x) > str_len, " ".join(data).lower().split(" ")))

	for word in overall:
		overall.remove(word)
		words.append([word, 1])
		while True:
			if word in overall:
				overall.remove(word)
				words[-1][1] += 1
			else:
				break

	return words


def create_not_spam_spam_dict(not_spam_dict, spam_dict):
	final_dict = []
	# temp_not_spam = map(lambda i: final_dict.append(i[0]), not_spam_dict)
	# temp_spam = map(lambda i: final_dict.append(i[0]), spam_dict)
	for item in not_spam_dict:
		is_added: bool = False
		for item2 in spam_dict:
			if item[0] == item2[0]:
				final_dict.append([item[0], item[1], item2[1]])
				spam_dict.remove(item2)
				is_added = True
				break
		if not is_added:
			final_dict.append([item[0], item[1], 0])
	for item in spam_dict:
		final_dict.append([item[0], 0, item[1]])

	return final_dict


def create_weights(word_dict):
	def get_normed(p_word, n_word):
		return (n_word * p_word + 0.5) / (n_word + 1)

	weights_arr = []
	for word in word_dict:
		summa = word[1] + word[2]
		part = 1 / summa
		word1 = get_normed(word[1] * part, summa)
		word2 = get_normed(word[2] * part, summa)
		weights_arr.append([word[0], word1, word2])
	return weights_arr


def calc_p_test_line(test_str, weights_dict):
	test_data = list(filter(lambda x: len(x) > str_len, test_str.lower().split(" ")))
	base_p_spam = 0.5
	base_p_not_spam = 0.5
	for word in test_data:
		for tup in weights_dict:
			if tup[0] == word:
				base_p_not_spam *= tup[1]
				base_p_spam *= tup[2]
	res = spam_str
	if base_p_not_spam > base_p_spam:
		res = non_spam_str
	return [test_data, base_p_not_spam, base_p_spam, res]


def print_results(test_dataw, weights_arr):
	for item in test_dataw:
		res = calc_p_test_line(item, weights_arr)
		if res[3] == spam_str:
			print(Back.RED + Fore.BLACK + "headline - " + str(" ".join(res[0])) + ", P not-spam - " + str(
				round(res[1], 3)) + ", P spam - " + str(round(res[2], 3)) + ", so it is - " + res[3])
		else:
			print(
				Back.GREEN + Fore.BLACK + "headline - " + str(" ".join(res[0])) + ", P not-spam - " + str(
					round(res[1], 3)) + ", P spam - " + str(
					round(res[2], 3)) + ", so it is - " + res[3])


def main():
	test = [
		"Free file tomorrow",
		"New meeting tomorrow file",
		"corporate party tomorrow",
		"new greeting text",
		"Free sales party",
		"free file for you",
		"free file upload"
		"Значит ли, что новые телефоны рассчитаны на животных",
		"Электричество платное для животных",
		"Новые животные поступили на продажу",
		"Методы передачи телефона от животных человеку",
		"Животные и новый тариф на использование электричества",
		"Каждый электрик должен знать где спит животное",
		"Что такое телефон и как ими пользуется животное",
		"Как понимает животное что телефон полностью заряжен"
	]

	spam = [
		"Free sales party",
		"free file for you",
		"free file upload"
		"Телефоны и электрошок",
		"Животные казнили животных используя электричество",
		"Животное увидело барсука и включил электричество",
		"Как найти хорошее животное используя телефон",
		"Вас посетило электричество",
		"Вас одолевают животные. Используйте электричество",
		"Можно пользоваться электричеством для подзарядки телефонов домашних животных",
		"Каждый кто прочитает это должен найти свое животное"
	]

	not_spam = [
		"New meeting tomorrow file",
		"corporate party tomorrow",
		"new greeting text"
		"Новые животные для оплаты электричества",
		"Новые телефоны по самым низким ценам ",
		"Вы просрочили оплату за электричество",
		"Ваше животное снова говорило со мной по телефону",
		"Животное снова нашло выключатель",
		"Электричество по самым выгодным ценам",
		"Видит ли электричество животных",
		"Почему не стоит пользоваться электричеством"
	]

	# [["word", times]]
	spam_dict = create_dict(spam)
	not_spam_dict = create_dict(not_spam)

	# [["word", not_spam_times, spam_times]]
	overall_dict = create_not_spam_spam_dict(not_spam_dict, spam_dict)

	# [["word", not_spam_times, spam_times]]
	weights_arr = create_weights(overall_dict)

	print_results(test, weights_arr)


if __name__ == '__main__':
	main()
