
def prime_generator(start_value=0, end_value=2):
    """
    prime_generator takes in two parameters,  a start value and an end value the returns
    a list of prime numbers from the start_value to end_value.
    
    :param start_value: type int
    :param end_value: type int
    :return: type list
    """
    start_point = start_value
    prime_numbers = [2] if (start_point <= 2 and end_value >= 2) else []

    while start_point <= end_value:
        prime = False
        divisor_number = 2
        while divisor_number < start_point:
            # print(divisor_number)
            if start_point % divisor_number != 0:
                prime = True

            else:
                prime = False
                break
            divisor_number += 1

        
        if prime:
            prime_numbers.append(start_point)

        start_point += 1

    return prime_numbers