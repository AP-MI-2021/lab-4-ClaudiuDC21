from typing import List

def show_menu():
    print('1. Citirea a doua liste de numere intregi. ')
    print('2. Afisare daca cele doua liste au acelasi numar de elemente pare. ')
    print('3. Afisarea intersectiei celor doua liste')
    print('4. Afisare palindroame prin concatenarea listelor. ')
    print('5. Afisare oglindit daca acel element e divizibil la toate elementele celei de a 3 a lista')
    print('x. Iesire.')


def read_list() -> List[int]:
    """
    Citire lista.
    """
    lista_str = input('Alegeti numerele separate prin spatiu: ')
    lista_str_split = lista_str.split(' ')
    lista_int = []
    for num in lista_str_split:
        lista_int.append(int(num))
    return lista_int


def get_same_number_of_par(lst1: List[int], lst2: List[int]) -> bool:
    '''
    Determina daca 2 liste au acelaso numar de elemente pare.
    :param lst1: Prima lista data.
    :param lst2: A doua lista data.
    :return: True daca au acelasi numar de elemente pare, False in caz contrar.
    '''
    numar1 = 0
    numar2 = 0
    for num in lst1:
        if num % 2 == 0:
            numar1 += 1
    for num in lst2:
        if num % 2 == 0:
            numar2 += 1
    if numar1 == numar2:
        if numar1 == 0 and numar2 == 0:
            return False
        return True
    return False


def test_get_same_number_of_par():
    assert get_same_number_of_par([], []) == False
    assert get_same_number_of_par([1, 2, 3, 4, 5], [2, 3, 4, 3, 3, 55, 45, 57]) == True
    assert get_same_number_of_par([12, 13, 14, 1618], [11, 3, 5, 7]) == False


def get_numbers_from_both_lists(lst1: List[int], lst2: List[int]) -> List[int]:
    '''
    Determina elementele care sunt in ambele liste.
    :param lst1: Prima lista data.
    :param lst2: A doua lista data.
    :return: O lista cu intersectia primel 2 liste.
    '''
    intersectia = []
    for num1 in lst1:
        for num2 in lst2:
            if num1 == num2:
                ok = 1
                for elemente in intersectia:
                    if num1 == elemente:
                        ok = 0
                if ok == 1:
                    intersectia.append(int(num1))
    return intersectia


def test_get_numbers_from_both_lists():
    assert get_numbers_from_both_lists([], []) == []
    assert get_numbers_from_both_lists([12, 22, 36, 424], [22, 23, 36, 55, 424]) == [22, 36, 424]
    assert get_numbers_from_both_lists([13, 14, 53, 365, 345, 23, 13, 14, 365],[13, 14, 243, 3445, 13, 14, 24342, 365]) == [13, 14, 365]


def get_palindrome_on_concat_of_lists(lst1: List[int], lst2: List[int]) -> List[int]:
    '''
    Determina toate palindroamele obținute prin concatenarea elementelor de pe aceleași poziții în cele două liste
    :param lst1: Prima lista data.
    :param lst2:A doua lista data.
    :return:O lista cu palindroamele obtinute prin concatenare.
    '''
    palindroame = []
    lungime_minima = min(len(lst1), len(lst2))
    for num in range(lungime_minima):
        str_list_1 = str(lst1[num])
        str_list_2 = str(lst2[num])
        str_mare = str_list_1 + str_list_2
        if str_mare == str_mare[::-1]:
            palindroame.append(int(str_mare))
    return palindroame


def test_get_palindrome_on_concat_of_lists():
    assert get_palindrome_on_concat_of_lists([], []) == []
    assert get_palindrome_on_concat_of_lists([12, 22, 36, 11], [21, 23, 63, 55, 424]) == [1221, 3663]
    assert get_palindrome_on_concat_of_lists([1, 23, 45, 544, 342], [1, 23, 243, 2575, 243, 454, 666]) == [11, 342243]


def get_reverse(n: int) -> int:
    '''
    Determina inversul unui numar n.
    :param n: numarul dat
    :return: inversul numarului
    '''
    invers = 0
    while n:
        invers = invers * 10 + n % 10
        n = n // 10
    return invers


def test_get_reverse():
    assert get_reverse(1) == 1
    assert get_reverse(123) == 321
    assert get_reverse(246) == 642


def get_lists_with_reverse_on_div_elements(lst1: List[int], lst2: List[int], lst3:List[int]) -> tuple:
    '''
    Determina listele obținute prin înlocuirea în cele două liste citite la punctul 1 a
tuturor elementelor cu oglinditul lor dacă îndeplinesc următoarea regulă: elementele sunt divizibile
cu toate elementele din a treia lista.
    :param lst1:Prima lista data.
    :param lst2:A doua lista data.
    :param lst3:A treia lista cu care se vor compara primele 2.
    :return: 2 liste cu elemente prelucrte.
    '''
    lst1_prelucrat = []
    lst2_prelucrat = []
    for num in lst1:
        work = 1
        for div in lst3:
            if num % div != 0:
                work = 0
        if work == 1:
            lst1_prelucrat.append(int(get_reverse(num)))
        else:
            lst1_prelucrat.append(int(num))
    for num in lst2:
        work = 1
        for div in lst3:
            if num % div != 0:
                work = 0
        if work == 1:
            lst2_prelucrat.append(int(get_reverse(num)))
        else:
            lst2_prelucrat.append(int(num))
    return lst1_prelucrat, lst2_prelucrat


def test_get_lists_with_reverse_on_div_elements():
    assert get_lists_with_reverse_on_div_elements([], [], []) == ([], [])
    assert get_lists_with_reverse_on_div_elements([12, 22, 36, 363], [22, 23, 36, 55, 363], [1, 2, 3, 4]) == ([21, 22, 63, 363], [22, 23, 63, 55, 363])
    assert get_lists_with_reverse_on_div_elements([15, 23, 453, 643, 24], [12, 24, 35, 55], [1, 2, 3, 4]) == ([15, 23, 453, 643, 42], [21, 42, 35, 55])


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
            if get_same_number_of_par(lista1, lista2):
                print('Cele două liste au același număr de elemente pare.')
            else:
                print('Cele două liste nu au același număr de elemente pare.')
        elif optiunea == '3':
            print(f'Intersectia celo doua liste este {get_numbers_from_both_lists(lista1, lista2)}')
        elif optiunea == '4':
            print(f'Lista cu elementele palindrom prin concatenare sunt: {get_palindrome_on_concat_of_lists(lista1, lista2)}')
        elif optiunea == '5':
            print('Cititi a 3 a lista!')
            lista3 = read_list()
            print(f'Dupa prelucrare, listele vor fi acestea: {get_lists_with_reverse_on_div_elements(lista1,lista2,lista3)}')
        elif optiunea == 'x':
            break
        else:
            print('Optiune invalida, incercati din nou! ')


if __name__ == '__main__':
    test_get_same_number_of_par()
    test_get_numbers_from_both_lists()
    test_get_palindrome_on_concat_of_lists()
    test_get_reverse()
    test_get_lists_with_reverse_on_div_elements()
    main()
