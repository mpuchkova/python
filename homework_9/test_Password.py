import Password

class TestPassword:
    def test_password_minlen(self):
        assert Password.password('ffff')=='False'

    def test_password_only_numbers(self):
        assert Password.password('1234567890')=='False'

    def test_password_word_password(self):
        assert Password.password('paSswOrd')=='False'

    def test_password_without_numbers(self):
        assert Password.password('puchkova')=='False'
    
    def test_password_true(self):
        assert Password.password('puchkova08')=='True'