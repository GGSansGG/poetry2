def state_executed(old_list: list, n="EXECUTED") -> list:
    new_list = []
    for i in old_list:
        for v, b in i.items():
            if v == "state":
                if b == n:
                    new_list.append(i)
    return new_list


def sort_date(old_list: list, s=True) -> list:
    new_list = sorted(old_list, key=lambda x: x["date"], reverse=(s == True))
    return new_list
