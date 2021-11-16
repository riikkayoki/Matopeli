import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksupaate = Maksukortti(800)

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)
    
    def test_kassan_rahamaara_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myytyjen_edullisten_maara_oikea(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_myytyjen_maukkaiden_maara_oikea(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # EDULLINEN
    
    def test_myyty_edullinen_lounas_raha_riittaa_kateinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(480), 240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_myyty_2_edullinen_lounas_raha_riittaa_kateinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(480), 240)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100480)
        self.assertEqual(self.kassapaate.edulliset, 2)
    
    def test_myyty_edullinen_lounas_raha_riittaa_kortti(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksupaate), True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.maksupaate.saldo, 560)
    
    def test_myyty_edullinen_lounas_raha_ei_riitä_kateinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230), 230)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_myyty_edullinen_lounas_raha_ei_riita_kortti(self):
        self.maksupaate.ota_rahaa(700)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksupaate), False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.maksupaate.saldo, 100)

    # MAUKAS

    def test_myyty_maukas_lounas_raha_riittaa_kateinen(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(800), 400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_myyty_maukas_lounas_raha_riittaa_kortti(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksupaate), True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.maksupaate.saldo, 400)
   
    def test_myyty_maukas_lounas_raha_ei_riita_kateinen(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(230),230)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_myyty_maukas_lounas_raha_ei_riita_kortti(self):
        self.maksupaate.ota_rahaa(700)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksupaate), False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.maksupaate.saldo, 100)

    # LATAUKSET
    
    def lataa_positiivinen_summa_rahaa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksupaate, 1000)
        self.assertEqual(self.maksupaate.saldo, 2000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def lataa_negatiivinen_summa_rahaa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksupaate, -1000)
        self.assertEqual(self.maksupaate.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)