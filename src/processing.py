def state_executed(old_list: list, n="EXECUTED") -> list:
    new_list = []
    for i in old_list:
        for v, b in i.items():
            if v == "state":
                if b == n:
                    new_list.append(i)
    return new_list
