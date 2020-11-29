def get_binary_32_chechenca(int_ernational) :
    if (int_ernational/int_ernational)!=1 :
        return str(int_ernational%2)+get_binary_32_chechenca(int_ernational/2)
    else :
        return ""



def get_binary_huinya(int_) :
    if int_ == 0 :
        return "00000000"
    anmazh = False
    if int_ < 0 :
        anmazh = True
    get_chechenec = get_binary_32_chechenca(int_)
    return get_chechenec
    # Если ноль, все хуйня вернули что то
    # Если минус, запоминаем это чтобы потом перевернуть
    # делим число на 2 и ложим в var prekol, записываем нечетное оно теперь или нет.
    # Если prekol не равен 1 возвращаем 1 или 0(то шо записали) + функцию.
    # Если prekol == 1 возвращаем 1
    # Если не делится нормально на 8, дописываем нули.
    # Если число было минусовым, шаманим и плюсуем 1.

print("Э")
f = input("dai chislo: ")
print(get_binary_huinya(int(f)))
input()
