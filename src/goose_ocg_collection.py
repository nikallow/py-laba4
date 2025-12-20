from collections.abc import Iterator

from src.goose_ocg import GooseOCG


class GooseOCGCollection:
    """
    Коллекция ОПГ гусей
    """

    def __init__(self) -> None:
        self._ocg: list[GooseOCG] = []

    def add(self, ocg: GooseOCG) -> None:
        """
        Добавляет ОПГ в коллекцию.

        :param ocg: Объект ОПГ
        :type ocg: GooseOCG
        :return: None
        """
        if not isinstance(ocg, GooseOCG):
            raise TypeError("Можно добавлять только ОПГ гусей")
        self._ocg.append(ocg)

    def remove(self, ocg: GooseOCG) -> None:
        """
        Удаляет ОПГ из коллекции

        :param ocg: Объект ОПГ
        :type ocg: GooseOCG
        :return: None
        """
        if not isinstance(ocg, GooseOCG):
            raise TypeError("Можно удалять только ОПГ гусей")
        self._ocg.remove(ocg)

    def __iter__(self) -> Iterator[GooseOCG]:
        return iter(self._ocg)

    def __len__(self) -> int:
        return len(self._ocg)

    def __getitem__(self, index: int | slice) -> GooseOCG | list[GooseOCG]:
        return self._ocg[index]

    def __repr__(self):
        lines = ["Goose OCGs:"]
        for ocg in self._ocg:
            lines.append(repr(ocg))
        return "\n".join(lines)
