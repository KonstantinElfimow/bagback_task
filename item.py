class Item:
    __number: int = 0

    @classmethod
    def __set_number__(cls):
        cls.__number += 1
        return cls.__number

    def __init__(self, weight: int, value: int):
        self.weight = weight
        self.value = value
        self.count = Item.__set_number__()

    def get_weight(self):
        return self.weight

    def get_value(self):
        return self.value

    def get_count(self):
        return self.count

    @staticmethod
    def sum_of_weights(items: list) -> int:
        if items:
            for item in items:
                if not isinstance(item, Item):
                    raise ValueError("Передавайте только объекты типа Item!")
            return sum([item.get_weight() for item in items])
        else:
            return 0

    @staticmethod
    def sum_of_values(items: list) -> int:
        if items:
            for item in items:
                if not isinstance(item, Item):
                    raise ValueError("Передавайте только объекты типа Item!")
            return sum([item.get_value() for item in items])
        else:
            return 0

    def __str__(self) -> str:
        return 'weight={}, value={}'.format(self.weight, self.value)
