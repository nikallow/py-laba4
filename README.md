# Лаба по Python №4 "Гуси, ОПГ и казино"

## Установка и запуск
```bash
uv venv

source .venv/bin/activate # Для Linux/MacOS
source .venv\Scripts\activate # Для Windows

uv sync
```
```bash
uv run -m src.main --steps <int> --seed <int>
```
* steps - количество шагов симуляции
* seed - сид (логично)

## Тесты
```bash
uv run pytest
```

# Что да как
```
.
├── README.md
├── pyproject.toml
├── src
│   ├── __init__.py
│   ├── casino.py # Класс казино, регестрации, взаимодействия
│   ├── casino_balance.py # Коллекция фишек aka баланс игроков
│   ├── chip.py # Класс фишек
│   ├── constants.py # RNG
│   ├── goose.py # Базовый, кричащйи и боевой гуси
│   ├── goose_collections.py # Коллекция гусей
│   ├── goose_income.py # Коллекция доходов гусей
│   ├── goose_ocg.py # ОПГ гусей
│   ├── main.py
│   ├── player.py # Класс игрока
│   ├── player_collection.py # Коллекция игроков
│   └── simulation.py # Запуск симуляции
├── tests
│   ├── __init__.py
│   ├── test_casino_balance.py
│   ├── test_goose.py
│   ├── test_goose_collection.py
│   ├── test_goose_income.py
│   ├── test_goose_ocg.py
│   ├── test_player.py
│   └── test_player_collection.py
└── uv.lock
```
# Действия симуляции:
1. Взаимодействие игрока с казино:
    - Нет фишек - деп и крутка
    - Есть фишки - додеп и крутка
    - Есть фишки - крутка
    - Есть фишки - вывод с казика
2. Гусь кричит (1 lvl крика = +1 lvl паники)
3. Гусь атакует (5% * lvl силы + 2% * lvl паники игрока)
4. ОПГ кричит (80%, что это сделает 1 из гусей)
5. ОПГ атакует (80, что это сделает 1 из гусей)

Игрок умирает, если на балансе 0 осталось после атаки гуся (гусь решил пожалеть и убил)
ОПГ могут устроить стычку между собой

P.S. вышел за дедлайн
