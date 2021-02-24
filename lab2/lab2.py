import matplotlib.pyplot as plt
import numpy as np

data_file = "data.csv"


def export_data(data):
	with open(data_file, mode="w") as csfile:
		for indx, word in enumerate(data[0]):
			sting = str(data[0][indx]) + ", " + str(data[1][indx]) + "\n"
			csfile.write(sting)
		csfile.close()


def import_data():
	try:
		with open(data_file, newline='') as csvfile:
			data = np.genfromtxt(data_file, delimiter=', ')
			if data.shape == (300, 2):
				data = data.reshape((2, 300))
			csvfile.close()
			return data
	# spamreader = csv.reader(csvfile, delimiter=', ', quotechar='|')
	# for row in spamreader:
	# 	print(', '.join(row))
	except Exception:
		print(Exception)
	pass


def main():

	generatePoints(x, y)

	mux, sigmax = 0.5, 0.2
	x = np.random.normal(mux, sigmax, size=300)

	muy, sigmay = 0.2, 0.1
	y = np.random.normal(mux, size=300)

	# plt.scatter(x, y)
	# plt.show()

	data = import_data()
	export_data([data.tolist(), data.tolist()])

	plt.scatter(data[0], data[1])
	plt.show()


def generatePoints():
	mux, sigmax = 0.1, 0.2
	x = np.random.normal(mux, sigmax, size=300)
	muy, sigmay = 0.2, 0.1
	y = np.random.normal(mux, size=300)


if __name__ == '__main__':
	main()
