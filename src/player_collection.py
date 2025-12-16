from src.player import Player


class PlayerCollection:
    def __init__(self):
        self._players: list[Player] = []

    def add(self, player: Player):
        if player in self._players:
            raise ValueError(f"Игрок уже в коллекции: {player.name}")
        self._players.append(player)

    def alive(self):
        return [p for p in self._players if p.is_alive()]

    def __iter__(self):
        return iter(self._players)

    def __len__(self):
        return len(self._players)

    def __getitem__(self, index):
        return self._players[index]
