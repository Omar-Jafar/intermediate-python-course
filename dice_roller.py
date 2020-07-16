def main():
    import random
    dice_rolls = int(input('How many dice would you like to roll? '))
    dice_sum = 0
    for i in range(0, dice_rolls):
        roll = random.randint(1, 6)
        dice_sum += roll
        print(f'You rolled a {roll}')
    print(f'You rolled a total of {roll}')


if __name__ == "__main__":
    main()
