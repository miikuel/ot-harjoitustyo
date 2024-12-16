# Changelog

## Viikko 3

- Lisätty UserRepository-luokka, joka vastaa käyttäjien tallennuksesta, etsimisestä ja poistamisesta (ei vielä pysyväistallennusta)
- Lisätty StudytrackerService-luokka, joka vastaa sovelluslogiikan koodista
- Yksikkötestit UserRepository-luokalle, testien haarautumakattavuus 100%
- Yksinkertainen tekstikäyttöliittymä käyttäjatunnuksen luomisen ja kirjautumisen testikäyttöön

## Viikko 4
- Implementoitu tietojen pysyväistallennus sqlite3 tietokantaan ja sen edellyttämät muutokset koodiin
- Lisätty TaskRepository-luokka, joka vastaa tehtäviin liittyvistä operaatioista sekä näihin liittyvät toiminnot lisätty StudyTracker-luokkaan
- Yksikkötestit TaskRepository-luokalle
- Lisätty mahdollisuus taskien lisäämiseen ja lisättyjen taskien katseluun sekä yleisesti paranneltu käyttöliittymää ja siirretty se omaan tiedostoon ui-kansioon

## Viikko 5
- Toteutetty graafinen käyttöliittymä TkInterillä
- Lisätty toiminnalisuus taskin tehdyksi merkkaamiseksi ja testi toiminnallisuudelle

## Viikko 6
- Lisätty filteröinti-toiminnalisuus, jossa käyttäjä pystyy valita näkymäksi joko tekemättömät, tehdyt tai kaikki taskit
- Lisätty toiminnallisuus, ettän taskin voi palauttaa tekemättömäksi
- Paranneltu graafista käyttöliittymä
- Lisätty yksikkötesti taskin tekemättömäksi palauttamiselle
- Docstring-dokumentointi, User, Task ja StudytrackerService -luokille
- Käyttöohje

## Viikko 7
- Refaktorointia ja testitietokannan määrittely
- Testit StudytrackerService -luokalle
- Testausdokumentti
- Docstring-dokumentaatio TaskRepository ja UserRepository -luokille