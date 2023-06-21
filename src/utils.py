import csv


def open_file():
    with open("items.csv", "r", encoding="windows-1251") as f:
        reader = csv.reader(f)
        list_of = [row for row in reader]
        items_list = list_of[1:]
        return items_list


class REWQ:
    def __init__(self, n, p, q):
        self.n = n
        self.p = p
        self.q = q

    def ass(self):
        return f"{self.n}   {self.p}"


items = [REWQ(el[0], el[1], el[2]) for el in open_file()]



