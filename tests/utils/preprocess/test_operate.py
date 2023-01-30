from unittest import TestCase

from src.utils.preprocess.operate import preprocess


class TestPreprocess(TestCase):
    def test_preprocess1(self) -> None:
        return_value = preprocess("東京都　大田区北千束一丁目５０の１００ 大山クリーニング302号室")
        self.assertEqual(return_value, "東京都大田区北千束1/tyoume50/no100大山クリーニング302/gou室")

    def test_preprocess2(self) -> None:
        return_value = preprocess("愛媛県松番市一番町3丁目3ー6")
        self.assertEqual(return_value, "愛媛県松/ban市一/ban町3/tyoume3-6")

    def test_preprocess3(self) -> None:
        return_value = preprocess("東京都港区南青山7-1-7. C-Cube南青山ビル 6F")
        self.assertEqual(return_value, "東京都港区南青山7-1-7.C-Cube南青山ビル6F")

    def test_preprocess4(self) -> None:
        return_value = preprocess("東京都大田区西六郷4-30-7音金六郷マンション1-C号")
        self.assertEqual(return_value, "東京都大田区西六郷4-30-7音金六郷マンション1-C/gou")
