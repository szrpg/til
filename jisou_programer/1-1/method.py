import csv


def read_items():
    """CSVのジェネレータを返す
    (商品, 価格)のタプル
    """
    with open(...) as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[0]
            price = int(row[1])
            yield name, price