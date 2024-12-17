# Ohjelmistotekniikka, harjoitustyö

Sovellus on kurssin esimerkkiaiheen mukainen opintojen seurantajärjestelmä, jonka avulla käyttäjä pystyy kirjaamaan opintoihin liittyviä tehtäviä, seuraamaan niiden deadlineja sekä merkkaamaan tehdyt tehtävät valmiiksi. Sovellukseen luodaan käyttäjätunnus, mikä mahdollistaa käyttäjäkohtaiset yksilölliset listaukset. Kirjaus sisältää aiheen, se voidaan luokitella johonkin kategoriaan, sillä on deadline ja valmis tehtävä voidaan merkata tehdyksi.

## Dokumentaatio

- [Käyttöohje](./dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Testausdokumentti](./dokumentaatio/testaus.md)
- [Releaset](https://github.com/miikuel/ot-harjoitustyo/releases)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Jos haluat määritellä olemassa olevan hakemiston johon SQLite-tietokantatiedostot tallennettaan, luo sovelluksen juurihakemistoon .env-tiedosto ja anna polku kansioon suhteessa juurihakemistoon. Jos konfigurointia ei tehdä, sovellus luo juurihakemistoon "data" nimisen kansion ja tallentaa tietokantatiedostot sinne. Konfiguroinnin .env-tiedostossa tulee olla seuraavanlainen:

```
DB_PATH=./kansion_nimi/
TEST_DB_PATH=./kansion_nimi/
```

3. Suorita vaadittavat alustustoimenpiteet komennolla:

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
