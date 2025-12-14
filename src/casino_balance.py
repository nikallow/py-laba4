from src.chip import Chip
from src.player import Player


class CasinoBalance:
    """
    Словарная коллекция фишек игроков казино.

    Ключ — Player
    Значение — Chip
    """

    def __init__(self):
        self._balances: dict[Player, Chip] = {}

    def register_player(self, player: Player) -> None:
        """
        Регистрирует игрока с нулевым количеством фишек.

        :param player: Игрок
        """
        self._balances[player] = Chip(0)
        print(f"Фишки {player.name}: 0")

    def add(self, player: Player, amount: int) -> None:
        """
        Добавляет фишки игроку.

        :param player: Игрок
        :param amount: Количество фишек
        """
        self[player] = self[player] + Chip(amount)

    def reset(self, player: Player) -> None:
        """
        Обнуляет количество фишек игрока.

        :param player: Игрок
        """
        self[player] = Chip(0)

    def __getitem__(self, player: Player) -> Chip:
        """
        Возвращает фишки игрока.

        :param player: Игрок
        :raises KeyError: Если игрок не зарегистрирован
        :returns: Фишки игрока
        """
        if player not in self._balances:
            raise KeyError(f"Игрок {player.name} не зарегистрирован")

        return self._balances[player]

    def __setitem__(self, player: Player, chips: Chip) -> None:
        """
        Устанавливает количество фишек игрока.

        :param player: Игрок
        :param chips: Фишки
        :raises KeyError: Если игрок не зарегистрирован
        :returns: None
        """
        if player not in self._balances:
            raise KeyError(f"Игрок {player.name} не зарегистрирован")

        old = self._balances.get(player, Chip(0))
        self._balances[player] = chips
        print(f"Фишки {player.name}: {old.value} -> {chips.value}")

    def __iter__(self):
        return iter(self._balances)

    def __len__(self) -> int:
        return len(self._balances)

    def __repr__(self) -> str:
        lines = ["Casino chips balance:"]
        for player, chips in self._balances.items():
            lines.append(f"\t{player.name}: {chips.value}")
        return "\n".join(lines)
