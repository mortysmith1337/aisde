#!/usr/bin/env python3
import string

class bcolors:

    OKGREEN = '\033[92m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    ENDC = '\033[0m'

def shellSort(tab):
    #Autorem tej funkcji jest Mohit Kumra, kod podchodzi z geeksforgeeks.org
    # Start with a big gap, then reduce the gap
    n = len(tab)
    gap = n/2

    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:

        for i in range(gap,n):

            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = tab[i]

            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while  j >= gap and tab[j-gap] >temp:
                tab[j] = tab[j-gap]
                j -= gap

            # put temp (the original a[i]) in its correct location
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
