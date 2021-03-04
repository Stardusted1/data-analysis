import matplotlib.pyplot as plt
import numpy as np
import scipy.cluster.hierarchy as sch
from scipy.cluster.vq import kmeans
from sklearn.datasets import make_blobs

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
	except Exception:
		print(Exception)
	pass


def main():
	n_samples = 350
	n_components = 4

	X, y_true = make_blobs(n_samples=n_samples, centers=n_components,
	                       cluster_std=0.8, random_state=15)

	for k, col in enumerate(X):
		plt.scatter(col[0], col[1],
		            c="b", marker='.', s=10)
	plt.yticks([])
	plt.xticks([])
	plt.show()

	centers_init, indices = kmeans(X, n_components)

	sch.dendrogram(sch.linkage(centers_init, method='ward', metric='euclidean', ))
	plt.show()

	plt.figure(1)
	colors = ['#4EACC5', '#FF9C34', '#4E9A06', '#4E2A24']

	for k, col in enumerate(colors):
		cluster_data = y_true == k
		plt.scatter(X[cluster_data, 0], X[cluster_data, 1],
		            c=col, marker='.', s=10)

	plt.scatter(centers_init[:, 0], centers_init[:, 1], c='#000', marker="x", s=50)
	plt.show()


def plot_dendrogram(model, **kwargs):
	counts = np.zeros(model.children_.shape[0])
	n_samples = len(model.labels_)
	for i, merge in enumerate(model.children_):
		current_count = 0
		for child_idx in merge:
			if child_idx < n_samples:
				current_count += 1  # leaf node
			else:
				current_count += counts[child_idx - n_samples]
		counts[i] = current_count

	linkage_matrix = np.column_stack([model.children_, model.distances_,
	                                  counts]).astype(float)
	sch.dendrogram(linkage_matrix, **kwargs)


if __name__ == '__main__':
	main()
