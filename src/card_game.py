class CardGame:


  def check_for_ace(self, card):
    if card.value == 1:
      return True
    else:
      return False
   

  def highest_card(self, card1, card2):
    if card1.value > card2.value:
        return card1
    if self.value < card2.value:
        return card2
    else:
        return "The cards have the same value"
  

  def cards_total(self, cards):
    total = 0
    for card in cards:
        total += card.value
    return f"You have a total of {total}"