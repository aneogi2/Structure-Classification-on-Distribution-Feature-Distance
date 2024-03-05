import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

def bhattacharya_distance(hist1, hist2):
    """Calculate Bhattacharya Distance between two histograms."""
    assert len(hist1) == len(hist2), "Histograms should be of equal lengths"
    h1_mean = np.mean(hist1)
    h2_mean = np.mean(hist2)
    score = sum(sqrt(h1 * h2) for h1, h2 in zip(hist1, hist2))
    return sqrt(1 - (1 / sqrt(h1_mean * h2_mean * len(hist1)**2)) * score)

def preprocess_data(file_path):
    """Preprocess data from a given file path."""
    dataset = []
    with open(file_path) as file:
        lines = file.readlines()
        for line in lines:
            if "ITEM: ATOMS id c_Qf[1] c_Qf[2]" not in line:
                cols = line.split()
                if len(cols) == 3:
                    dataset.append([float(cols[1]), float(cols[2])])
    return np.array(dataset)

def analyze_dataset(dataset):
    """Analyze dataset to extract features and perform histogram analysis."""
    # Extract features
    q4_min, q4_max = np.amin(dataset, axis=0)[0], np.amax(dataset, axis=0)[0]
    q6_min, q6_max = np.amin(dataset, axis=0)[1], np.amax(dataset, axis=0)[1]
    q4_mean, q4_std = np.mean(dataset, axis=0)[0], np.std(dataset, axis=0)[0]
    q6_mean, q6_std = np.mean(dataset, axis=0)[1], np.std(dataset, axis=0)[1]
    
    # Perform histogram analysis
    # Your histogram analysis logic here...

    # Return analyzed data
    return {
        "q4": {"min": q4_min, "max": q4_max, "mean": q4_mean, "std": q4_std},
        "q6": {"min": q6_min, "max": q6_max, "mean": q6_mean, "std": q6_std},
        # Include histogram analysis results here...
    }

def main(file_path):
    """Main function to execute data analysis workflow."""
    dataset = preprocess_data(file_path)
    analysis_results = analyze_dataset(dataset)
    
    # Print analysis results
    for feature, stats in analysis_results.items():
        print(f"{feature} statistics:")
        for stat, value in stats.items():
            print(f"  {stat}: {value}")
    
    # Histogram analysis results printing...
    # Additional analysis results printing...

if __name__ == "__main__":
    file_path = "Q.dat"
    main(file_path)
