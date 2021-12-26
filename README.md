# Ohjelmistotekniikka syksy 2021

# Matopeli-sovellus



Sovelluksen avulla käyttäjien on mahdollista pelata perinteistä Matopeliä.
Sovellusta voi käyttää yksi pelaaja kerrallaan. 

Pelin tarkoituksena on ohjata matoa peliruudukossa ja syödä omenoita. Syömällä omenoita, käyttäjä saa pisteitä.
Omenoita ilmestyy satunnaisessa järjestyksessä peliruudukkoon yksi kerrallaan.
Peli loppuu mikäli mato törmää seinään tai itseensä. 


## Huomio Python-versiosta



Sovelluksen toiminta on testattu Python 3.8.10 versiolla. 

## Lataa sovellus 

Valmiin sovelluksen release löytyy [täältä](https://github.com/riikkayoki/ot-harjoitustyo/releases).

## Dokumentatio


* [Käyttöohje](https://github.com/riikkayoki/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)


* [Vaatimusmäärittely](https://github.com/riikkayoki/ot-harjoitustyo/blob/master/dokumentaatio/vaativuusmaarittely.md)


* [Arkkitehtuurikuvaus](https://github.com/riikkayoki/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)


* [Testausdokumentti](https://github.com/riikkayoki/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)


* [Työaikakirjanpito](https://github.com/riikkayoki/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

## Asennus


Asenna riippuvuudet komennolla:

`poetry install`

Suorita alustustoimenpiteet komennolla:

`poetry run invoke build`

Käynnistä komennolla:

`poetry run invoke start`

## Komentorivitoiminnot


### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla: 

```
poetry run invoke start
```

### Testaus

Ohjelman testit pystyy testaamaan komennolla: 

```
poetry run invoke test
```


### Testikattavuus

Ohjelman testikattavuuden pystyy generoimaan komennolla: 

```
poetry run invoke coverage-report
```

Testauskattavuuden raportin saa avattua Firefox -selaimessa komennolla:

```
poetry run invoke view-report
```

### Pylint

Tiedoston [.pylintrc](https://github.com/riikkayoki/ot-harjoitustyo/blob/master/harjoitustyo/.pylintrc) 
määrittelemien tarkistukset voi suorittaa komennolla:

```
poetry run invoke lint
```



