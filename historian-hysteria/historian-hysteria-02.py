def calculate_similarity(filename):
    try:
        with open(filename) as f:
            pairs = [tuple(map(int, line.split())) for line in f]
        
        nums1, nums2 = zip(*pairs)
        similarity_score = 0
        for num in nums1:
            count = nums2.count(num)
            similarity_score += num * count
        return similarity_score
    
    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'")
        return None
    except ValueError:
        print("Error: File contains invalid number format")
        return None

if __name__ == "__main__":
    result = calculate_similarity("01-data.txt")
    if result is not None:
        print(f"Similarity score: {result}")