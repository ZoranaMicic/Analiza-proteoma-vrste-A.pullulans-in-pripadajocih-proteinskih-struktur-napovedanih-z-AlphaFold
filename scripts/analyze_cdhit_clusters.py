from collections import Counter

cluster_sizes = []

current_size = 0

with open(
    "results/clustering/A_pullulans_cdhit90.faa.clstr"
) as f:

    for line in f:

        line = line.strip()

        if line.startswith(">Cluster"):

            if current_size > 0:
                cluster_sizes.append(current_size)

            current_size = 0

        else:
            current_size += 1


# add last cluster
cluster_sizes.append(current_size)


print("Number of clusters:", len(cluster_sizes))
print("Total proteins in clusters:", sum(cluster_sizes))

print("\nCluster size distribution:")
print(Counter(cluster_sizes).most_common(10))


with open(
    "results/clustering/cluster_sizes.tsv",
    "w"
) as out:

    out.write("Cluster_size\n")

    for size in cluster_sizes:
        out.write(str(size)+"\n")
