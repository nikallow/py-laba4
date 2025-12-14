class Chip:
    """
    Фишки казино.
    """

    def __init__(self, value: int = 0):
        """
        Создаёт набор фишек.

        :param value: Количество фишек
        """
        if value < 0:
            raise ValueError("Значение фишки не может быть отрицательным")
        self.value = value

    def __add__(self, other: Chip) -> Chip:
        """
        Складывает фишки.

        :param other: Другие фишки
        :return: Новый объект Chip
        """
        if not isinstance(other, Chip):
            return NotImplemented
        return Chip(self.value + other.value)

    def __mul__(self, k: int) -> Chip:
        """
        Умножает количество фишек.

        :param k: Множитель
        :returns: Новый объект Chip
        """
        return Chip(self.value * k)

    def __bool__(self) -> bool:
        """
        Проверка наличия фишек.

        :returns: True если фишек больше нуля
        """
        return self.value > 0

    def __repr__(self) -> str:
        return f"Chip({self.value})"
