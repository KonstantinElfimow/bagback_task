from item import Item


def solution(items: tuple, W: int) -> dict:
    if not W:
        return {0: []}
    # Создаём словарь (оптимальное решение: списки предметов, дающих оптимальное решение)
    result: dict = {}
    # Начальная ценность положенных вещей - 0
    V: int = 0
    # Асимптотическая сложность алгоритма задачи о рюкзаке O(2 ** k),
    # тогда будет всего 2 ** k комбинаций
    for num in range(2 ** len(items)):
        # Бинарное число, начинающееся с младшего разряда, и размером в len(items)
        # Пример: len(items) == 4 и num == 1 => r_b = 1000
        r_b: str = '{:0{width}b}'.format(num, width=len(items))[::-1]
        # print(r_b)
        # Если r_b[0] == 1 => берём предмет №1 из списка. Если r_b[0] == 0 => не берём предмет №1 из списка. И т.д.
        used_items: list = [item for i, item in enumerate(items) if int(r_b[i]) == 1]
        # Допустимое решение?
        if Item.sum_of_weights(used_items) <= W:
            # Ценность положенных вещей
            sum_v: int = Item.sum_of_values(used_items)
            # Если ценность равна V, то добавляем в матрицу новых список предметов
            if sum_v == V:
                result.setdefault(V, []).append([x.get_count() for x in used_items])
            # иначе удаляем старое решение, если sum_v > V, и добавляем новое решение
            elif sum_v > V:
                del result[V]
                V = sum_v
                result.setdefault(V, []).append([x.get_count() for x in used_items])
        # print('Решение на данном шаге: {}; {}'.format(result, [x.get_count() for x in used_items]))
    # Возвращаем результат
    return result
