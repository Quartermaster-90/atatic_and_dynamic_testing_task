### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
# missing the second '=' symbol to allow the if statement to equate correctly
    if card.value = 1:
      return True
# missing colon at the end of the 'else' statement
    else
      return False
   

# define functiion (def) is misspelt, therefore rendering the function inactive;
# missing comma (,) after card1 parameter 
  dif highest_card(self, card1 card2):
# if statement indentation incorrect - needs to move > one step
  if card1.value > card2.value:
# card1 is not defined correctly
    return card
  else:
    return card2
  


# function indentation incorrect - needs to move > one step
def cards_total(self, cards):
# total variable is missing a value
  total
  for card in cards:
    total += card.value
# return indentation incorrect - needs to move < one step
# Space could be introdcued at the end of the string for clean presentation of return result
# Incorrect concatenation for the total value, which requires a str() function
    return "You have a total of" + total
  
```
