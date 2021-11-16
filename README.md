# Ohjelmistotekniikka 2021

-----------------------
##Harjoitustehtävät

--------------------------

- [x] Viikko 1 

  [gitlog.txt](https://github.com/riikkayoki/ot-harjoitustyo/blob/master/laskarit/viikko1/gitlog.txt) & 
  [komentorivi.txt](https://github.com/riikkayoki/ot-harjoitustyo/blob/master/laskarit/viikko1/komentorivi.txt)


- [x] Viikko 2

  [maksukortti](),
  [unicafe](),
  [vaatimusmäärittely]() &
  [tuntiaikakirjanpito]()


- [ ] Viikko 3

- [ ] Viikko 4

- [ ] Viikko 5 

- [ ] Viikko 6


# Tetris-sovellus

-------------------------------

Sovelluksen avulla käyttäjien on mahdollista pelata perinteistä Tetris-peliä.
Sovellusta voi käyttää yksi pelaaja kerrallaan. 

Pelin tarkoituksena on kerätä pisteitä järjestäen palikoita vaakasuoriksi riveiksi.
Palikoita tippuu peliruudun yläreunasta satunnaisessa järjestyksessä, ja niitä järjestetään peliruudun alareunaan käyttäjän haluamalla tavalla.
Pisteiden kertyessä, myös pelin vaikeustaso muuttuu eli palikoiden tippumisnopeus kiihtyy.
Peli loppuu mikäli palikat ylittävät peliruudun yläreunan. 

##Huomio Python-versiosta

-------------------------------
Sovelluksen toiminta on testattu Python 3.8.10 versiolla. 

##Dokumentatio

-------------------------------

* [Käyttöohje]()
* [Vaatimusmäärittely]()
* [Arkkitehtuurikuvaus]()
* [Testausdokumentti]()
* [Työaikakirjanpito]()

##Asennus

-------------------------------

1. Asenna riippuvuudet komennolla: `poetry install`


3. Suorita vaadittavat alustustoimenpiteet komennolla:`poetry run invoke build`


3. Käynnistä sovellus komennolla: `poetry run invoke start`


##Komentorivitoiminnot

------------------------

###Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla: `poetry run invoke start`


###Testaus

Ohjelman testit pystyy testaamaan komennolla: `poetry run invoke test`


###Testikattavuus

Ohjelman testikattavuuden pystyy generoimaan komennolla: `poetry run invoke coverage-report`

###Pylint



