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


2. *Käyttöohjevalikko*: Kun päävalikosta painetaan nappia 'INSTRUCTIONS', päädymme käyttöohjevalikkoon.
Käyttöohjevalikosta voi katsoa pelin ohjeet. 


3. *Tulostauluvalikko*: Kun päävalikosta painetaan nappia 'LEADERBOARD', päädymme käyttöohjevalikkoon.
Tulostauluvalikosta voi katsoa pelin top10 parhaat pelaajat. 


4. *Peliruudukko*: peliruudussa on näkyvissä itse matopeli.


5. *Onnittelut ja nimimerkin lisääminen*: Pelin loputtua, pelaaja päätyy valikkoon, jossa häntä onnitellaan. 
Tämän lisäksi hänen tulee syöttää nimimerkkinsä ruutuun ja lähettää tämän eteenpäin painamalla 'enter' -nappia.


## Perusversion tarjoama toiminnallisuus
___________________________________

* Päävalikko. 
  * Start -nappi 
  * Käyttöohjeet -nappi 
  * Tulostaulukko -nappi
  

* Pelialue. 
  * Mato voi liikkua vain pelialueella.  
  * Jos mato osuu pelialueen reunaan, peli loppuu 
  

* Pelissä on mato. 
  * Madon pituus muodostuu aluksi yhdestä ruudusta.
  * Mato pitenee, kun se syö omenan. 
  * Mato liikkuu kokoajan. 
  * Matoa voi kääntää aina vasemmalle, oikealle, ylös tai alas.


* Pelissä on omena.
  * Peliruudussa on yksi omena kerrallaan.
    * Omena sijoittuu satunnaiseen paikkaan peliruudussa. 
Se voi myös sijoittua kohtaan, jossa mato on.
    * Omena vaihtaa paikkaa, kun mato syö sen. 


* Pelaaja kerää pisteitä syömällä omenoita.
  * Pelaaja saa pisteen, kun syö omenan. 
  * Kun pelaaja saa pisteen, piste tulee näkyviin kohtaan 'Points'. 
  

* Peli päättyy, jos mato osuu itseensä tai pelialueen reunaan.
  * Pelaaja syöttää nimimerkkinsä tekstinsyöttöruutuun.
  * Syötettyään nimensä ja painettuaan 'enter' -nappia, pelaaja päätyy tulostaulunäkymään.


## Jatkokehitysideoita
____________________________________________________

Jos jää aikaa jäljelle niin sovellusta voi kehittää seuraavasti:

* Pelissä on vaikeustasoja.
* Pelin voi laittaa tauolle.
* Top 10 pelaajaa näkyy myös peliä pelatessa.
* Pelissä on ääniefektejä.
