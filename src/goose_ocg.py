from src.constants import RNG
from src.goose import Goose, HonkGoose, WarGoose
from src.goose_collections import HonkGooseCollection, WarGooseCollection
from src.player import Player


class GooseOCG:
    """
    Организованная преступная группа гусей.
    """

    def __init__(self):
        self.war_geese = WarGooseCollection()
        self.honk_geese = HonkGooseCollection()
        self.strongest_war: WarGoose | None = None
        self.loudest_honk: HonkGoose | None = None

    @classmethod
    def unite(cls, first: Goose, second: Goose) -> GooseOCG:
        """
        Объединяет гусей в ОПГ.

        :param first: Первый гусь (может быть одиночкой или состоять в ОПГ)
        :type first: Goose
        :param second: Второй гусь (обязан быть одиночкой)
        :type second: Goose
        :return: ОПГ, в которую в итоге входят гуси
        :raises ValueError:
            - если гуси совпадают
            - если второй гусь уже состоит в ОПГ
        """
        if first is second:
            raise ValueError("Нельзя объединить гуся с самим собой")

        # Второй гусь обязан быть одиночкой
        if second.ocg is not None:
            raise ValueError("Второй гусь уже состоит в ОПГ")

        # Если первый уже в ОПГ — добавляем второго
        if first.ocg is not None:
            first.ocg.add_goose(second)
            return first.ocg

        # Иначе создаём новую ОПГ
        ocg = cls()
        ocg.add_goose(first)
        ocg.add_goose(second)
        return ocg

    def add_goose(self, goose: Goose) -> None:
        """
        Добавляет гуся в ОПГ и переносит доход.

        :param goose: Гусь, добавляемый в ОПГ
        :type goose: Goose
        :raises ValueError: Если гусь уже состоит в другой ОПГ
        :returns: None
        """
        if goose.ocg is not None:
            raise ValueError("Гусь уже состоит в ОПГ")
        goose.ocg = self

        # Определяем тип гуся, кешируем лучших
        if isinstance(goose, WarGoose):
            self.war_geese.add(goose)
            if (
                self.strongest_war is None
                or goose.strength > self.strongest_war.strength
            ):
                self.strongest_war = goose

        elif isinstance(goose, HonkGoose):
            self.honk_geese.add(goose)
            if (
                self.loudest_honk is None
                or goose.honk_volume > self.loudest_honk.honk_volume
            ):
                self.loudest_honk = goose

        print(f"{goose} вступил в ОПГ")

    def attack(self, player: Player) -> int:
        """
        ОПГ атакует игрока.

        :param player: Игрок
        :type player: Player
        :returns: Украденные деньги
        """
        if player.is_dead or self.war_geese.total_strength == 0:
            return 0

        # Шанс 80%, что будет атаковать 1 гусь
        if self.strongest_war and RNG.random() < 0.8:
            return self.strongest_war.attack(player)
        else:
            stolen = 0
            for goose in self.war_geese:
                if player.is_dead:
                    break
                stolen += goose.attack(player)
            return stolen

    def honk(self, player: Player) -> None:
        """
        ОПГ кричит на игрока.

        :param player: Игрок
        :type player: Player
        :returns: None
        """

        # Шанс 80%, что кричать будет только 1 гусь
        if self.loudest_honk and RNG.random() < 0.8:
            self.loudest_honk.honk(player)
        else:
            for goose in self.honk_geese:
                goose.honk(player)

    def fight(self, other: GooseOCG) -> tuple[GooseOCG, GooseOCG]:
        """
        Схватка двух ОПГ.

        Побеждает ОПГ с большей суммарной силой.
        Банк проигравшей ОПГ переходит победителю.

        :param other: Другая ОПГ
        :type other: GooseOCG
        :returns: Победившая ОПГ
        """
        self_strength = self.war_geese.total_strength
        other_strength = other.war_geese.total_strength

        winner = self if self_strength >= other_strength else other
        loser = other if winner is self else self

        print(f"{winner} победила {loser}")

        return winner, loser

    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        return self is other

    def __repr__(self) -> str:
        return "ОПГ гусей"
