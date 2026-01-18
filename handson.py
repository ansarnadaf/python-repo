def twoSum(nums, target):
    # Map to store: { value: index }
    prev_map = {} 

    for i, n in enumerate(nums):
        diff = target - n
        
        # If the 'complement' is in our map, we found the pair!
        if diff in prev_map:
            return [prev_map[diff], i]
        
        # Otherwise, add the current number to the map
        prev_map[n] = i
        
    return [] # Return empty if no solution is found