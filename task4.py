# Tough exam #

n = int(input())
cards = {}
for i in range(n):
    card = input().split(":")
    cards[card[0]] = card[1]

print(cards[input()])
