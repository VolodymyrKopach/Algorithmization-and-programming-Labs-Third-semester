def get_data_from_file(name_of_file):
    file = open(name_of_file, 'r')
    data_of_file = file.read()
    file.close()
    return data_of_file


def get_list_of_vertex(data_of_vertex):
    list_of_vertex = []
    for row_number in range(len(data_of_vertex.split(' ')[0])):
        list_of_vertex.append(row_number)

    return list_of_vertex


def get_list_of_related_employees(data_of_vertex):
    list_of_related_employees = []
    for row_number in data_of_vertex.split(' '):
        list_of_related_employee = []
        for i in range(len(row_number)):
            if row_number[i] == 'Y':
                list_of_related_employee.append(i)

        if not list_of_related_employee:
            list_of_related_employees.append([])
        else:
            list_of_related_employees.append(list_of_related_employee)

    return list_of_related_employees


def get_graph(list_of_vertex, list_of_related_certificates):
    graph = {}
    for i in range(len(list_of_vertex)):
        graph[list_of_vertex[i]] = list_of_related_certificates[i]

    return graph


def print_working_position(graph_of_employees):
        for employee in range(len(graph_of_employees)):
            if not graph_of_employees[employee]:
                print(str(employee) + " не є чиїмось менеджером")
            else:
                for subordinate_employee in graph_of_employees[employee]:
                    print(str(employee) + " є менеджером для " + str(subordinate_employee))


def print_salary_of_each_employee(graph_of_employees):
    for employee in range(len(graph_of_employees)):
        if not graph_of_employees[employee]:
            print("Зарплата працівника " + str(employee) + " є 1 (немає підлеглих)")
        else:
            count_of_subordinate_employee = 0
            for count_of_subordinate_employee in range(len(graph_of_employees[employee])):
                count_of_subordinate_employee += 1

            print("Зарплата працівника " + str(employee) + " є " + str(count_of_subordinate_employee) + " (менеджер)")


if __name__ == '__main__':
    data_of_matrix = get_data_from_file("in.txt")
    list_of_vertex = get_list_of_vertex(data_of_matrix)
    list_of_related_employees = get_list_of_related_employees(data_of_matrix)
    graph_of_employees = get_graph(list_of_vertex, list_of_related_employees)

    print_working_position(graph_of_employees)
    print_salary_of_each_employee(graph_of_employees)