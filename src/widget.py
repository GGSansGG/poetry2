def mask_number(number: str) -> str:
    """Принимает на вход строку и делает маску"""
    for i in number:
        if (i == "с") or (i == "С"):
            masks_number_score = number[:4] + "**" + number[-4:]
            return masks_number_score
        else:
            masks_number_card = number[:9] + " " + number[9:11] + "** **** " + number[17:21]
            return masks_number_card
