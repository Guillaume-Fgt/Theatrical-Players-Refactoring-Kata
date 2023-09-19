import math
from dataclasses import dataclass


AMOUNT_PER_TYPE = {
    "tragedy": {
        "base": 40000,
        "audience_bonus": 1000,
        "audience_threshold": 30,
        "audience_base": 0,
    },
    "comedy": {
        "base": 40000,
        "audience_bonus": 500,
        "audience_threshold": 20,
        "audience_base": 300,
    },
    "drama": {
        "base": 30000,
        "audience_bonus": 400,
        "audience_threshold": 10,
        "audience_base": 100,
    },
    "thriller": {
        "base": 25000,
        "audience_bonus": 200,
        "audience_threshold": 10,
        "audience_base": 200,
    },
}


def format_as_dollars(amount):
    return f"${amount:0,.2f}"


@dataclass
class Play:
    customer: str
    playID: str
    audience: int
    name: str
    type: str
    volume_credits: int = 0

    def calc_amount_invoice(self, play_parameters: dict[str, int]) -> int:
        base, aud_bonus, aud_threshold, aud_base = play_parameters.values()
        return (
            base
            + aud_bonus * (max(self.audience, aud_threshold) - aud_threshold)
            + aud_base * self.audience
        )

    def get_parameters(self) -> dict[str, int]:
        parameters = AMOUNT_PER_TYPE.get(self.type)
        if not parameters:
            raise ValueError(f"unknown type: {self.type}")
        return parameters

    def calculate_volume_credits(self) -> int:
        self.volume_credits += max(self.audience - 30, 0)
        if "comedy" == self.type:
            self.volume_credits += math.floor(self.audience / 5)
        return self.volume_credits

    def print_play(self):
        return (
            f" {self.name}:"
            f" {format_as_dollars(self.calc_amount_invoice(self.get_parameters())/100)} ({self.audience} seats)\n"
        )


def construct_play(invoices: dict, plays: dict):
    for perf in invoices["performances"]:
        perf["customer"] = invoices["customer"]
        perf["name"] = plays[perf["playID"]]["name"]
        perf["type"] = plays[perf["playID"]]["type"]
        yield perf


def create_play_classes(perf) -> Play:
    return Play(**perf)


def statement(invoice: dict, plays: dict, html: bool = False) -> str:
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    cleaned_data = construct_play(invoice, plays)
    my_list_plays = map(create_play_classes, cleaned_data)

    for play in my_list_plays:
        parameters = play.get_parameters()
        total_amount += play.calc_amount_invoice(parameters)
        volume_credits += play.calculate_volume_credits()
        result += play.print_play()

    result += f"Amount owed is {format_as_dollars(total_amount/100)}\n"
    result += f"You earned {volume_credits} credits\n"
    return "<p>" + result.replace("\n", "<br>") + "</p>" if html else result
