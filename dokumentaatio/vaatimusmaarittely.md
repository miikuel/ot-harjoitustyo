# Vaatimusmäärittely

## Sovelluksen tarkoitus

Tarkoituksena on toteuttaa kurssin esimerkkiaiheen mukainen opintojen seurantajärjestelmä, jossa käyttäjä pystyy kirjaamaan opintoihin liittyviä deadlineja ja seuraamaan niiden valmistumista.
Kirjaus sisältää aiheen (esim. kurssin X laskarit), se voidaan luokitella johonkin kategoriaan (esim. kurssi y), sillä on deadline ja se voidaan merkata tehdyksi.
Sovellukseen luodaan käyttäjätunnus, jolloin sovellus muistaa kunkin käyttäjän kirjaukset.

## Käyttäjät

Kaikki soveluksen käyttäjät ovat peruskäyttäjiä samoilla käyttöoikeuksilla, sillä varsinaista tarvetta muille käyttäjärooleille ei ole.

## Käyttöliittymäluonnos

Sovellus sisältää ainakin seuraavat näkymät:
1. Kirjautumisnäkymä
2. Käyttäjätilin luomisnäkymä
3. Sisäänkirjautuneen käyttäjän listatus omista kirjauksistaan

## Sovelluksen perustoiminnalisuudet

- käyttäjä voi luoda sovellukseen käyttäjätunnuksen. Käyttäjätunnuksen tulee olla uniikki ja sisältää vähintään 5 merkkiä.
- käyttäjä voi kirjautua sisään sovellukseen. Sovellus ilmoittaa jos käyttäjätunnus tai salasana ei täsmää tai käyttäjätunnusta ei ole olemassa.
- käyttäjä voi luoda uuden deadlinen antamalla sille aiheen, kategorian ja määräpäivän
- käyttäjä voi merkata deadlinen tehdyksi
- käyttäjä näkee listauksen kirjauksistaan
- käyttäjä pystyy filteröimään listausta näyttämään joko kaikki deadlinet tai ainoastaan tekemättömät/tehdyt. Filtteröinnin voi tehdä myös kategorioittain.

## Jatkokehitysideoita

Perusversioita voitaisiin laajentaa esimerkiksi seuraavanlaisilla toiminnallisuuksilla:

- deadline-listaus näyttää montako päivää kunkin deadlinen määräpäivään on aikaa
- kirjattua deadlinea pystyy editoimiaan
- käyttäjä pystyy merkkaamaan valmiusasteen prosentteina keskeneräisille deadlineille
- käyttäjä pystyy asettaan deadlinelle prioriteetin
- värikoodaus sen perusteella, kuinka lähellä määräpäivä on
- erilaisia lisänäkymiä, esim. deadlinet, jotka eivät valmistuneet määräpäivään mennessä