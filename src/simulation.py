from src.casino import Casino
from src.constants import RNG
from src.goose import Goose, HonkGoose, WarGoose
from src.player import Player


def gen_players(amount: int = 20) -> list[Player]:
    lst = []
    for i in range(amount):
        lst.append(Player(f"Player{i}", RNG.randint(1, 200)))
    return lst


def gen_gooses(amount: int = 20) -> list[Goose]:
    lst = []
    for i in range(amount):
        goose_type = RNG.choice([WarGoose, HonkGoose])
        lst.append(goose_type(f"Goose{i}", RNG.randint(1, 10)))
    return lst


def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    """
    Запускает симуляцию казино.

    :param steps: Количество шагов
    :type steps: int
    :param seed: Seed генератора случайных чисел
    :type seed: int | None
    """
    if seed is not None:
        RNG.seed(seed)

    casino = Casino()

    for player in gen_players():
        casino.register_player(player)

    for goose in gen_gooses():
        casino.register_goose(goose)

    events = [
        casino.goose_attack,
        casino.goose_honk,
        casino.ocg_attack,
        casino.ocg_honk,
        casino.form_ocg,
        casino.casino_interaction,
    ]

    for step in range(steps):
        if not casino.players.alive():
            print("Все игроки мертвы! Симуляция завершена.")
            break

        print(f"\n--- STEP {step + 1} ---")
        RNG.choice(events)()
