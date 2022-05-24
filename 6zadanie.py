#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    for a in [(1, 1, 1), (1, 2, 2), (1, 1, 2, 2), ()]:
            c = len(list(filter(lambda x: x == a[0], a)))
            print(c)
            print(a[c:])
            print()
