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

    def _change_balance(self, delta: int) -> int:
        """
        Изменяет баланс игрока

        :param delta: Запрашиваемое изменение баланса
        :type delta: int
        :return: Фактически изменённая сумма
        :rtype: int
        """
        old_balance = self.balance

        if delta < 0:
            delta = min(self.balance, -delta)
            self.balance -= delta
        else:
            self.balance += delta

        print(f"Баланс игрока {self.name} поменялся:  {old_balance} -> {self.balance}")

        return delta

    def pay(self, amount: int) -> int:
        """
        Покупка фишек
        :param amount: Сумма покупки
        :type amount: int
        :returns: Фактическая сумма покупки
        :rtype: int
        """
        return self._change_balance(-amount)

    def receive_money(self, amount: int) -> None:
        """
        Получение денег
        :param amount: Сумма
        :type amount: int
        :returns: None
        """
        self._change_balance(amount)

    def steal_money(self, amount: int) -> int:
        """
        Ворует деньги у игрока.
        Если деньги заканчиваются — игрок умирает.

        :param amount: Запрашиваемая сумма
        :returns: Фактически забранная сумма
        """
        stolen = self._change_balance(-amount)

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

    def is_alive(self) -> bool:
        return not self.is_dead

    def can_pay(self):
        return self.balance > 0

    def __eq__(self, other):
        return isinstance(other, Player) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self) -> str:
        return (
            f"Player({self.name}, balance={self.balance}, "
            f"panic={self.panic_level}, dead={self.is_dead}"
        )
