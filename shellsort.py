#!/usr/bin/env python3
import string

class bcolors:

    OKGREEN = '\033[92m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    ENDC = '\033[0m'

def shellSort(tab):
    #Autorem tej funkcji jest Mohit Kumra, kod podchodzi z geeksforgeeks.org
    n = len(tab)
    gap = n/2

    while gap > 0:

        for i in range(gap,n):

            temp = tab[i]
            j = i
            while  j >= gap and tab[j-gap] >temp:
                tab[j] = tab[j-gap]
                j -= gap
            tab[j] = temp
        gap /= 2

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
        except NameError:
            print("przerwano!")
            i = 0
        except SyntaxError:
            print("przerwano!")
            i = 0
        if(i != 0):
            tab_input.append(i)
    print(bcolors.HEADER + "Przed posortowaniem:\n" + bcolors.ENDC)
    print(bcolors.OKBLUE + str(tab_input) + bcolors.ENDC + "\n")
    shellSort(tab_input)
    print(bcolors.HEADER + "Po posortowaniu:\n" + bcolors.ENDC)
    print(bcolors.OKBLUE + str(tab_input) + bcolors.ENDC)
