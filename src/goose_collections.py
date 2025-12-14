from collections.abc import Hashable, Iterator

from src.goose import Goose, HonkGoose, WarGoose


class GooseCollection:
    """
    Базовая коллекция гусей.

    Хранит базового гуся и его наследников.
    Поддерживает добавление, удаление и итерирование.
    """

    def __init__(self) -> None:
        self._geese: list[Goose] = []

    def add(self, goose: Goose) -> None:
        """
        Добавляет гуся в коллекцию.

        :param goose: Объект гуся
        :type goose: Goose
        :raises TypeError: Если объект не является гусем
        """
        if not isinstance(goose, Goose):
            raise TypeError("Можно добавлять только Goose")
        self._geese.append(goose)

    def remove(self, goose: Goose) -> None:
        """
        Удаляет гуся из коллекции.

        :param goose: Гусь
        :type goose: Goose
        :raises ValueError: Если гуся нет в коллекции
        """
        self._geese.remove(goose)

    def __add__(self, other: GooseCollection) -> GooseCollection:
        """
        Объединяет две коллекции гусей.

        :param other: Другая коллекция
        :type other: GooseCollection
        :return: Новая коллекция гусей
        :rtype: GooseCollection
        """
        if not isinstance(other, GooseCollection):
            return NotImplemented

        result = GooseCollection()
        result._geese = self._geese + other._geese
        return result

    def __iter__(self) -> Iterator[Goose]:
        """
        Возвращает итератор по гусям.

        :return: Итератор гусей
        :rtype: Iterator[Goose]
        """
        return iter(self._geese)

    def __len__(self) -> int:
        """
        Возвращает количество гусей в коллекции.

        :return: Количество гусей
        :rtype: int
        """
        return len(self._geese)

    def __getitem__(self, index: int | slice) -> Goose | list[Goose]:
        """
        Возвращает гуся по индексу или подсписок по срезу.

        :param index: Индекс или срез
        :type index: int | slice
        :return: Гусь или список гусей
        :rtype: Goose | list[Goose]
        """
        return self._geese[index]


class WarGooseCollection(GooseCollection):
    """
    Коллекция боевых гусей.

    Поддерживает кеширование суммарной боевой силы.
    """

    def __init__(self) -> None:
        super().__init__()
        self.total_strength: int = 0

    def add(self, goose) -> None:
        """
        Добавляет боевого гуся в коллекцию.

        :param goose: Боевой гусь
        :type goose: WarGoose
        :raises TypeError: Если объект не является WarGoose
        """
        if not isinstance(goose, WarGoose):
            raise TypeError("Можно добавлять только WarGoose")

        super().add(goose)
        self.total_strength += goose.strength

    def remove(self, goose) -> None:
        """
        Удаляет боевого гуся из коллекции.

        :param goose: Боевой гусь
        :type goose: WarGoose
        :raises TypeError: Если объект не является WarGoose
        """
        if not isinstance(goose, WarGoose):
            raise TypeError("Можно удалять только WarGoose")

        super().remove(goose)
        self.total_strength -= goose.strength


class HonkGooseCollection(GooseCollection):
    """
    Коллекция кричащих гусей.

    Поддерживает кеширование суммарной громкости крика.
    """

    def __init__(self) -> None:
        super().__init__()
        self.total_honk_volume: int = 0

    def add(self, goose) -> None:
        """
        Добавляет кричащего гуся в коллекцию.

        :param goose: Кричащий гусь
        :type goose: HonkGoose
        :raises TypeError: Если объект не является HonkGoose
        """
        if not isinstance(goose, HonkGoose):
            raise TypeError("Можно добавлять только HonkGoose")

        super().add(goose)
        self.total_honk_volume += goose.honk_volume

    def remove(self, goose) -> None:
        """
        Удаляет кричащего гуся из коллекции.

        :param goose: Кричащий гусь
        :type goose: HonkGoose
        :raises TypeError: Если объект не является HonkGoose
        """
        if not isinstance(goose, HonkGoose):
            raise TypeError("Можно удалять только HonkGoose")

        super().remove(goose)
        self.total_honk_volume -= goose.honk_volume


class GooseIncome:
    """
    Словарная коллекция доходов гусей и ОПГ.

    Ключ: Одиночный гусь или ОПГ гусей
    Значение: int — накопленный доход
    """

    def __init__(self) -> None:
        self._income: dict[Hashable, int] = {}

    def __getitem__(self, owner) -> int:
        """
        Возвращает доход владельца.

        :param owner: Гусь или ОПГ
        :type owner: Goose | OCG
        :raises KeyError: Если владелец отсутствует
        :return: Доход владельца
        :rtype: int
        """
        if owner not in self._income:
            raise KeyError(f"Неизвестный владелец: {owner}")
        return self._income[owner]

    def __setitem__(self, owner, value: int) -> None:
        """
        Устанавливает доход владельца.

        :param owner: Гусь или ОПГ
        :type owner: Goose | OCG
        :param value: Новое значение дохода
        :type value: int
        """
        self._income[owner] = value

    def add(self, owner, amount: int) -> None:
        """
        Добавляет доход владельцу.

        :param owner: Гусь или ОПГ
        :type owner: Goose | OCG
        :param amount: Сумма дохода
        :type amount: int
        """
        self[owner] = self._income.get(owner, 0) + amount

    def pop(self, owner) -> int:
        """
        Удаляет и возвращает доход владельца.

        :param owner: Гусь или ОПГ
        :type owner: Goose | OCG
        :return: Доход владельца или 0, если отсутствует
        :rtype: int
        """
        return self._income.pop(owner, 0)
