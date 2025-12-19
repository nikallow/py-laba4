from src.casino_balance import CasinoBalance
from src.chip import Chip
from src.constants import RNG
from src.goose import Goose
from src.goose_collections import GooseCollection
from src.goose_income import GooseIncome
from src.goose_ocg import GooseOCG
from src.player import Player
from src.player_collection import PlayerCollection


class Casino:
    def __init__(self):
        """
        Казино.
        """
        self.players = PlayerCollection()
        self.balance = CasinoBalance()

        self.geese = GooseCollection()
        self.ocgs: list[GooseOCG] = []

        self.goose_income = GooseIncome()

    def register_player(self, player: Player) -> None:
        """
        Регистрирует игрока.

        :param player: Игрок
        :type player: Player
        :returns: None
        """
        self.players.add(player)
        print(f"Зарегистрирован игрок {player}")
        self.balance.register_player(player)

    def register_goose(self, goose: Goose) -> None:
        """
        Регистрирует одиночного гуся.

        :param goose: Гусь
        :type goose: Goose
        :returns: None
        """
        self.geese.add(goose)
        print(f"Зарегистрирован гусь {goose}")
        self.goose_income.add(goose, 0)

    def _spin(self, player: Player) -> None:
        """
        Выполняет крутку казино.

        :param player: Игрок
        :type player: Player
        :returns: None
        """
        chips = self.balance[player]

        if RNG.random() <= player.lose_chance():
            print(f"{player.name} проиграл {chips.value} фишек")
            self.balance.reset(player)
        else:
            self.balance[player] = chips * 2
            print(f"{player.name} выиграл! Фишек стало {self.balance[player].value}")

    def _interact_with_casino(self, player: Player) -> None:
        """
        Взаимодействие игрока с казино.

        WHAT:
            1. Если у игрока нет фишек — он покупает от 1 до balance
               и сразу крутит.
            2. Если фишки есть — случайно выбирается действие:
                - крутить казино
                - сделать додеп и крутить
                - обменять все фишки на деньги

        :param player: Игрок
        :type player: Player
        :returns: None
        """
        if not player.is_alive():
            print("Кто сюда труп притащил???")
            return

        if not player.can_pay():
            print("Пошёл вон, бомжара!")
            return

        chips = self.balance[player]

        # 1. Нет фишек — покупка + крутка
        if not chips:
            print(f"{player.name} купил фишки")
            amount = RNG.randint(1, player.balance)

            paid = player.pay(amount)
            if paid == 0:
                return
            self.balance[player] = Chip(paid)

            self._spin(player)
            return

        # 2. Если есть фишки
        action = RNG.randint(1, 3)

        # 2.1. Крутить
        if action == 1:
            self._spin(player)

        # 2.2. Додеп + крутка
        elif action == 2:
            f"{player.name} сделал додеп:"
            add = RNG.randint(0, player.balance)

            paid = player.pay(add)
            if paid > 0:
                self.balance[player] = chips + Chip(paid)

                print(f"(Фишки: {self.balance[player].value}) ")

            self._spin(player)

        # 2.3. Обмен всех фишек на деньги
        elif action == 3:
            print(f"{player.name} обменял {chips.value} фишек на деньги")
            player.receive_money(chips.value)
            self.balance.reset(player)

    def form_ocg(self) -> None:
        """
        Формирует ОПГ из двух гусей.
        """
        # second — строго из одиночек
        free_geese = [g for g in self.geese if g.ocg is None]
        if not free_geese:
            print("Все гуси разбежались по ОПГ")
            return
        second = RNG.choice(free_geese)

        # first — любой гусь, кроме second
        possible_first = [g for g in self.geese if g is not second]
        if not possible_first:
            print("Недостаточно гусей для формирования ОПГ")
            return
        first = RNG.choice(possible_first)

        ocg = GooseOCG.unite(first, second)
        if ocg not in self.ocgs:
            self.ocgs.append(ocg)

    def goose_attack(self) -> None:
        """
        Атака одиночного гуся.
        """
        war_geese = [g for g in self.geese if hasattr(g, "attack")]
        players = self.players.alive()

        if not players:
            print("Все игроки мертвы...")
            return

        if not war_geese:
            print("Служба по отлову гусей отловила всех кусачих")
            return

        goose = RNG.choice(war_geese)
        player = RNG.choice(players)

        stolen = goose.attack(player)
        owner = goose.ocg if goose.ocg else goose
        self.goose_income.add(owner, stolen)

    def goose_honk(self) -> None:
        """
        Крик одиночного гуся.
        """
        honk_geese = [g for g in self.geese if hasattr(g, "honk")]
        players = self.players.alive()

        if not players:
            print("Все игроки мертвы...")
            return

        if not honk_geese:
            print("Служба по отлову гусей отловила всех кричащих")
            return

        RNG.choice(honk_geese).honk(RNG.choice(players))

    def ocg_attack(self) -> None:
        """
        Атака ОПГ.
        """
        if not self.ocgs:
            print("Они что-то замышляют...")
            return

        players = self.players.alive()
        if not players:
            print("Все игроки мертвы...")
            return

        ocg = RNG.choice(self.ocgs)
        player = RNG.choice(players)

        stolen = ocg.attack(player)
        self.goose_income.add(ocg, stolen)

    def ocg_honk(self) -> None:
        """
        Крик ОПГ.
        """
        if not self.ocgs:
            print("Они что-то замышляют...")
            return

        players = self.players.alive()
        if not players:
            print("Все игроки мертвы...")
            return

        RNG.choice(self.ocgs).honk(RNG.choice(players))

    def ocg_fight(self) -> None:
        """
        Драка ОПГ между собой.
        """
        if len(self.ocgs) < 2:
            print("Шоу не будет. ОПГ не встретились")
            return

        a, b = RNG.sample(self.ocgs, 2)
        winner, loser = a.fight(b)

        # Переносим доход проигравшей ОПГ к победителю
        income = self.goose_income.pop(loser)
        self.goose_income.add(winner, income)

    def casino_interaction(self) -> None:
        """
        Случайное взаимодействие одного игрока с казино.
        """
        players = self.players.alive()
        if not players:
            return

        player = RNG.choice(players)
        self._interact_with_casino(player)
