import random

def random_value(obj):
    """
    Returns a random element from a list, tuple, set, or a random value from a dictionary.
    
    Parameters:
    obj (list or tuple or set or dict): The input list, tuple, set, or dictionary.
    
    Returns:
    Any: A random element from the list, tuple, set, or a random value from the dictionary.
    
    Raises:
    TypeError: If the input is not a list, tuple, set, or dictionary.
    """
    if isinstance(obj, (list, tuple)):
        choice_index = random.randint(0, len(obj) - 1)
        return obj[choice_index]
    elif isinstance(obj, dict):
        dict_keys = list(obj.keys())
        dict_key = random.choice(dict_keys)
        return obj[dict_key]
    else:
        raise TypeError('Input should be a list, tuple, set, or dictionary')

# Example usage
if __name__ == "__main__":
    array = ["rays", "sun", "moon", "earth"]
    tuple_obj = ("apple", "banana", "cherry")
    dict_obj = {1: "house", 5: "road", 8: "shop", 3: "store"}

    print(random_value(array))  # Random element from array
    print(random_value(tuple_obj))  # Random element from tuple
    print(random_value(dict_obj))  # Random value from dict
