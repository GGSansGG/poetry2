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
