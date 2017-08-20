#!/usr/bin/env python3
class bcolors:

    OKGREEN = '\033[92m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    ENDC = '\033[0m'


def selectionSort(tab):
    a = 0
    for a in range(len(tab)-1,0,-1):
        posMax = 0
        for location in range(1, a+1):
            if tab[location] > tab[posMax]:
                posMax = location
        temp = tab[a]
        tab[a] = tab[posMax]
        tab[posMax] = temp

        for i in range(0, a):
            print(str(tab[i]), sep = ' ', end=' ', flush=True)
        for j in range(a, len(tab)):
            print(bcolors.OKGREEN + str(tab[j]) + bcolors.ENDC, sep = ' ', end=' ', flush=True)
        print("\n")
    for j in range(0, len(tab)):
        print(bcolors.OKGREEN + str(tab[j]) + bcolors.ENDC, sep = ' ', end=' ', flush=True)
    print("\n")


if __name__ == "__main__":
    tab_input = []
    print("Wprowadz liczbe to tabeli i nacisnij enter: \n Aby przerwac zostaw puste pole lub wpisz inna wartosc niz liczba")
    i = 1
    while(i):
        try:
            i = int(input('liczba = '))
        except ValueError:
            print("przerwano!")
            i = 0
        if(i != 0):
            tab_input.append(i)
    print(bcolors.HEADER + "Przed posortowaniem:\n" + bcolors.ENDC)
    print(bcolors.OKBLUE + str(tab_input) + bcolors.ENDC + "\n")
    selectionSort(tab_input)
    print(bcolors.HEADER + "Po posortowaniu:\n" + bcolors.ENDC)
    print(bcolors.OKBLUE + str(tab_input) + bcolors.ENDC)
