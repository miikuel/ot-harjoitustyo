# Ohjelmistotekniikka, harjoitustyö

Tarkoituksena on toteuttaa kurssin esimerkkiaiheen mukainen opintojen seurantajärjestelmä, jossa käyttäjä pystyy kirjaamaan opintoihin liittyviä deadlineja ja seuraamaan niiden valmistumista. Kirjaus sisältää aiheen (esim. kurssin x laskarit), se voidaan luokitella johonkin kategoriaan (esim. kurssi y), sillä on deadline ja se voidaan merkata tehdyksi. Sovellukseen luodaan käyttäjätunnus, jolloin sovellus muistaa kunkin käyttäjän kirjaukset.

## Dokumentaatio

- [Käyttöohje](./dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Releaset](https://github.com/miikuel/ot-harjoitustyo/releases)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
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

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
