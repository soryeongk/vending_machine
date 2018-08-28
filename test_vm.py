from vm import VendingMachine


def test_initiallize_change_should_zero():
    m = VendingMachine()
    assert '100원을 넣었습니다' == m.run('동전 100')

def test_insert_coin_and_check():
    m = VendingMachine()
    assert '100원을 넣었습니다' == m.run('동전 100')
    assert '잔액은 100원입니다' == m.run('잔액')

def test_accumulation_of_change():
    m = VendingMachine()
    m.run('동전 100')
    m.run('동전 100')
    assert '잔액은 200원입니다' == m.run('잔액')

def test_initial_change_should_be_zero():
    m = VendingMachine()
    assert '잔액은 0원입니다' == m.run('잔액')

def test_unknown_cmd():
    m = VendingMachine()
    assert '알 수 없는 명령입니다' == m.run('blah')

def test_give_me_coffee():
    m = VendingMachine()
    m.run('동전 500')
    assert '커피가 나왔습니다' == m.run('음료 커피')
    assert '잔액은 350원입니다' == m.run('잔액')
    m.run('음료 우유')
    assert '잔액은 150원입니다' == m.run('잔액')

def test_unknown_drink():
    m = VendingMachine()
    m.run('동전 500')
    assert '알 수 없는 음료입니다' == m.run('음료 맥주')
    assert '잔액은 500원입니다' == m.run('잔액')

def test_unknown_coins():
    m = VendingMachine()
    assert '알 수 없는 동전입니다' == m.run('동전 130')
    assert '잔액은 0원입니다' == m.run('잔액')
#
# def test_return_change():
#     m = VendingMachine()
#     m.run('동전 500'); m.run('동전 100'); m.run('동전 50')
#     m.run('동전 10'); m.run('동전 10')
#     assert '500원 100원 50원 10원 10원 ' == m.run('반환')

def test_milk_coffee():
    m = VendingMachine()
    m.run('동전 500')
    assert '밀크커피가 나왔습니다' == m.run('음료 밀크커피')
    assert '우유가 나왔습니다' == m.run('음료 우유')
