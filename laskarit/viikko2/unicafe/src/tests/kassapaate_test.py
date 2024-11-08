import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luodun_kassapaatteen_saldo_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_luodussa_kassapaatteessa_ei_myytyja_lounaita(self):
        myydyt_lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(myydyt_lounaat, 0)

    def test_syo_edullisesti_kateisella_jalkeen_kassan_maaraa_oikein_kun_maksu_yli_hinnan(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)

    def test_syo_edullisesti_kateisella_jalkeen_kassan_maaraa_oikein_kun_maksu_tasarahalla(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)

    def test_syo_edullisesti_kateisella_jalkeen_kassan_maaraa_oikein_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_syo_edullisesti_kateisella_jalkeen_vaihtorahan_maaraa_oikein_kun_maksu_yli_hinnan(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)

    def test_syo_edullisesti_kateisella_jalkeen_vaihtorahan_maaraa_oikein_kun_maksu_tasarahalla(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(vaihtoraha, 0.0)

    def test_syo_edullisesti_kateisella_jalkeen_vaihtorahan_maaraa_oikein_kun_maksu_ei_riittava(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)

    def test_syo_edullisesti_kateisella_jalkeen_lounaiden_maara_oikein_kun_maksu_yli_hinnan(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        myydyt_lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(myydyt_lounaat, 1)

    def test_syo_edullisesti_kateisella_jalkeen_lounaiden_maara_oikein_kun_maksu_tasarahalla(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        myydyt_lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(myydyt_lounaat, 1)

    def test_syo_edullisesti_kateisella_jalkeen_lounaiden_maara_oikein_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        myydyt_lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(myydyt_lounaat, 0)

    def test_syo_maukkaasti_kateisella_jalkeen_kassan_maaraa_oikein_kun_maksu_yli_hinnan(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)

    def test_syo_maukkaasti_kateisella_jalkeen_kassan_maaraa_oikein_kun_maksu_tasarahalla(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)

    def test_syo_maukkaasti_kateisella_jalkeen_kassan_maaraa_oikein_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_syo_maukkaasti_kateisella_jalkeen_vaihtorahan_maaraa_oikein_kun_maksu_yli_hinnan(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)

    def test_syo_maukkaasti_kateisella_jalkeen_vaihtorahan_maaraa_oikein_kun_maksu_tasarahalla(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(vaihtoraha, 0.0)

    def test_syo_maukkaasti_kateisella_jalkeen_vaihtorahan_maaraa_oikein_kun_maksu_ei_riittava(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)

    def test_syo_maukkaasti_kateisella_jalkeen_lounaiden_maara_oikein_kun_maksu_yli_hinnan(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        myydyt_lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(myydyt_lounaat, 1)

    def test_syo_maukkaasti_kateisella_jalkeen_lounaiden_maara_oikein_kun_maksu_tasarahalla(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        myydyt_lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(myydyt_lounaat, 1)

    def test_syo_maukkaasti_kateisella_jalkeen_lounaiden_maara_oikein_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        myydyt_lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(myydyt_lounaat, 0)

    def test_syo_edullisesti_kortilla_palauttaa_true_kun_kortilla_tarpeeksi_rahaaa(self):
        maksukortti = Maksukortti(300)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), True)

    def test_syo_edullisesti_kortilla_jalkeen_lounaiden_maara_oikein_kun_kortilla_tarpeeksi_rahaa(self):
        maksukortti = Maksukortti(300)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        lounaiden_maara = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(lounaiden_maara, 1)

    def test_syo_edullisesti_kortilla_palauttaa_false_kun_kortilla_ei_tarpeeksi_rahaaa(self):
        maksukortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), False)

    def test_syo_edullisesti_kortilla_jalkeen_lounaiden_maara_oikein_kun_kortilla_ei_tarpeeksi_rahaa(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        lounaiden_maara = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(lounaiden_maara, 0)

    def test_syo_maukkaasti_kortilla_palauttaa_true_kun_kortilla_tarpeeksi_rahaaa(self):
        maksukortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), True)

    def test_syo_maukkaasti_kortilla_jalkeen_lounaiden_maara_oikein_kun_kortilla_tarpeeksi_rahaa(self):
        maksukortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        lounaiden_maara = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(lounaiden_maara, 1)

    def test_syo_maukkaasti_kortilla_palauttaa_false_kun_kortilla_ei_tarpeeksi_rahaaa(self):
        maksukortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), False)

    def test_syo_maukkaasti_kortilla_jalkeen_lounaiden_maara_oikein_kun_kortilla_ei_tarpeeksi_rahaa(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        lounaiden_maara = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(lounaiden_maara, 0)

    def test_syo_edullisesti_kortilla_jalkeen_saldo_oikein_kun_kortilla_riittavasti_rahaa(self):
        maksukortti = Maksukortti(300)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 60)

    def test_syo_edullisesti_kortilla_jalkeen_saldo_oikein_kun_kortilla_ei_riittavasti_rahaa(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 200)

    def test_syo_maukkaasti_kortilla_jalkeen_saldo_oikein_kun_kortilla_riittavasti_rahaa(self):
        maksukortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 100)

    def test_syo_maukkaasti_kortilla_jalkeen_saldo_oikein_kun_kortilla_ei_riittavasti_rahaa(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 200)

    def test_syo_edullisesti_kortilla_ei_muuta_kassapaatteen_saldoa(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_syo_maukkaasti_kortilla_ei_muuta_kassapaatteen_saldoa(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_lataa_rahaa_kortille_jalkeen_kortin_saldo_oikein_kun_ladattava_summa_ei_negatiivinen(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 1000)
        self.assertEqual(maksukortti.saldo_euroina(), 11.0)

    def test_lataa_rahaa_kortille_jalkeen_kortin_saldo_oikein_kun_ladattava_summa_on_negatiivinen(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -1000)
        self.assertEqual(maksukortti.saldo_euroina(), 1.0)

    def test_lataa_rahaa_kortille_jalkeen_kassassa_oikea_maara_rahaa(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1010.0)