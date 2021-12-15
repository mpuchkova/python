import Fibonacchi

class TestFibonacchi:
    def test_Fibonacchi_8(self):
        assert Fibonacchi.Fibonacchi_number(8) == 21

    def test_Fibonacchi_1(self):
        assert Fibonacchi.Fibonacchi_number(1)==1

    def test_Fibonacchi_2(self):
        assert Fibonacchi.Fibonacchi_number(2)==1

    def test_Fibonacchi_10(self):
        assert Fibonacchi.Fibonacchi_number(10)==55