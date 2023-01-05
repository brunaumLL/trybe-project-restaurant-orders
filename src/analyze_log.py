import csv
from statistics import mode


def analyze_log(path_to_file):
    if '.csv' not in path_to_file:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file) as file:
            file_inf = csv.reader(file)
            data = [item for item in file_inf]
            list = organizer_list(data)
            mo = most_orded(list, "maria")
            to = times_orded(list, "arnaldo", "hamburguer")
            no = never_orded(list, "joao")
            dnv = days_never_visited(list, "joao")
            save_analyze(mo, to, no, dnv)
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


def most_orded(list, client):
    order = []
    for obj in list:
        if obj['client'] == client:
            order.append(obj['order'])
    most_requested = (mode(order))
    return most_requested


def times_orded(list, client, order):
    orded = []
    for obj in list:
        if obj['client'] == client:
            orded.append(obj['order'])
    times_orded = orded.count(order)
    return times_orded


def never_orded(list, client):
    orders = []
    all_orders = []
    never_order = []
    for obj in list:
        all_orders.append(obj['order'])
        if obj['client'] == client:
            orders.append(obj['order'])

    for order in all_orders:
        if order not in orders:
            never_order.append(order)
    return set(never_order)


def days_never_visited(list, client):
    days_visited = []
    days = []
    never_visited = []
    for obj in list:
        days.append(obj['day'])
        if obj['client'] == client:
            days_visited.append(obj['day'])

    for day in days:
        if day not in days_visited:
            never_visited.append(day)
    return set(never_visited)


def busiest_day(list):
    days_visited = []
    for obj in list:
        days_visited.append(obj['day'])
    most_visited = (mode(days_visited))
    return most_visited


def least_busy_day(list):
    days_visited = []
    for obj in list:
        days_visited.append(obj['day'])
    lst = days_visited[::-1]
    return min(lst, key=lst.count)


def save_analyze(mo, to, no, dnv):
    with open('data/mkt_campaign.txt', 'w') as file:
        analyze = (f'{mo}\n{to}\n{no}\n{dnv}')
        file.write(analyze)
