class VendingMachine:  # 상태와 연산을 정의
    def __init__(self):
        self.change = 0

    def run(self, raw):
        tokens = raw.split(' ')
        cmd, params = tokens[0], tokens[1:]

        if cmd == '잔액':
            return '잔액은 {}원입니다'.format(self.change)
        elif cmd == '동전':
            coin = params[0]
            self.change += int(coin)
            return coin + '원을 넣었습니다'
        elif cmd == '음료':
            price = 150
            drink = params[0]
            if drink != '커피':
                return '알 수 없는 음료입니다'
            if self.change < price:
                return '잔액이 부족합니다'
            self.change -= price
            return drink + '가 나왔습니다'
        else:
            return '알 수 없는 명령입니다'

# def vm(vm_dict):
#     coin = int(input('동전을 넣어주세요: '))
#     drink = input('음료를 선택해주세요: ')
#     price = vm_dict[drink]
#     while coin >= price:
#         coin = coin - price
#         print('선택하신 음료 \'{0}\'가 나왔습니다. 잔액은 {1}원입니다.'.format(drink, coin))

#         if coin >= min(vm_dict.values()):
#             more_drink = input('음료를 더 선택하시려면 아무키나 누르세요(No = [Enter])')
#             if more_drink != '':
#                 drink = input('음료를 선택해주세요: ')
#             else:
#                 break
#         else:
#             more_coin = input('돈을 더 넣으시려면 금액을 입력하세요(No = [Enter])')
#             if more_coin == '':
#                 break
#             else:
#                 coin += int(more_coin)
#     if coin < price:
#         print('잔액이 부족합니다. 들어온 돈 : {0}원, 음료값 : {1}원'.format(coin, price))
#     print('잔액 {}원을 반환합니다.'.format(coin))
#
# vm_dict = {'밀크커피' : 150, '콜라' : 200, '사이다' : 200}
