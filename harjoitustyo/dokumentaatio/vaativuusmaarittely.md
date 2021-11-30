# Vaatimusmäärittely 
_____________________

## Sovelluksen tarkoitus

--------------------------------------

Sovellus on versio perinteisestä Matopelistä. 

## Käyttäjät
_______________________________________________________

Tässä sovelluksessa on vain yhden tyyppisiä käyttäjiä eli pelaajia.

## Käyttöliittymä luonnos
________________________________


Sovelluksen käyttöliittymä muodostuu neljästä erilaisesta komponentista:

1. *Päävalikko*: Kun peli avataan, tulee käyttäjälle näkyviin päävalikko. Päävalikosta pystyy katsomaan ohjeet ja aloittamaan pelin. 
Painaessaan 'Start' -nappia, peli käynnistyy. 


2. *Peliruudukko*: peliruudussa on näkyvissä itse peli, seuraava putoava pala sekä pisteet että taso. 


3. *Onnittelut ja nimimerkin lisääminen*: Mikäli pelaaja oli pistemäärältään top 5 pelaajan joukossa, päätyy hän valikkoon, jossa häntä onnitellaan. 
Tämän lisäksi hänen tulee syöttää nimimerkkinsä ruutuun ja lähettään tämän eteenpäin.


4. *Top 5 -näkymä*: Päädymme tähän 3. komponentin jälkeen tai mikäli käyttäjä ei ollut top 5 pelaajan joukossa.
Tässä valikossa käyttäjä lisää ruutuun nimimerkkinsä ja lähettää sen eteenpäin.
Tämän jälkeen käyttäjä päätyy top5 valikkoon, jossa näkyy hännen nimensä.
Päädymme tämän valikon jälkeen taas päävalikkoon.

## Perusversion tarjoama toiminnallisuus
___________________________________

* Päävalikko.
  * Start -nappi
  * Käyttöohjeet -nappi


* Pelialue 20x20.
  * Mato voi liikkua vain pelialueella.  **TEHTY**
  * Jos mato osuu pelialueen reunaan, peli loppuu **TEHTY**


* Pelissä on mato. **TEHTY**
  * Madon pituus muodostuu aluksi yhdestä ruudusta. **TEHTY**
  * Mato pitenee, kun se syö omenan. **TEHTY**
  * Mato liikkuu kokoajan. **TEHTY**
  * Matoa voi kääntää vasemmalle, oikealle, ylös tai alas. **TEHTY**


* Pelissä on omena.
  * Peliruudussa on yksi omena kerrallaan. **TEHTY**
  * * Omena vaihtaa paikkaa, kun mato syö sen. **TEHTY**


* Pelaaja kerää pisteitä syömällä omenoita.
  * Pelaaja saa pisteen, kun syö omenan.
  * Kun pelaaja saa pisteen, piste tulee näkyviin kohtaan 'Points'.
  

* Pelissä on eri tasoja:
  * Kun pelaaja on saanut tietyn määrän pisteitä, mato muuttuu taas yksi ruutuiseksi ja sen nopeus kiihtyy. 
  * Käyttäjä näkee tasonsa ja pisteidensä määrän peliruudun kohdasta 'Levels'. 
   

* Peli päättyy, jos mato osuu itseensä.
  * Jos pelaaja oli top5 pelaanjan joukossa pistemäärältään, hän lisää nimensä kenttään ja nimi näkyy leaderboardilla.
  * Jos pelaaja ei ollut top5 pelaajan joukossa, hän näkee sijoituksensa pelissä.
  * Näkymä ohjautuu taas päävalikkoon.


## Jatkokehitysideoita
____________________________________________________

Jos jää aikaa jäljelle niin sovellusta voi kehittää seuraavasti:

* Pelaaja voi valita vaikeustason päävalikosta.
* Päävalikkoon lisätään nappi, josta pääsee näkemään top 5 pelaajat ja heidän pisteet.
* Pelin voi laittaa tauolle.
* Top 5 pelaajaa näkyy myös pelatessa peliä.
* Pelissä on ääniefektejä.
