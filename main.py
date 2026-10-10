import random
import time

from sorts import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort

methods = [
    ("Пузырьком", bubble_sort),
    ("Выбором", selection_sort),
    ("Вставками", insertion_sort),
    ("Слиянием", merge_sort),
    ("Быстрая", quick_sort),
]

data = [random.randint(0, 1000) for _ in range(2000)]
right = sorted(data)

for name, func in methods:
    start = time.time()
    result = func(data)
    t = time.time() - start
    ok = "ок" if result == right else "ОШИБКА"
    print(f"{name:12} {t:.4f} сек  {ok}")
