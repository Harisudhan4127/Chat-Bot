from sklearn.cluster import KMeans

x = [[14],[26],[35],[20],[77],[80]]

kmeans = KMeans(n_clusters=2)

kmeans.fit(x)

print("cluster labels : ", kmeans.labels_)
print("cluster Centers : ", kmeans.cluster_centers_)