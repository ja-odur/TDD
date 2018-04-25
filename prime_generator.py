import math
def prime_generator(start_value=0, end_value=2):
    start_point =  start_value
    prime_numbers =  [2] if start_value <= 2 else []

    while start_point <= end_value:
        end_point = math.ceil(start_point / 2) if start_point < 7 else start_point
        # print(end_point)
        prime = False
        divisor_number = 2
        while divisor_number < end_point:
            if start_point % 2 != 0 and start_point%  divisor_number  != 0:
                prime = True

            else:
                prime = False
                break

            divisor_number += 1

        if prime:
            prime_numbers.append(start_point)

        start_point += 1


    return prime_numbers