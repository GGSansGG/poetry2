def state_executed(old_list: list, state_value: str = "EXECUTED") -> list:
    """Сортирует список по значению 'state'"""
    new_list = []
    for i in old_list:
        for v, b in i.items():
            if v == "state":
                if b == state_value:
                    new_list.append(i)
    return new_list


def sort_date(old_list: list, bool_reverse: bool = True) -> list:
    """Сортирует список по дате"""
    new_list = sorted(old_list, key=lambda x: x["date"], reverse=(bool_reverse))
    return new_list


print(
    state_executed(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)

print(
    sort_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
