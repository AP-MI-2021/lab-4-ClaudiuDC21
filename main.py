def show_menu():
    print('1. Citirea a doua liste de numere intregi. ')
    print('2. Afisare daca cele doua liste au acelasi numar de elemente pare. ')
    print('3. Afisarea intersectiei celor doua liste')
    print('4. Afisare palindroame prin concatenarea listelor. ')
    print('5. Afisare oglindit daca acel element e divizibil la toate elementele celei de a 3 a lista')
    print('x. Iesire.')


def read_list():
    """
    Citire lista.
    """
    lista_str = input('Alegeti numerele separate prin spatiu: ')
    lista_str_split = lista_str.split(' ')
    lista_int = []
    for num in lista_str_split:
        lista_int.append(int(num))
    return lista_int

def main():
    lista1 = []
    lista2 = []
    lista3 = []
    while True:
        show_menu()
        optiunea = input('Alegeti o optiune: ')
        if optiunea == '1':
            print('Prima lista care se citeste: ')
            lista1 = read_list()
            print()
            print('A doua lista care se citeste: ')
            lista2 = read_list()
        elif optiunea == '2':
            pass
        elif optiunea == '3':
            pass
        elif optiunea == '4':
            pass
        elif optiunea == '5':
            pass
        elif optiunea == 'x':
            break
        else:
            print('Optiune invalida, incercati din nou! ')


if __name__ == '__main__':
    main()
