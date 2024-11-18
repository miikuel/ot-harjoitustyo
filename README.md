# Ohjelmistotekniikka, harjoitustyö

Tarkoituksena on toteuttaa kurssin esimerkkiaiheen mukainen opintojen seurantajärjestelmä, jossa käyttäjä pystyy kirjaamaan opintoihin liittyviä deadlineja ja seuraamaan niiden valmistumista. Kirjaus sisältää aiheen (esim. kurssin x laskarit), se voidaan luokitella johonkin kategoriaan (esim. kurssi y), sillä on deadline ja se voidaan merkata tehdyksi. Sovellukseen luodaan käyttäjätunnus, jolloin sovellus muistaa kunkin käyttäjän kirjaukset.

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.