from constants import parameters, number_of_parameters as n


def bool_to_int(score):
    return int(score, 2)


def list_to_score(my_list):
    score = ""
    for x in parameters:
        if x in my_list:
            score += "1"
        else:
            score += "0"

    return bool_to_int(score)


def score_to_list(score):
    bin_format = '{0:0' + n + 'b}'
    my_bin = bin_format.format(score)

    my_list = []
    for index, x in enumerate(my_bin):
        if x == '1':
            my_list.append(parameters[index])

    return my_list
