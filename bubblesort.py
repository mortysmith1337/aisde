#!/usr/bin/env python3
class bcolors:

    OKGREEN = '\033[92m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    ENDC = '\033[0m'

def swap(tab, i, j):
        tab[i], tab[j] = tab[j], tab[i]

def bubbleSort(tab):
    n = len(tab)
    while(n>1):
        for i in range(n-1):
            if(tab[i] > tab[i+1]):
                swap(tab, i, i+1)
        n = n-1

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
    bubbleSort(tab_input)
    print(bcolors.HEADER + "Po posortowaniu:\n" + bcolors.ENDC)
    print(bcolors.OKBLUE + str(tab_input) + bcolors.ENDC)
