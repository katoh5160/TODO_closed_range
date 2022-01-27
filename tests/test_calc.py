""" This is a example test program for pytest. """
import sys, pytest
sys.path.append('../')

from src.calc import Calc

class TestCalc:
    """ 動作確認用クラス """
    
    @pytest.fixture(name='calc', scope='class')
    def fixture_calc(self):
        """ calcインスタンスを返す """
        calc = Calc(4, 2)
        return calc

    def test_add(self, calc):
        """ 足し算テスト """
        assert calc.add() == 6

    def test_diff(self, calc):
        """ 引き算テス """
        assert calc.diff() == 2

    def test_multiple(self, calc):
        """ 掛け算テスト """
        assert calc.multiple() == 8

    def test_division(self, calc):
        """ 割り算テスト """
        assert calc.division() == 2
