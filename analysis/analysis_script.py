# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Read in pipeline output into pandas dataframe
pipe_out_df = pd.read_csv("combined_out.txt", sep="\t",header=None)

# Take just the normalised counts
num_list = pipe_out_df[1].tolist()

# Reshape the data to KMeans format
samples_array = np.array(num_list).reshape(-1, 1)

# initialise wcss array to use "Elbow Method" to determine best number of clusters to use
# we already know it's control vs. experiment, but for the sake of clarity/understanding
wcss = []  

# Choose a cluster number
max_clusters = 6  

# Iterate over number of clusters
for i in range(1, max_clusters + 1):

    #Generate kmeans objects with increasing number of clusters until final iteration 
    # choose a random seed from which to start from (I like 52)
    # and choose how many iterations of starting with different initial centroid seeds
    kmeans = KMeans(n_clusters=i, random_state=52, n_init=10)
    kmeans.fit(samples_array)

    # Append the interia value/WCSS/homogeneity value to the list
    wcss.append(kmeans.inertia_) 

# Generate the "Elbow Method" plot using the WCSS array we've just made above
# and save it
plt.figure(figsize=(8, 6))
plt.plot(range(1, max_clusters + 1), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel("Cluster no.")
plt.ylabel('Within-Cluster Sum of Squares (WCSS)/Interia/Homogeneity')
plt.xticks(range(1, max_clusters + 1))
plt.grid(True)
plt.savefig('elbow_method.png', bbox_inches='tight')  

# "Elbow Method" and our general knowledge tells us two clusters would be optimal here as it's Experiment vs Control, so:
cluster_num = 2  

# Fit KMeans model to the sample values with our chosen criteria (2 clusters)
# choose a random seed from which to start from (I like 52)
# and choose how many iterations of starting with different initial centroid seeds
kmeans = KMeans(n_clusters=cluster_num, random_state=52,n_init=10)
kmeans.fit(samples_array)

# Get the cluster label assigned to each of the sample values
cluster_labels = kmeans.labels_

# We can get the distance from "centroids" or the "randomly" generated centroids 
# (which are fitted (in the code above) and moved according to the data points/sample values)
# This will tell us how "well" each of the samples fits into a specific cluster
distances = kmeans.transform(samples_array)  

# Iterate over the labels we've assigned and distances associated with each sample
# We use zip here as we're pairing these cluster labels and distances together for each sample to form a tuple
# Since we sorted numerically in the last pipeline step, this will be accurate for sample number on the plot!
for i, (label, distance) in enumerate(zip(cluster_labels, distances)):
    print(f"Sample {i+1}: Cluster {label+1}, Distance to centroid: {distance[label]:.4f}")

# Plot the results using each of the sample's associated clusters and normalised counts
# and save it
plt.figure(figsize=(8, 6))
plt.scatter(range(1,len(num_list)+1), num_list, c=cluster_labels, cmap='viridis', s=100, alpha=0.8)
plt.xlabel('Sample')
plt.ylabel('Normalised Counts')
plt.title(f'KMeans Clustering ({cluster_num} Clusters)')
plt.savefig(f'kmeans_clustering_{cluster_num}_clusters.png', bbox_inches='tight')  

# Let's be safe
plt.close('all')  

