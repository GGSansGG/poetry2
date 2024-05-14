def mask_number(number: str) -> str:
    """Принимает на вход строку и делает маску"""
    for i in number:
        if (i == "с") or (i == "С"):
            masks_number_score = number[:4] + " **" + number[-4:]
            return masks_number_score
        else:
            a = number.split()
            w = []
            for s in a:
                if s.isalpha() == True:
                    w.append(s)
            q = " ".join(w)
            v = q + " " + number[-19:-7] + "** ****" + number[-5:]
            return v

def convert_date(date_str):
    parts = date_str.split('T')[0].split('-')
    result = f"{parts[2]}.{parts[1]}.{parts[0]}"
    return result


print(mask_number("Visa Platinum 7000 7922 8960 6361"))
print(mask_number("Счет 73654108430135874305"))

print(convert_date("2018-07-11T02:26:18.671407"))
