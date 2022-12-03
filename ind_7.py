#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def initial_func(text1, text2):
    return text1.split(), text2.split()

def decor(func):
    def decor_meat(text1, text2):
        data = func(text1, text2)
        return dict(zip(*data))

    return decor_meat

if __name__ == '__main__':

    initial_func = decor(initial_func)

    text1 = "QUEEN_OF_RAP MONEYDEALER"
    text2 = "MONEYKEN_LOVE И_ЧТОЭ"

    print(initial_func(text1, text2))