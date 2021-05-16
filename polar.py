# -*- coding: utf-8 -*-
from itertools import combinations
from argparse import ArgumentParser


def diff_lists(x, y):
    res = []
    sorted_y = [sorted(i) for i in y]
    for i in x:
        if not sorted(i) in sorted_y:
            res.append(i)
    return res

def weakly_less(x, y):
    for i in x:
        if not i in y:
            return False
    return True

def get_max_monomials(code):
    max_code = []
    for x in code:
        add = True
        for y in code:
            if not x == y and weakly_less(x, y):
                add = False
                break
        if add:
            max_code.append(x)
    return max_code

def get_dual_code(m, intervals):
    i_code = set()
    teta = ''.join(str(i) for i in range(1, m + 1))
    all_monomials = [''.join(l) for i in range(len(teta)) for l in combinations(teta, i+1)]
    for x in intervals:
        i_code.update([''.join(l) for i in range(len(x)) for l in combinations(x, i+1)])
    i_code.add('')
    i_check = []
    for x in list(i_code):
        rev = ''.join(i for i in list(set(teta) - set(x)))
        i_check.append(rev)
    return diff_lists(all_monomials, i_check)


def main():
    parser = ArgumentParser()
    parser.add_argument("--dim", dest="dim", type=int, required=True,
                        help="Размерность пространства мономов")
    parser.add_argument("--monomials", dest="monoms_str", type=str, required=True,
                        help="Мономы из множества максимальных мономов кода через запятую в кавычках, пример - \"\'12345, 2346, 1237\'\"")
    parser.add_argument("--print-all", dest="print_all", action="store_true",
                        help="Вывести весь дуальный код (без этого аргумента выводится только множество максимальных мономов)")
    args = parser.parse_args()

    intervals = args.monoms_str.replace(' ', '').split(',')

    code = get_dual_code(args.dim, intervals)
    if args.print_all:
        print(code)
    print(get_max_monomials(code))

if __name__ == '__main__':
    main()
