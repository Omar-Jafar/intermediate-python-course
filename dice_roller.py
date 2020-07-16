def main():
    import random
    dice_rolls = 2
    for i range(0,dice_rolls):
        dice_sum = 0
        roll = random.randint(1,6)
        dice_sum += roll
        print(f'You rolled a total of {roll}')
if __name__== "__main__":
  main()
