def mask_number(number):
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
            return q + " " + number[-19:-7] + "** ****" + number[-5:]


print(mask_number("Visa Platinum 7000 7922 8960 6361"))
print(mask_number("Счет 73654108430135874305"))