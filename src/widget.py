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
