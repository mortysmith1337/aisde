#!/usr/bin/env python3
import string


class bcolors:

    OKGREEN = '\033[92m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    ENDC = '\033[0m'

def shakerSort(array):

    passed = 0
    swapped = True
    while swapped == True:
        swapped = False
        if passed % 2 == 0:
            for i in range (len(array) - 1):
                if array[i] > array [i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swapped = True
        else:
            for i in range(len(array) - 1, 0, -1):
                if array[i] < array [i - 1]:
                    array[i - 1], array[i] = array[i], array[i - 1]
                    swapped = True
        passed += 1
    return

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
    shakerSort(tab_input)
    print(bcolors.HEADER + "Po posortowaniu:\n" + bcolors.ENDC)
    print(bcolors.OKBLUE + str(tab_input) + bcolors.ENDC)
