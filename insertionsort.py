#!/usr/bin/env python3
class bcolors:

    OKGREEN = '\033[92m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    ENDC = '\033[0m'


def insertionSort(tab):

    for i in range(1, len(tab)):
        key = tab[i]
        j = i-1
        while((j>=0) and tab[j] > key):
            tab[j+1] = tab[j]
            j = j-1
        tab[j+1] = key

        for k in range(0, i):
            print(bcolors.OKGREEN + str(tab[k]) + bcolors.ENDC, sep = ' ', end=' ', flush=True)
        for g in range(i, len(tab)):
            print(str(tab[g]), sep = ' ', end=' ', flush=True)
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
    insertionSort(tab_input)
    print(bcolors.HEADER + "Po posortowaniu:\n" + bcolors.ENDC)
    print(bcolors.OKBLUE + str(tab_input) + bcolors.ENDC)
