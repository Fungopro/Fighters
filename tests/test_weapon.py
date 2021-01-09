import unittest
import Weapon.Swords.Sword as Sword
import Weapon.LongBow.Bow as Bow


class TestWeaponMethods(unittest.TestCase):

    def test_Sword_Deal_Dmg(self):
        sw = Sword.Sword('HellSword', 20)
        self.assertTrue(sw.dmg_deal() in (18, 20))

    def test_Sword_Get_Dmg(self):
        sw = Sword.Sword('HellSword', 20)
        self.assertEqual(sw.get_dmg(), 20)

    def test_Bow_Deal_Dmg(self):
        bw = Bow.LongBow('jungle bow', 20, .9)
        dmg = bw.dmg_deal()
        self.assertTrue(dmg == 18 or dmg == 0)

    def test_Bow_Get_Dmg(self):
        bw = Bow.LongBow('jungle bow', 20, .9)
        self.assertEqual(bw.get_dmg(), 18)


if __name__ == '__main__':
    unittest.main()