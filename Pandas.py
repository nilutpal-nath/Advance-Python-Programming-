# Data Manipulation with Pandas Series
# Experiment 11: Based on the aim to create a Pandas Series with ten random numbers using NumPy and Pandas

import pandas as pd
import numpy as np

def main():
    # Generate ten random numbers using NumPy[cite: 81]
    random_numbers = np.random.rand(10)
    
    # Create a Pandas Series using the generated numbers[cite: 81]
    series = pd.Series(random_numbers, name="RandomSeries")
    
    # Display the Pandas Series[cite: 81]
    print("Pandas Series with Ten Random Numbers:")
    print(series)

if __name__ == "__main__":
    main()