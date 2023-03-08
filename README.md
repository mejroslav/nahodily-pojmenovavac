# Nahodilý Pojmenovávač

Tento skript generuje náhodné dvojice 'přídavné jméno' + podstatné jméno.

## Usage

**Flags**:
- `-n int` - generuje daný počet dvojic
- `-d` - generuje bez diakritiky, ve tvaru `podstatne_pridavne`

```shell
foo@bar~$ python3 main.py
pravomocný zdravotník
```

```shell
foo@bar~$ python3 main.py -n 3
gastronomický psík
rezervní karbon
osmadvacetiletý dubček
```

```shell
foo@bar~$ python3 main.py -n 3 -u
dvoubrankový_vozíček
žulový_kotník
rozebraný_deníček
```

```shell
foo@bar~$ python3 main.py -n 3 -d
slovesny navstevnik
breclavsky slavik
breclavsky korinek
```

```shell
foo@bar~$ python3 main.py -n 3 -du
obsahly_prohresek
kutnohorsky_usudek
zanikly_opasek
```