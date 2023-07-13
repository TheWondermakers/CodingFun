def check_for_prime_number(number: int) -> bool:
    """
    Check if a given number is a prime number

    params: number (int) -> number that should be checked if it is a prime number
    """
    flag: bool = False

    if number == 1:
        flag = True

    elif number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                flag = True
                break

        # check if flag is True
        if flag:
            return False
        else:
            return True


number: int = 29
is_prime_number: bool = check_for_prime_number(number)

if is_prime_number:
    print(str(number) + ' is a prime number')
else:
    print(f'{number} is no prime number')
