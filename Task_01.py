list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]

from collections import OrderedDict

def merge_lists(list_1, list_2) -> list:
    """
    Complete this function, by merging the information from list_1 and list_2
    to create a new list, which has all the information about each student from
    both lists in one single dict.

    - Both lists are unsorted
    - Both lists can have missing values (for ex list_2 has missing id=2)
    """
    merged_dict = {}
    
    # Merge the information from list_1
    for item in list_1:
        merged_dict[item['id']] = item
        
    # Merge the information from list_2
    for item in list_2:
        merged_dict.setdefault(item['id'], {}).update(item)
    
    #Sorting dictionary
    merged_dict_sorted = OrderedDict(sorted(merged_dict.items()))
    
    # Convert the merged dictionary to a list
    merged_list = list(merged_dict_sorted.values())
    return merged_list


list_3 = merge_lists(list_1, list_2)
print(list_3)