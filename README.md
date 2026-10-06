# Algorithms and Data Structures

Реализация классических структур данных и алгоритмов сортировки на Python.

## Структуры данных

- **Array** — динамический массив с авторасширением
- **LinkedList** — односвязный список
- **Deque** — дек на двусвязном списке
- **AVLTree** — самобалансирующееся бинарное дерево поиска

## Сортировки

- **Bubble Sort** — сортировка пузырьком
- **Quick Sort** — быстрая сортировка (in-place, схема Ломуто)

## Установка

```bash
pip install -r requirements.txt
python3 -m pytest
cat > .github/workflows/ci.yml << 'EOF'
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12"]

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: |
          pytest
