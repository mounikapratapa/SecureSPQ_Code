import numpy as np
import faiss
import csv

def generate_data(dataset_size, dimension):
    data_points = np.random.randint(0, 3, size=(dataset_size, dimension)).astype('float32')
    data_labels = [f"R{i+1}" for i in range(dataset_size)]
    return data_points, data_labels

def build_faiss_lsh_index(data_points, dimension, num_bits, num_tables):
    """
    Builds an LSH index using FAISS.
    """
    lsh_index = faiss.IndexLSH(dimension, num_bits)
    lsh_index.train(data_points)
    lsh_index.add(data_points)
    return lsh_index

def find_lsh_candidates(lsh_index, query_vector, k):
    """
    Finds LSH candidates for the given query vector using the FAISS LSH index.
    """
    query_vector = np.array([query_vector], dtype='float32')
    distances, indices = lsh_index.search(query_vector, k)
    lsh_candidates = indices[0]
    return lsh_candidates

def euclidean_distance(p, q):
    return np.sqrt(np.sum((np.array(p) - np.array(q))**2))

def compute_exact_distances(data_points, data_labels, candidates, query_vector, threshold):
    euclidean_similar_lsh = []
    for index in candidates:
        vector = data_points[index]
        label = data_labels[index]
        actual_distance = euclidean_distance(vector, query_vector)
        if actual_distance <= threshold:
            euclidean_similar_lsh.append((label, actual_distance))
    euclidean_similar_lsh.sort(key=lambda x: x[1])
    return euclidean_similar_lsh

def full_euclidean_search(data_points, data_labels, query_vector, threshold):
    euclidean_distances = [(label, euclidean_distance(vector, query_vector))
                           for label, vector in zip(data_labels, data_points)]
    euclidean_distances = [record for record in euclidean_distances if record[1] <= threshold]
    euclidean_distances.sort(key=lambda x: x[1])
    return euclidean_distances

def generate_random_query(dimension):
    return np.random.randint(0, 3, size=dimension).astype('float32')

# Parameters
dataset_size = 2500  # Number of records
dimension = 100  # Dimension of the vectors
num_bits_list = [4, 8, 16, 32, 64, 128, 256, 512]  # Different number of hyperplanes (bits)
num_tables = 1  # Number of hash tables (FAISS has mechanism to build tree anyway)
threshold = 10.0  # Distance threshold
k_percentages = [0.1, 0.5, 1, 5, 10, 20, 50, 100]  # Different percentages of total rows for k

# Generate the dataset
data_points, data_labels = generate_data(dataset_size, dimension)
query_vector = generate_random_query(dimension)

# Full Euclidean distance search for comparison
exact_results = full_euclidean_search(data_points, data_labels, query_vector, threshold)
exact_set = set([label for label, _ in exact_results])

# CSV file to store results
csv_file = 'lsh_faiss_topk_results_percentage.csv'

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Num Bits", "Top-K (%)", "Top-K", "Accuracy", "Num LSH Candidates"])

    for num_bits in num_bits_list:
        # Build the FAISS LSH index
        lsh_index = build_faiss_lsh_index(data_points, dimension, num_bits, num_tables)

        for k_percent in k_percentages:
            k = int((k_percent / 100) * dataset_size)
            # Find LSH candidates using FAISS LSH
            lsh_candidates = find_lsh_candidates(lsh_index, query_vector, k)
            
            # Compute exact Euclidean distances for LSH candidates
            euclidean_similar_lsh = compute_exact_distances(data_points, data_labels, lsh_candidates, query_vector, threshold)
            
            lsh_set = set([label for label, _ in euclidean_similar_lsh])
            
            # Calculate accuracy as the proportion of correct matches
            correct_matches = len(exact_set.intersection(lsh_set))
            accuracy = correct_matches / len(exact_set) if exact_set else 0
            
            num_lsh_candidates = len(lsh_candidates)
            
            # Write results to CSV
            writer.writerow([num_bits, k_percent, k, accuracy, num_lsh_candidates])
            print(f"Num Bits: {num_bits}, Top-K (%): {k_percent}, k: {k}, Accuracy: {accuracy}, Num LSH Candidates: {num_lsh_candidates}")

print(f"Results stored in {csv_file}")
