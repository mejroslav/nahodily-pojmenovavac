#!/usr/bin/python
"""Tento skript generuje daný počet náhodně vybraných dvojic
'přídavné jméno' + 'podstatné jméno'."""
import os
import re
import random
import optparse

PATH = os.path.dirname(__file__)


translation_table = {
    ord("Á"): ord("A"),
    ord("É"): ord("E"),
    ord("Ě"): ord("E"),
    ord("Í"): ord("I"),
    ord("Ó"): ord("O"),
    ord("Ú"): ord("U"),
    ord("Ů"): ord("U"),
    ord("Ý"): ord("Y"),
    ord("Č"): ord("C"),
    ord("Ď"): ord("D"),
    ord("Ň"): ord("N"),
    ord("Ř"): ord("R"),
    ord("Š"): ord("S"),
    ord("Ť"): ord("T"),
    ord("Ž"): ord("Z"),
}


def remove_diacritics(s: str) -> str:
    """Remove hooks and dashes from a word or letter."""
    return s.upper().translate(translation_table).lower()


def merge_with_underscore(str1, str2):
    return str1 + "_" + str2


def main(number: int):
    filename: str = os.path.abspath(PATH+"/slova.txt")
    seznam: list[str] = []

    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f.readlines():
            seznam.append(line.rstrip("\n"))

    seznam_pridavnych_jmen: list[str] = [
        w for w in seznam if re.search("(í|ý)$", w)
        and not re.search("(a|á|e|ě)ní$", w)
        and not re.search("emí$", w)
        and not re.search("ství$", w)
        and not re.search("tí$", w)
        and not re.search("tví$", w)]
    seznam_podstatnych_jmen: list[str] = [
        w for w in seznam if re.search("(a|á|e|é|i|í|o|ó|u|ů)k$", w)
        or re.search("o(n|ň)$", w) or re.search("(u|ů)(n|ň)$", w)]

    for _ in range(number):
        pridavne: str = random.choice(seznam_pridavnych_jmen)
        podstatne: str = random.choice(seznam_podstatnych_jmen)
        if options.diacritics:
            pridavne, podstatne = remove_diacritics(pridavne), remove_diacritics(podstatne)
        if options.underscore:
            nahodne_slovo = merge_with_underscore(pridavne, podstatne)
        else:
            nahodne_slovo = pridavne.lower() + " " + podstatne.lower()
        print(nahodne_slovo)


if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-n', dest='number',
                      type='int',
                      help='generate n random doubles')
    parser.add_option('-d',
                      action="store_true",
                      dest='diacritics',
                      default=False,
                      help='remove diacritics')
    parser.add_option('-u',
                      action="store_true",
                      dest='underscore',
                      default=False,
                      help='merge it with underscore')
    (options, args) = parser.parse_args()
    number = options.number if options.number is not None else 1
    main(number)
