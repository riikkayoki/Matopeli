# Ohjelmistotekniikka 2021

-----------------------
# Matopeli-sovellus

-------------------------------

Sovelluksen avulla käyttäjien on mahdollista pelata perinteistä Matopeliä.
Sovellusta voi käyttää yksi pelaaja kerrallaan. 

Pelin tarkoituksena on ohjata matoa peliruudukossa ja syödä omenoita. Syömällä omenoita, käyttäjä saa pisteitä.
Omenoita ilmestyy satunnaisessa järjestyksessä peliruudukkoon yksi kerrallaan.
Pisteiden kertyessä, myös pelin vaikeustaso muuttuu eli madon etenemisnopeus kiihtyy.
Peli loppuu mikäli mato törmää itseensä. 

## Huomio Python-versiosta

-------------------------------

Sovelluksen toiminta on testattu Python 3.8.10 versiolla. 

## Dokumentatio

-------------------------------

* [Käyttöohje]()
* [Vaatimusmäärittely](https://github.com/riikkayoki/ot-harjoitustyo/blob/master/harjoitustyo/dokumentaatio/vaativuusmaarittely.md)
* [Arkkitehtuurikuvaus]()
* [Testausdokumentti]()
* [Työaikakirjanpito](https://github.com/riikkayoki/ot-harjoitustyo/blob/master/harjoitustyo/dokumentaatio/tyoaikakirjanpito.md)

## Asennus

-------------------------------

1. Asenna riippuvuudet komennolla: `poetry install`


3. Suorita vaadittavat alustustoimenpiteet komennolla:`poetry run invoke build`


3. Käynnistä sovellus komennolla: `poetry run invoke start`


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



