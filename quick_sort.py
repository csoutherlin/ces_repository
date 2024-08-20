# divide and conquer

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    
    else: 
        pivot = lst[0]
        less = [x for x in lst[1:] if x <= pivot]
        more = [x for x in lst[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(more)
    

example_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
sorted_array = quick_sort(example_array)
print(sorted_array)