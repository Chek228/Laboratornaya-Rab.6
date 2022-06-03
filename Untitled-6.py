#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Ввести кортеж одной строкой.
    A = tuple(map(int, input().split()))
    ind = 0
    while ind < len(A) and A[ind] == A[0]:
        ind += 1
    print(ind, A[ind:])