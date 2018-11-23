def get_number_in_decimal_number_system(number_in_binary_number_system):
    return int(number_in_binary_number_system, 2)


def get_list_number_x_in_pow(number_X, number_in_decimal_number_system):
    list_number_x_in_pow = []
    is_generate_number_x_in_pow = True
    while is_generate_number_x_in_pow:
        if not list_number_x_in_pow:
            list_number_x_in_pow.append(pow(number_X, 0))
        else:
            if list_number_x_in_pow[-1] < number_in_decimal_number_system:
                list_number_x_in_pow.append(pow(number_X, len(list_number_x_in_pow)))
            else:
                is_generate_number_x_in_pow = False

    return list_number_x_in_pow


def check_for_number_in_pow(number_in_binary_system, list_number_x_in_pow):
    count_of_element = 0
    for i in list_number_x_in_pow:
        if count_of_element == 0:
            if get_number_in_decimal_number_system(number_in_binary_system[count_of_element]) == i:
                check_for_number_in_pow(number_in_binary_system[1:], list_number_x_in_pow)
                count_of_element += 1
            elif get_number_in_decimal_number_system(number_in_binary_system[0:count_of_element] == i):
                check_for_number_in_pow(number_in_binary_system[count_of_element:], list_number_x_in_pow)
                count_of_element += 1


def get_generated_answer_str_when_all_number_found(list_of_part_of_number_in_binary):
    list_of_part_of_number_in_binary_str = ''
    for part_of_number_in_binary in list_of_part_of_number_in_binary:
        list_of_part_of_number_in_binary_str += str(part_of_number_in_binary.get('number_in_binary_system')
                                                    + '(' + str(get_number_in_decimal_number_system(part_of_number_in_binary.get('number_in_binary_system'))) + ')')
        if part_of_number_in_binary == list_of_part_of_number_in_binary[-1]:
            return str(len(
                list_of_part_of_number_in_binary)) + '\n(Можна розбити на ' + list_of_part_of_number_in_binary_str + ')'
        else:
            list_of_part_of_number_in_binary_str += ', '


list_of_part_of_number_in_binary = []


def get_smallest_number_of_pieces(number_in_binary_system, number_x, list_number_x_in_pow,
                                  length_number_in_binary_system, start_position):
    print('Рекурсія')
    print(list_of_part_of_number_in_binary)

    count_iteration = 0
    list_of_found_binary_number_in_current_recursion = []
    for i in range(len(number_in_binary_system[start_position:])):

        item_of_number_in_binary_system = number_in_binary_system[start_position:start_position + i + 1]
        item_of_number_in_decimal_system = get_number_in_decimal_number_system(item_of_number_in_binary_system)
        count_iteration += 1
        print('item_of_number_in_binary_system = ' + str(item_of_number_in_binary_system + ' !'))

        if item_of_number_in_decimal_system in list_number_x_in_pow:
            list_of_found_binary_number_in_current_recursion.append({
                "number_in_binary_system": item_of_number_in_binary_system,
                "last_position_in_initial_number": start_position + count_iteration})

    if not list_of_found_binary_number_in_current_recursion:
        print("Дане двійкове число неможна розділити так щоб в усіх розділених частинах було число " + str(
            number_x) + " в якійсь степені")
        return -1

    else:
        list_of_part_of_number_in_binary.append(list_of_found_binary_number_in_current_recursion[-1])

        last_position_in_binary_system = list_of_found_binary_number_in_current_recursion[-1].get(
            "last_position_in_initial_number")
        if last_position_in_binary_system < length_number_in_binary_system:
            print('last_position_in_binary_system = ' + str(last_position_in_binary_system)
                  + '\nlength_number_in_binary_system = ' + str(length_number_in_binary_system))
            return get_smallest_number_of_pieces(number_in_binary_system, number_X, list_number_x_in_pow,
                                                 length_number_in_binary_system, last_position_in_binary_system)

        else:
            print("Всю стрічку з числом в двійковій системі числення пройдено")
            return get_generated_answer_str_when_all_number_found(list_of_part_of_number_in_binary)


if __name__ == '__main__':
    in_data = '101101101 5'
    number_in_binary_system = in_data.split(' ')[0]
    number_X = int(in_data.split(' ')[1])
    number_in_decimal_number_system = get_number_in_decimal_number_system(number_in_binary_system)
    list_number_x_in_pow = get_list_number_x_in_pow(number_X, number_in_decimal_number_system)

    print(number_in_decimal_number_system)
    print(list_number_x_in_pow)

    print(get_smallest_number_of_pieces(number_in_binary_system, number_X, list_number_x_in_pow,
                                        len(number_in_binary_system), 0))