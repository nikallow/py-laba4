from typing import TYPE_CHECKING

from src.player import Player

if TYPE_CHECKING:
    from src.goose_ocg import GooseOCG


class Goose:
    """
    Базовый гусь.
    """

    def __init__(self, name: str):
        """
        Создаёт базового гуся.

        :param name: Имя гуся
        """
        self.name = name
        self.ocg: GooseOCG | None = None

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}) in OCG({self.ocg})"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return isinstance(other, Goose) and self.name == other.name


class HonkGoose(Goose):
    def __init__(self, name: str, honk_volume: int):
        """
        Кричащий гусь.
        """
        super().__init__(name)
        self.honk_volume = honk_volume

    def honk(self, player: Player) -> None:
        """
        Увеличивает тревожность игрока.

        :param player: Игрок
        :returns: None
        """
        before = player.panic_level
        player.adjust_panic(self.honk_volume)

        print(f"{self} накричал на {player.name}: {before} -> {player.panic_level}")


class WarGoose(Goose):
    def __init__(self, name: str, strength: int):
        """
        Боевой гусь.
        """
        super().__init__(name)
        self.strength = strength

    def attack(self, player: Player) -> int:
        """
        Отбирает деньги у игрока.

        :param player: Игрок
        :returns: Сумму украденных денег
        """
        percent = min(100, self.strength * 5 + player.panic_level * 2)
        amount = int(player.balance * percent / 100)
        stolen = player.steal_money(amount)
        print(
            f"{self} отжал {stolen} у {player.name} (баланс игрока: {player.balance})"
        )
        return stolen
