# Ohjelmistotekniikka 2021

-----------------------
# Matopeli-sovellus

-------------------------------
[Paina tästä päästäksesi viimeisempään releaseen](https://github.com/riikkayoki/ot-harjoitustyo/releases)

-------------------------------

Sovelluksen avulla käyttäjien on mahdollista pelata perinteistä Matopeliä.
Sovellusta voi käyttää yksi pelaaja kerrallaan. 

Pelin tarkoituksena on ohjata matoa peliruudukossa ja syödä omenoita. Syömällä omenoita, käyttäjä saa pisteitä.
Omenoita ilmestyy satunnaisessa järjestyksessä peliruudukkoon yksi kerrallaan.
Peli loppuu mikäli mato törmää seinään tai itseensä. 

## Huomio Python-versiosta

-------------------------------

Sovelluksen toiminta on testattu Python 3.8.10 versiolla. 

## Dokumentatio

-------------------------------

* [Käyttöohje](https://github.com/riikkayoki/ot-harjoitustyo/blob/master/harjoitustyo/dokumentaatio/kayttoohje.md)
* [Vaatimusmäärittely](https://github.com/riikkayoki/ot-harjoitustyo/blob/master/harjoitustyo/dokumentaatio/vaativuusmaarittely.md)
* [Arkkitehtuurikuvaus](https://github.com/riikkayoki/ot-harjoitustyo/blob/master/harjoitustyo/dokumentaatio/arkkitehtuuri.md)
* [Testausdokumentti](https://github.com/riikkayoki/ot-harjoitustyo/blob/master/harjoitustyo/dokumentaatio/testaus.md)
* [Työaikakirjanpito](https://github.com/riikkayoki/ot-harjoitustyo/blob/master/harjoitustyo/dokumentaatio/tyoaikakirjanpito.md)

## Asennus

-------------------------------

1. Asenna riippuvuudet komennolla: `poetry install`


2. Käynnistä sovellus komennolla: `poetry run invoke start`


## Komentorivitoiminnot

------------------------

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla: `poetry run invoke start`


### Testaus

Ohjelman testit pystyy testaamaan komennolla: `poetry run invoke test`


### Testikattavuus

Ohjelman testikattavuuden pystyy generoimaan komennolla: `poetry run invoke coverage-report`

### Pylint

Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:

`poetry run invoke lint`



