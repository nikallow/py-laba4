class Player:
    def __init__(self, name: str, balance: int):
        """
        Игрок

        :param name: Имя игрока
        :param balance: Начальный баланс
        """
        self.name = name
        self.balance = balance
        self.panic_level = 0
        self.is_dead = False

    def adjust_panic(self, value: int) -> None:
        """
        Изменяет уровень тревожности игрока.

        :param value: Изменение тревожности
        :returns: None
        """
        self.panic_level = max(0, min(20, self.panic_level + value))

    def take_money(self, amount: int) -> int:
        """
        Забирает деньги у игрока.
        Если деньги заканчиваются — игрок умирает.

        :param amount: Запрашиваемая сумма
        :returns: Фактически забранная сумма
        """
        stolen = min(self.balance, amount)
        self.balance -= stolen

        if self.balance == 0:
            self.is_dead = True
            print(f"{self.name} умер")

        return stolen

    def lose_chance(self) -> float:
        """
        Шанс проигрыша ставки.

        :returns: Вероятность проигрыша
        """
        return 0.6 + self.panic_level * 0.02

    def __eq__(self, other):
        return isinstance(other, Player) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self) -> str:
        return (
            f"Player({self.name}, balance={self.balance}, "
            f"panic={self.panic_level}, dead={self.is_dead}"
        )
