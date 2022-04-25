#binary search - a searching algorithm that accepts sorted array and returns the item u searching for
#it is a better algorithm to simple/stupid search where u search the whole array to find the right item/value
#Big O notation for binary search is - O(log(n)). and that for simple search is O(n)
#Big O notation is runtime for algorithms. It is not measured by time but by the growth of the algorithm
#binary search aka half interval search since we first split the sorted array into two and search starting from the mid value.
#eventually the item you are looking for will be the mid_idx therefore it will be returned or found
def binary_search(sorted_array, item):
    """a search algorithm that returns the index of the item you are searching for.It works this way:
    1.if key/item is equal to guess/mid_value we have found item
    2. if key > guess, we increment mid_idx plus one(low=mid+1). so it can get closer to key
    3. else if key < guess we decrement mid_idx minus one(high=mid-1)
    4. else we return nothing at all, indicating the item cannot be found"""
    low_idx = 0
    high_idx = len(sorted_array)-1

    while low_idx <= high_idx:
        mid_idx = (low_idx+high_idx)//2
        guess = sorted_array[mid_idx] #guess is the mid value.
        if item == guess:
            return f'can be found at: index {mid_idx}'
        elif item > guess:
            low_idx = mid_idx + 1
        else:
            high_idx = mid_idx - 1
    return 'Item cannot be found'


print(binary_search([2, 4, 6, 8], 4))







