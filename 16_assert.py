def firs_letter(caracter_letter):
    firs_letter = []

    for letter in caracter_letter:
        assert type(letter) == str, f'{letter} mo es un string'
        assert len(letter) > 0, ' X Is a invalid sentences X ' 

        firs_letter.append(letter[0])
    return firs_letter