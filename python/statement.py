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
}


def calc_amount_invoice(
    spec_num: int,
    base: int,
    audience_bonus: int,
    audience_threshold: int,
    audience_base: int,
) -> int:
    return (
        base
        + audience_bonus * (max(spec_num, audience_threshold) - audience_threshold)
        + audience_base * spec_num
    )


def format_as_dollars(amount):
    return f"${amount:0,.2f}"


@dataclass
class Play:
    customer: str
    playID: str
    audience: int
    name: str
    type: str

    def calculate_amount(self):
        parameters = AMOUNT_PER_TYPE.get(self.type)
        if not parameters:
            raise ValueError(f"unknown type: {self.type}")
        return calc_amount_invoice(self.audience, **parameters)


def construct_play(invoices: dict, plays: dict):
    for perf in invoices["performances"]:
        perf["customer"] = invoices["customer"]
        perf["name"] = plays[perf["playID"]]["name"]
        perf["type"] = plays[perf["playID"]]["type"]
        yield perf


def create_play_classes(perf) -> Play:
    return Play(**perf)


def statement(invoice, plays) -> str:
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    cleaned_data = construct_play(invoice, plays)
    my_list_plays = map(create_play_classes, cleaned_data)

    for play in my_list_plays:
        total_amount += play.calculate_amount()
        # add volume credits
        volume_credits += max(play.audience - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play.type:
            volume_credits += math.floor(play.audience / 5)
        # print line for this order
        result += (
            f" {play.name}:"
            f" {format_as_dollars(play.calculate_amount()/100)} ({play.audience} seats)\n"
        )

    result += f"Amount owed is {format_as_dollars(total_amount/100)}\n"
    result += f"You earned {volume_credits} credits\n"
    print(result)
    return result
