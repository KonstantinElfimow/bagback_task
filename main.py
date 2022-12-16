from datetime import datetime
import bagpack_task
from item import Item


def main():
    suffix: int = 1
    # Читаем файл
    file_input = open(f'./input/input_{suffix}.txt', 'r')
    # Создаём массив непустых строк из файла
    lines = file_input.read().splitlines()
    # Закрываем файл
    file_input.close()

    # Создаём пустой список и добавляем новый Item
    items = []
    for line in lines[1:-1]:
        words = line.split(' ')
        if int(words[0]) <= 0 or int(words[1]) <= 0:
            raise ValueError("Записывайте только положительные значения")
        item: Item = Item(int(words[0]), int(words[1]))
        items.append(item)
    items = tuple(items)

    # Общая вместимость
    W: int = int(lines[-1].split('W=')[1])

    start = datetime.now()
    value_lists: dict = bagpack_task.solution(items, W)
    end = datetime.now()
    # Время, потраченное на поиск решения
    print(end - start)
    # Запись результата в файл
    file_output = open(f'./output/output_{suffix}.txt', 'w')
    optimal_value: str = ''.join([str(x) for x in value_lists.keys()])
    optimal_solution: str = ''.join([str(x) for x in value_lists.values()])
    file_output.write('Оптимальное значение:\n'
                      '{}\n'
                      'Оптимальное решение (списки порядковых номеров Items):\n'
                      '{}'.format(optimal_value, optimal_solution))
    file_output.close()


if __name__ == '__main__':
    main()
