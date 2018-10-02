import json
import time

coc = 0  # comparison operation counter
eoc = 0  # exchange operation counter

class Helicopter:
    def __init__(self, maximum_lifting_weight, name, maximum_height):
        self.maximum_lifting_weight = maximum_lifting_weight
        self.name = name
        self.maximum_height = maximum_height


def selection_sort(helicopters):
    global coc
    global eoc

    for i in range(len(helicopters)-1):
        least = i
        for j in range(least+1, len(helicopters)):
            coc += 1
            if helicopters[j].maximum_height < helicopters[least].maximum_height:
                least = j

        eoc += 1
        tmp_helicopter = helicopters[i]
        helicopters[i] = helicopters[least]
        helicopters[least] = tmp_helicopter

    return helicopters


def merge_sort(mas):
    global coc
    global eoc

    coc += 1
    if len(mas) <= 1:
        return mas

    middle = len(mas) // 2
    left = merge_sort(mas[:middle])
    right = merge_sort(mas[middle:])

    return merge(left, right)


def merge(left_arr, right_arr):
    global coc
    global eoc

    result = []
    left_i = 0
    right_i = 0
    first_count = False
    coc +=2
    while left_i < len(left_arr) and right_i < len(right_arr):

        if first_count:
            coc += 2
        first_count = True
        coc += 1

        if left_arr[left_i].maximum_lifting_weight > right_arr[right_i].maximum_lifting_weight:

            eoc += 1

            result.append(left_arr[left_i])
            left_i += 1
        else:
            eoc += 1

            result.append(right_arr[right_i])
            right_i += 1

    first_count = False
    coc += 1
    while left_i < len(left_arr):

        if first_count:
            coc += 1
        first_count = True

        eoc += 1
        result.append(left_arr[left_i])
        left_i += 1

    first_count = False
    coc += 1
    while right_i < len(right_arr):

        if first_count:
            coc += 1
        first_count = True

        eoc+=1
        result.append(right_arr[right_i])
        right_i += 1

    return result


if __name__ == '__main__':
    helicopters = []
    data = json.load(open('data.json'))
    for i in range(len(data)):
        helicopters.append(Helicopter(data[i].get("maximum_lifting_weight"), data[i].get("name"), data[i].
                                      get("maximum_height")))


    coc = 0
    eoc = 0
    start_time = time.time()
    sorted_helicopters_by_max_height = selection_sort(helicopters)
    estimated_time = time.time() - start_time
    print('SELECTION SORT')
    print('Algorithm running time : %s seconds' % estimated_time)
    print('The number of comparison operations : ' + str(coc))
    print('Number of exchange operations : ' + str(eoc))
    print('Sort result :')
    for helicopter in sorted_helicopters_by_max_height:
        print('maximum height = ' + str(helicopter.maximum_height))


    coc = 0
    eoc = 0
    start_time = time.time()
    sorted_helicopters_by_max_lift_weight = merge_sort(helicopters)
    estimated_time = time.time() - start_time

    print('\nMERGE SORT')
    print('Algorithm running time : %s seconds' % estimated_time)
    print('The number of comparison operations : ' + str(coc))
    print('Number of exchange operations : ' + str(eoc))
    print('Sort result : ')
    for helicopter in sorted_helicopters_by_max_lift_weight:
        print('maximum_lifting_weight = ' + str(helicopter.maximum_lifting_weight))
