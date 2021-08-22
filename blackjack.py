import time
import random

print("< 블랙잭 게임 >")
time.sleep(1)
ruleyn = input("룰 설명을 보시겠습니까? (y/n 입력)")
if ruleyn == "y":
    print("블랙잭은 딜러와 카드를 한 장씩 받아가며 21에 가까운 수를 만드는 사람이 승리하는 게임입니다.")
    time.sleep(2)
    print("처음에는 두 장을 받고 시작하며, 두 장을 받은 뒤 원하면 카드를 더 받을 수 있습니다. 이것을 히트라고 합니다.")
    time.sleep(2)
    print("그리고, 그만 받는 것을 스테이라고 부릅니다.")
    time.sleep(2)
    print("카드의 수 계산은 A부터 10까지 1~10에 해당합니다.")
    time.sleep(2)
    print("J, Q, K는 모두 10으로 취급합니다.")
    time.sleep(2)
    print("만약 카드 수의 총합이 21을 넘으면 '버스트'라고 부르며, 게임에서 패배합니다.")
    time.sleep(2)
    print("딜러는 수의 총합이 17이 되기 이전까지 무조건 카드를 받습니다. 딜러의 드로우는 플레이어의 덱이 완성된 후 진행합니다.")
    time.sleep(2)
    print("그리고, 딜러 덱은 최초 한 장만 처음에 공개하고, 나머지는 플레이어 덱이 완성된 후 드로우하며 공개합니다.")
    time.sleep(2)
    print("또, 여기서는 A는 버스트되지 않는 이상 무조건 11으로 취급합니다.")
    time.sleep(2)
    print("여기서는 플레이어가 버스트해도 이후 딜러가 버스트하면 무승부인 것으로 취급했습니다.")
    time.sleep(2)
    print("마지막으로, 스플릿이나 더블다운 등의 룰은 애초에 판돈이 없는 버전이므로 제외했습니다.")
    time.sleep(5)

a11repdic = {"A" : 11, "J" : 10, "Q" : 10, "K" : 10}
a1repdic = {"A" : 1, "J" : 10, "Q" : 10, "K" : 10}
def totalNum(deck):
    a11tmp = sum([a11repdic.get(i,i) for i in deck])
    a1tmp = sum([a1repdic.get(i,i) for i in deck])
    if a11tmp > 21:
        return a1tmp
    else:
        return a11tmp

def printDeck(deck):
    tmtmp = [str(i) for i in deck]
    tmp = ", ".join(tmtmp)
    return tmp

time.sleep(2)
print("게임을 시작합니다.")
deck = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]*4
playerDeck = []
dealerDeck = []
time.sleep(1)
print("초기 덱을 드로우합니다.")
time.sleep(1)
random.shuffle(deck)
playerDeck.append(deck.pop())
playerDeck.append(deck.pop())
print("현재 플레이어 덱은 {}입니다.".format(printDeck(playerDeck)))
dealerDeck.append(deck.pop())
print("딜러가 받은 첫 카드는 {}입니다.".format(printDeck(dealerDeck)))
time.sleep(1)

onPlayerTurn = True
playerBust = False
while onPlayerTurn:
    playerStatus = input("무엇을 하시겠습니까? (h : 히트, s : 스테이)")
    time.sleep(1)
    if playerStatus == "h":
        print("히트를 선택하셨습니다. 카드를 드로우합니다.")
        time.sleep(1)
        playerDeck.append(deck.pop())
        print("현재 플레이어 덱은 {}입니다.".format(printDeck(playerDeck)))
        time.sleep(2)
        if totalNum(playerDeck) > 21:
            print("플레이어 버스트! 턴을 종료합니다.")
            playerBust = True
            onPlayerTurn = False
        else:
            print("현재 플레이어 덱의 수의 총합은 {}입니다. 다음 행동으로 진행합니다.".format(totalNum(playerDeck)))
            time.sleep(3)
    elif playerStatus == "s":
        print("스테이를 선택하셨습니다. 플레이어 턴을 종료합니다.")
        time.sleep(2)
        print("현재 플레이어 덱의 수의 총합은 {}입니다.".format(totalNum(playerDeck)))
        onPlayerTurn = False

onDealerTurn = True
dealerBust = False
time.sleep(2)
print("딜러 턴으로 진입합니다. 딜러가 받은 첫 카드는 {}였습니다.".format(printDeck(dealerDeck)))
while onDealerTurn:
    time.sleep(1)
    if totalNum(dealerDeck) < 17:
        print("현재 딜러 덱의 수의 총합이 17 미만입니다. 딜러 히트합니다.")
        dealerDeck.append(deck.pop())
        time.sleep(2)
        print("현재 딜러 덱은 {}입니다.".format(printDeck(dealerDeck)))
        time.sleep(3)
        if totalNum(dealerDeck) > 21:
            print("딜러 버스트! 턴을 종료합니다.")
            dealerBust = True
            onDealerTurn = False
        else:
            print("현재 딜러 덱의 수의 총합은 {}입니다. 다음 행동으로 진행합니다.".format(totalNum(dealerDeck)))
            time.sleep(2)
    else:
        print("현재 딜러 덱의 수의 총합이 17 이상이므로, 딜러 턴을 종료합니다.")
        onDealerTurn = False

time.sleep(2)
print("플레이어와 딜러의 턴이 모두 끝났으므로 게임 결과를 발표합니다.")
time.sleep(3)
if playerBust and dealerBust:
    print("플레이어와 딜러가 모두 버스트했습니다. 무승부입니다.")
elif playerBust:
    print("플레이어가 총합 {}의 버스트로 패배했습니다.".format(totalNum(playerDeck)))
elif dealerBust:
    print("딜러가 총합 {}의 버스트로 패배했습니다. 플레이어 승리!".format(totalNum(dealerDeck)))
else:
    if totalNum(playerDeck) > totalNum(dealerDeck):
        print("플레이어가 총합 {}, 딜러 총합 {}로 플레이어가 승리했습니다!".format(totalNum(playerDeck), totalNum(dealerDeck)))
    elif totalNum(playerDeck) == totalNum(dealerDeck):
        print("플레이어와 딜러의 총합이 {}로 무승부입니다.".format(totalNum(playerDeck)))
    elif totalNum(playerDeck) < totalNum(dealerDeck):
        print("플레이어 총합 {}, 딜러 총합 {}로 플레이어가 패배했습니다.".format(totalNum(playerDeck), totalNum(dealerDeck)))

time.sleep(4)
raise SystemExit