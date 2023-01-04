import csv
from statistics import multimode


def analyze_log(path_to_file):
    if '.csv' not in path_to_file:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file) as file:
            file_inf = csv.reader(file)
            data = [item for item in file_inf]
            list = organizer_list(data)
            mrm = most_requsted_maria(list)
            ttar = times_that_arnaldo_requested(list)
            jno = joao_never_order(list)
            jngtsb = joao_never_go_to_snack_bar(list)
            save_analyze(mrm, ttar, jno, jngtsb)
    except FileNotFoundError:
        raise FileNotFoundError(f'Arquivo inexistente. {path_to_file}')


def organizer_list(data):
    list = []
    for client, order, day in data:
        obj = {
            'client': client,
            'order': order,
            'day': day
        }
        list.append(obj)
    return list


def most_requsted_maria(list):
    maria_order = []
    for obj in list:
        if obj['client'] == 'maria':
            maria_order.append(obj['order'])
    most_requested = (multimode(maria_order))
    return most_requested[0]


def times_that_arnaldo_requested(list):
    arnaldo_request = []
    for obj in list:
        if obj['client'] == 'arnaldo':
            arnaldo_request.append(obj['order'])
    times_requested = arnaldo_request.count('hamburguer')
    return times_requested


def joao_never_order(list):
    joao_orders = []
    orders = []
    never_order = []
    for obj in list:
        orders.append(obj['order'])
        if obj['client'] == 'joao':
            joao_orders.append(obj['order'])

    for order in orders:
        if order not in joao_orders:
            never_order.append(order)
    return set(never_order)


def joao_never_go_to_snack_bar(list):
    joao_go = []
    days = []
    never_go = []
    for obj in list:
        days.append(obj['day'])
        if obj['client'] == 'joao':
            joao_go.append(obj['day'])

    for day in days:
        if day not in joao_go:
            never_go.append(day)
    return set(never_go)


def save_analyze(mrm, ttar, jno, jngtsb):
    with open('data/mkt_campaign.txt', 'w') as file:
        analyze = (f'{mrm}\n{ttar}\n{jno}\n{jngtsb}')
        print(analyze)
        file.write(analyze)
