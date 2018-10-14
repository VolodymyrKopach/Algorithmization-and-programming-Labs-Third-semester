file = open('bugtrk.in.txt', 'r')
bugtrk_data_list = file.read().split(' ')
file.close()
print(bugtrk_data_list)


N = int(bugtrk_data_list[0])
W = int(bugtrk_data_list[1])
H = int(bugtrk_data_list[2])

filled_in_width = 0
filled_in_height = 0
size_of_side_of_square = 0
number_of_rows = 0
is_first_cycle = True

i = N
while i > 0:

    if filled_in_width + W <= filled_in_height + H:
        print('if: ' + str(filled_in_width + W) + ' ' + str(filled_in_height + H))

        filled_in_width += W
        if is_first_cycle:
            filled_in_height += H
            is_first_cycle = False

        i -= number_of_rows

        size_of_side_of_square = filled_in_width
        print('if:                    i = ' + str(i))

    else:
        print('else: ' + str(filled_in_width + W) + ' ' + str(filled_in_height + H))

        number_of_rows += 1

        filled_in_height += H
        if is_first_cycle:
            filled_in_width += W
            is_first_cycle = False

        if (i - (filled_in_width - W) / W) > 0:
            i -= (filled_in_width - W) / W
        else:
            i = 0

        size_of_side_of_square = filled_in_height
        print('else:                    i = ' + str(i))

    i -= 1

print(size_of_side_of_square)

my_file = open("bugtrk.out.txt", "w")
my_file.write(str(size_of_side_of_square))
my_file.close()
