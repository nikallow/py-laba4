from src.goose import Goose
from src.goose_ocg import GooseOCG


class GooseIncome:
    """
    Словарная коллекция доходов гусей и ОПГ.

    Ключ: Одиночный гусь или ОПГ гусей
    Значение: int — накопленный доход
    """

    def __init__(self) -> None:
        self._income: dict[Goose | GooseOCG, int] = {}

    def __getitem__(self, owner: Goose | GooseOCG) -> int:
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

    def __setitem__(self, owner: Goose | GooseOCG, value: int) -> None:
        """
        Устанавливает доход владельца.

        :param owner: Гусь или ОПГ
        :type owner: Goose | OCG
        :param value: Новое значение дохода
        :type value: int
        """
        self._income[owner] = value

    def add(self, owner: Goose | GooseOCG, amount: int) -> None:
        """
        Добавляет доход владельцу.

        :param owner: Гусь или ОПГ
        :type owner: Goose | OCG
        :param amount: Сумма дохода
        :type amount: int
        """
        self[owner] = self._income.get(owner, 0) + amount

    def pop(self, owner: Goose | GooseOCG) -> int:
        """
        Удаляет и возвращает доход владельца.

        :param owner: Гусь или ОПГ
        :type owner: Goose | OCG
        :return: Доход владельца или 0, если отсутствует
        :rtype: int
        """
        return self._income.pop(owner, 0)
