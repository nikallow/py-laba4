from src.player import Player


class PlayerCollection:
    def __init__(self):
        self._players: list[Player] = []

    def add(self, player: Player) -> None:
        """
        Добавляет игрока в коллекцию.

        :param player: Объект игрока
        :type player: Player
        :return: None
        """
        if player in self._players:
            raise ValueError(f"Игрок уже в коллекции: {player.name}")
        self._players.append(player)

    def alive(self) -> list[Player]:
        """
        Возвращает список живых игроков

        :return: Список живых игроков
        :rtype: list[Player]
        """
        return [p for p in self._players if p.is_alive()]

    def __iter__(self):
        return iter(self._players)

    def __len__(self):
        return len(self._players)

    def __getitem__(self, index):
        return self._players[index]

    def __repr__(self):
        lines = ["Player Collection: "]
        for player in self._players:
            lines.append(repr(player))
        return "\n".join(lines)
