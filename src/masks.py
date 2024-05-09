def masks_card(number_card: str) -> str:
    """Принимает номер карты и возвращает ее маску"""
    masks_number_card = number_card[:4] + " " + number_card[4:6] + "** **** " + number_card[12:16]
    return masks_number_card


def masks_score(number_score: str) -> str:
    """Принимает номер счета и возвращает его маску"""
    masks_number_score = "**" + number_score[-4:]
    return masks_number_score
