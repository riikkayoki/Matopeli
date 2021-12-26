
# Arkkitehtuurikuvaus

## Rakenne

![rakenne](ot-harjoitustyo/dokumentaatio/pictures/structure.png)

## Käyttöliittymä

Käyttöliittymä sisältää 5 erilaista näkymää:

* Päävalikko
* Käyttöohjevalikko
* Tulostaulukkovalikko
* Peli
    * Pelaajan nimimerkin syöttämisikkuna

Päävalikosta käyttäjä voi valita, haluaako hän siirtyä peliin, tulostauluun vai käyttöohjeisiin. 
Pelinäkymässä pelaaja voi pelata peliä eli kääntää matoa pyrkien saamaan pisteitä osumalla omenaan.
Käyttöohjevalikossa pelaaja voi lukea pelin käyttöohjeet.
Tulostauluvalikossa pelaaja voi tarkastella edellisten pelaajien tuloksia. 

Kukin valikko on toteutettu omissa luokissaan:

* Päävalikko: `MainMenu`,
* Käyttöohjevalikko: `InstructionsMenu`,
* Tulostauluvalikko: `LeaderboardMenu`,

ja ne rakentuvat suurilta määrin pygamen visuaalisista elementeistä. 

Itse pelinäkymä rakentuu usemmasta eri luokasta. Pelin suorittaminen tapahtuu kuitenkin pääpiirtein `Game` -luokassa.
`Game` -luokka kutsuu muita pelin kannalta tärkeitä luokkia riippuen siitä mitä pelissä tapahtuu juuri sillä hetkellä.
Pelin loppuessa, näytölle ilmestyy ikkuna, jossa pelaajalle kerrotaan pelin loppuneen. Tämä on toteutettu `FormUI` -luokassa
Samassa ikkunassa pelaajaa pyydetään syöttämään nimimerkkinsä ja painamaan enter -nappia.
Nimimerkki tallentuu järjestelmään niin kauan kuin sama peli on auki, jotta saman pelaajan ei tarvitse kirjoittaa nimimerkkiänsä joka kerta uudelleen.
Pelaajalle avautuu taas tulostauluvalikko, kun hän on painanut enteriä. Tästä valikosta pääsee takaisin taas päävalikkoon.


## Tietojen pysyväistallennus

### Tietokanta

`LeaderboardRepository `-luokka huolehtii tietojen tallentamisesta SQLite-tietokantaan. 
Tietokantaan tallennetaan jokaisen pelin jälkeen pelaajan nimimerkki ja pistemäärä.
Vain top 10 -pelaajaa näytetään sovelluksen käyttäjälle. 

Pelaajan nimi ja pistemäärä tallennetaan tietokannassa `Leaderboard` -tauluun. 
Leaderboard taulu näyttää seuraavanlaiselta:

| username | points    |
|----------|-----------|
| pelaaja1 | 10        |  
| pelaaja2 | 2         |

Tietokantaan saadaan yhteys [database_connection.py](https://github.com/riikkayoki/ot-harjoitustyo/blob/master/harjoitustyo/src/database_connection.py) tiedostossa 
ja tietokanta alustetaan [initialize_database.py](https://github.com/riikkayoki/ot-harjoitustyo/blob/master/harjoitustyo/src/initialize_database.py)
tiedostossa.

## Päätoiminnallisuudet

### Käyttöohjeiden lukeminen

Kun päävalikossa painetaan nappia `INSTRUCTIONS`, sovelluksen toiminta etenee seuraavanlaisesti:

![instructions_arch](/home/salojoki/ot-harjoitustyo/dokumentaatio/pictures/instructions_architecture.png)

Painaessa `INSTRUCTIONS` -nappia ohjelma havaitsee, että `self.open_instructions`-olio on saanut arvon True.
SnakeGame -luokka kutsuu tällöin `show_instructions()` -metodia luokasta `InstructionsMenu`, 
mikä löytyy tiedostosta [instructions_menu_ui.py](https://github.com/riikkayoki/ot-harjoitustyo/blob/master/harjoitustyo/src/ui/instructions_menu_ui.py).
Päävalikkoon päästään takaisin, kun painetaan `BACK TO MENU` -nappia.

### Tulostaulun tilastojen katsominen

Kun päävalikossa painetaan nappia `LEADERBOARD`, sovelluksen toiminta etenee seuraavanlaisesti:

![leaderboard_arch](/home/salojoki/ot-harjoitustyo/dokumentaatio/pictures/leaderboard_architecture.png)

Painaessa`LEADERBOARD` -nappia ohjelma havaisee, että `self.open_leaderboard` -olio on saanut arvokseen True.
SnakeGame -luokka kutsuu tällöin `show_leaderboard()` -metodia luokasta `LeaderboardMenu`, 
mikä löytyy tiedostosta [leaderboard_menu_ui.py](https://github.com/riikkayoki/ot-harjoitustyo/blob/master/harjoitustyo/src/ui/leaderboard_menu_ui.py).
LeaderboardMenu hakee ja näyttää tiedot kymmenestä parhaasta pelaajasta `LeaderboardRepository` -luokasta, mikä löytyy tiedostosta [leaderboard_repository.py]().
Päävalikkoon päästään takaisin, kun painetaan `BACK TO MENU` -nappia.

### Pelin pelaaminen ja nimimerkin luominen

Kun päävalikossa painetaan nappia `START`, sovelluksen toiminta etenee seuraavanlaisesti:

![game_arch](/home/salojoki/ot-harjoitustyo/dokumentaatio/pictures/game_architecture.png)

Painaessa`START` -nappia, ohjelma havaitsee, että `self._start_game` on saanut arvokseen True.
SnakeGame -luokka kutsuu tällöin metodia `run_game()`. 
Kun peli loppuu, ohjelma havaitsee, että `self._stop_game` on saanut arvon True.
Tällöin SnakeGame -luokka kutsuu `show_form()` -funktiota luokasta FormUI, 
mikä löytyy tiedostosta [form_ui.py](https://github.com/riikkayoki/ot-harjoitustyo/blob/master/harjoitustyo/src/ui/form_ui.py).
Kun pelaaja on painanut kirjoittanut nimimerkkinsä tekstinsyöttyruutuun ja painanut `ENTER` -nappia, 
ohjelma havaitsee, että `self._enter` on saanut arvokseen True. 
Tämän jälkeen, ohjelma tallentaa pelaajan tuloksen tietokantaan. 
Ohjelma palaa takaisin aloitusvalikkoon tämän jälkeen.

## Rakenteeseen jääneet heikkoudet

Luokan SnakeGame olisi voinut jakaa useampaan eri tiedostoon ja luokkaan. 
Tämä olisi parantanut sekä pelin rakennetta että testattavuutta. 
SnakeGamessa on myös hieman toisteista koodissa, jotta sain testattavuuden toimimaan paremmin. 
Näiden lisäksi Pylint ilmoittaa myös, että SnakeGame -luokassa on liikaa atribuutteja.
