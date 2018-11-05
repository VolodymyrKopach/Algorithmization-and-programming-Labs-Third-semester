def read_data_from_file_with_certificates(name_of_file):
    file = open(name_of_file, 'r')
    govern_data = file.read()
    file.close()
    return govern_data


def write_data_to_file(data, name_of_file):
    file = open(name_of_file, 'w')
    for name_of_certificate in data:
        file.write(name_of_certificate + "\n")


def get_finish_vertex(graph):
    for i in graph:
        if graph[i] == '':
            return i


def get_start_vertex(graph):
    set_of_related_sertificate = set()
    for i in graph.keys():
        if type(graph[i]) == list:
            for k in graph[i]:
                set_of_related_sertificate.add(k)
        else:
            set_of_related_sertificate.add(graph[i])

    result = list(set(graph.keys()) - set_of_related_sertificate)[0]
    return result


def get_list_of_vertex(govern_data):
    list_of_vertex = []

    for related_certificates in govern_data.split('\n'):
        certificate = related_certificates.split(' ')[0]
        previous_certificate = related_certificates.split(' ')[1]

        if certificate not in list_of_vertex:
            list_of_vertex.append(certificate)

        if previous_certificate not in list_of_vertex:
            list_of_vertex.append(previous_certificate)

    return list_of_vertex


def get_list_of_related_certificates(list_of_vertex, govern_data):
    list_of_related_certificates = []
    for vertex in list_of_vertex:
        list_of_related_certificate = []

        for related_certificates in govern_data.split('\n'):
            certificate = related_certificates.split(' ')[0]
            previous_certificate = related_certificates.split(' ')[1]
            if vertex == previous_certificate:
                list_of_related_certificate.append(certificate)

        if not list_of_related_certificate:
            list_of_related_certificates.append('')
        else:
            list_of_related_certificates.append(list_of_related_certificate)

    return list_of_related_certificates


def get_dict_of_marks(list_of_vertex):
    dict_of_marks = {}
    for i in list_of_vertex:
        dict_of_marks[i] = 0

    return dict_of_marks


def get_graph(list_of_vertex, list_of_related_certificates):
    graph = {}
    for i in range(len(list_of_vertex)):
        graph[list_of_vertex[i]] = list_of_related_certificates[i]

    return graph


def dfs(current_vertex, list_of_vertex, dict_of_marks, graph, path):
    dict_of_marks[current_vertex] = 2
    path.append(current_vertex)

    for w in graph.get(current_vertex):
        if dict_of_marks[w] != 2:
            dfs(w, list_of_vertex, dict_of_marks, graph, path)


if __name__ == '__main__':
    govern_data = read_data_from_file_with_certificates('govern.in.txt')
    path = []
    list_of_vertex = get_list_of_vertex(govern_data)
    list_of_related_certificates = get_list_of_related_certificates(list_of_vertex, govern_data)
    dict_of_marks = get_dict_of_marks(list_of_vertex)
    graph = get_graph(list_of_vertex, list_of_related_certificates)
    finish_vertex = get_finish_vertex(graph)
    start_vertex = get_start_vertex(graph)

    dfs(start_vertex, list_of_vertex, dict_of_marks, graph, path)

    print(list_of_vertex)
    print(list_of_related_certificates)
    print(get_finish_vertex(graph))
    print(get_start_vertex(graph))

    path.remove(finish_vertex)
    path.append(finish_vertex)

    print(path)

    write_data_to_file(path, "govern.out.txt")



