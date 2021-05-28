def fun(nota):
    if nota > 7:
        return "Promociona"
    else:
        if nota < 4:
            return "Aplazado"
        else:
            if 4 <= nota <= 7:
                return "Aprobado"