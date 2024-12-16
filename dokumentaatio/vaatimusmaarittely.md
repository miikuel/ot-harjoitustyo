# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on kurssin esimerkkiaiheen mukainen opintojen seurantajärjestelmä, jonka avulla käyttäjä pystyy kirjaamaan opintoihin liittyviä tehtäviä, seuraamaan niiden deadlineja sekä merkkaamaan tehdyt tehtävät valmiiksi. Sovellukseen luodaan käyttäjätunnus, mikä mahdollistaa käyttäjäkohtaiset yksilölliset listaukset. Kirjaus sisältää aiheen, se voidaan luokitella johonkin kategoriaan, sillä on deadline ja valmis tehtävä voidaan merkata tehdyksi.

## Käyttäjät

Kaikki soveluksen käyttäjät ovat peruskäyttäjiä samoilla käyttöoikeuksilla, sillä varsinaista tarvetta muille käyttäjärooleille ei ole.

## Käyttöliittymäluonnos

Sovellus sisältää seuraavat näkymät:
1. Kirjautumisnäkymä
2. Käyttäjätilin luomisnäkymä
3. Listatus sisäänkirjautuneen käyttäjän kirjauksista, jota voidaan filteröidä tehtävän statuksen (tehty/tekemättä/kaikki) perusteella. Näkymässä voidaan luoda myös uusia kirjauksia.

## Sovelluksen perustoiminnalisuudet

- Käyttäjä voi luoda sovellukseen käyttäjätunnuksen. Käyttäjätunnuksen tulee olla uniikki ja sisältää vähintään 4 merkkiä. Salasanan tulee olla vähintään 5 merkkiä. **tehty**
- Käyttäjä voi kirjautua sisään sovellukseen. Sovellus ilmoittaa jos käyttäjätunnus tai salasana ei täsmää tai käyttäjätunnusta ei ole olemassa. **tehty**
- Kyttäjä voi luoda uuden deadlinen antamalla sille aiheen, kategorian ja määräpäivän. **tehty**
- Käyttäjä voi merkata deadlinen tehdyksi. **tehty**
- Käyttäjä näkee listauksen kirjauksistaan. **tehty**
- Käyttäjä pystyy filteröimään listausta näyttämään joko kaikki deadlinet tai ainoastaan tekemättömät/tehdyt. **tehty**

## Jatkokehitysideoita

Perusversioita voitaisiin laajentaa esimerkiksi seuraavanlaisilla toiminnallisuuksilla:

- Listauksessa näkyy montako päivää kuhunkin deadlineen on aikaa
- Kirjausta pystyy editoimiaan
- Käyttäjä pystyy merkkaamaan valmiusasteen prosentteina keskeneräisille kirjaukselle
- Käyttäjä pystyy asettamaan kirjaukselle prioriteetin
- Värikoodaus sen perusteella, kuinka lähellä määräpäivä on
- Erilaisia lisänäkymiä, esim. kirjauksista, jotka eivät valmistuneet määräpäivään mennessä
- Filtteröinti kategorioittain
