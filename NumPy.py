# Understanding NumPy Basics and Array Operations
# Experiment 10: Based on the aim to create a one-dimensional NumPy array containing numbers from 1 to 10 using np.arange()

import numpy as np

def main():
    # Use np.arange() to create an array containing numbers from 1 to 10 (exclusive of 11)[cite: 76]
    array = np.arange(1, 11)
    
    # Display the created array[cite: 76]
    print("NumPy Array (1 to 10):")
    print(array)
    print(f"Array data type: {array.dtype}")
    print(f"Array shape: {array.shape}")

if __name__ == "__main__":
    main()