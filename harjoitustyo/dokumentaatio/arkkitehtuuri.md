
# Arkkitehtuurikuvaus

--------------

## Rakenne


--------------

## Käyttöliittymä

---------------------

Käyttöliittymä sisältää 5 erilaista näkymää:

* Päävalikko
* Käyttöohjevalikko
* Tulostaulukkovalikko
* Peli
    * Pelaajan nimimerkin syöttämisikkuna

Päävalikosta käyttäjä voi valita, haluaako hän siirtyä peliin, tulostauluun vai käyttöohjeisiin. 
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


Pelinäkymässä pelaaja kääntää matoa 

## Tietojen pysyväistallennus

----------------

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

--------------

### Käyttöohjeiden lukeminen

Kun pelaaja painaa 'INSTRUCTIONS' -nappia, ohjelma kutsuu `self.instructions.run_instructions_menu()` funktiota. 
Jos pelaaja painaa 'BACK TO MENU' -nappia, ohjelma havaitsee, että `self.go_back` -olio on saanut arvon 'True'.
Tämän jälkeen ohjelma asettaa `self.open_instructions` -olion arvoksi 'False', mikä ohjaa pelaajan takaisin päävalikkoon.


### Tulostaulun tilastojen katsominen

Kun pelaaja painaa 'LEADERBOARD' -nappia, ohjelma havaisee, että `self.open_leaderboard` -olion arvo on saanut arvon 'True' 
ja näin ohjelma kutsuu `self.leaderboard.run_leaderboard_menu()` funktiota. 
Jos pelaaja painaa 'BACK TO MENU' -nappia, ohjelma havaitsee, että `self.go_back` -olio on saanut arvon 'True'.
Tämän jälkeen ohjelma asettaa `self.open_leaderboard` -olion arvoksi 'False', mikä ohjaa pelaajan takaisin päävalikkoon.

### Pelin pelaaminen ja nimimerkin luominen

Kun pelaaja painaa 'START' -nappia, ohjelma havaitsee, että `self.start_game` on saanut arvokseen 'True' 
ja näin ohjelma `self.run_game()` ja `self.game.draw_snake_speed(200)` -funktioita. Jos mato törmää itseensä
tai peliruudun reunaan, peli loppuu ja ohjelma havaitsee, että `self.stop_game` on saanut arvon 'True'
ja näin se kutsuu `self.form.form()` -funktiota. Kun pelaaja on painanut 'enter' -nappia, ohjelma havaitsee, 
että `self.enter` on saanut arvokseen 'True'. Tämän jälkeen ohjelma kutsuu `self.reset_game()` -funktiota. 

## Rakenteeseen jääneet heikkoudet

Luokan Game olisi voinut vielä jakaa pienempiin osiin. 
