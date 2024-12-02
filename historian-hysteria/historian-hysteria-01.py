def calculate_distance(filename):
    try:
        with open(filename) as f:
            pairs = [tuple(map(int, line.split())) for line in f]
        
        nums1, nums2 = zip(*pairs)
        return sum(abs(a - b) for a, b in zip(sorted(nums1), sorted(nums2)))
    
    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'")
        return None
    except ValueError:
        print("Error: File contains invalid number format")
        return None

if __name__ == "__main__":
    result = calculate_distance("01-data.txt")
    if result is not None:
        print(f"Total distance: {result}")