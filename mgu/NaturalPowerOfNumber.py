from math import log, modf


def check_if_number_is_power(number):
    for i in range(2, 1000):
        log_result = log(number, i)
        split = modf(log_result)
        if split[0] == 0.0 and split[1] > 1:
            print("Yes")
            print("Found: "
                  + str(i)
                  + " in power of "
                  + str(int(log_result))
                  + " is "
                  + str(number))
            break
    else:
        print("No")
        print("Not found base for " + str(number))


check_if_number_is_power(int(input()))
