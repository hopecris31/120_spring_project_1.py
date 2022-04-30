import hands as h
import deck as d
import poker_sim as p

new_deck = d.create_deck()
d.shuffle(new_deck)

#print(h.deal(new_deck))
#print(p.deal_round(10))

#print(h.deal(new_deck))
#print(h.deal(new_deck))

hand = ['3H', '3C', '3S', '8C', '9C'] # false
hand2 = ['3H', '3C', '3S', '3S', '9C'] # true
hand3 = ['3H', '3C', '8S', '8C', '9C'] # true
hand4 = ['3H', '3C', '3S', '8C', '9C'] # false
hand5 = ['3H', '3C', '4S', '4C', '9C'] # true

print(h.is_two_pair(hand))
print(h.is_two_pair(hand2))
print(h.is_two_pair(hand3))
print(h.is_two_pair(hand4))
print(h.is_two_pair(hand5))
