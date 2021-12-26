# Käyttöohje


Voit ladata harjoitustyön lähdekoodin [täältä](https://github.com/riikkayoki/ot-harjoitustyo/releases/tag/finalproject).

## Ohjelman käynnistäminen

Asenna riippuvuudet komennolla:

```
poetry install
```

Suorita alustustoimenpiteet komennolla:

```
poetry run invoke build
```

Käynnistä komennolla:

```
poetry run invoke start
```

## Pelin aloittaminen

Sovellus käyynistyy päävalikkonäkymään:

![mainmenu](./pictures/mainmenu_instructions.png)

Lue ensin pelin käyttöohjeet painamalla 'INSTRUCTIONS' -nappia tietokoneesi hiirellä.
Pääset takaisin päävalikkoon painamalla 'BACK TO MENU' -nappia tietokoneesi hiirellä:

![instructions](./pictures/instructions_instructions.png)

Katso top 10 pelaajien tuloksia painamalla 'LEADERBOARD' -nappia päävalikosta tietokoneesi hiirellä. 
Pääset takaisin painamalla BACK TO MENU -nappia tietokoneesi hiirellä:

![leaderboard](./pictures/leaderboard_instructions.png)

Voit aloittaa pelin painamalla päävalikosta nappia 'START' tietokoneesi hiirellä. 
Pelaa peliä 'INSTRUCTIONS' -valikossa olleiden käyttöohjeiden mukaisesti.

![game](./pictures/game_instructions.png)

Kun peli loppuu, paina tekstiruutua ja kirjoita nimimerkkisi siihen tietokoneesi näppäimillä. 
Paina tämän jälkeen 'enter' -nappia, jotta pääset takaisin päävalikkoon. 

![form](./pictures/form_instructions.png)
