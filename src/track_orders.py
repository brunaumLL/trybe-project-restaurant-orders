from src.analyze_log import organizer_list, most_orded, busiest_day
from src.analyze_log import never_orded, days_never_visited, least_busy_day


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        list = organizer_list(self.orders)
        most_ordered = most_orded(list, customer)
        return most_ordered

    def get_never_ordered_per_customer(self, customer):
        list = organizer_list(self.orders)
        never_ordered = never_orded(list, customer)
        return never_ordered

    def get_days_never_visited_per_customer(self, customer):
        list = organizer_list(self.orders)
        never_visited = days_never_visited(list, customer)
        return never_visited

    def get_busiest_day(self):
        list = organizer_list(self.orders)
        most_visited = busiest_day(list)
        return most_visited

    def get_least_busy_day(self):
        list = organizer_list(self.orders)
        least_visited = least_busy_day(list)
        return least_visited
