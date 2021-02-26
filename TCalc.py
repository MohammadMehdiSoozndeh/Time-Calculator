def add_times():
    print("\n Add Times\n enter -1 for stop\n\n")
    flag_add = True
    time_sum = 0
    while flag_add:
        temp_time = input(" input  >> ")
        if temp_time != "-1":
            temp = int(str(temp_time.split(":")[0])) * 60 + int(str(temp_time.split(":")[1]))
            time_sum = temp + time_sum
            print("                     result: " + str(int(time_sum / 60)) + ":" + str(time_sum % 60))
        else:
            print("                     result: " + str(int(time_sum / 60)) + ":" + str(time_sum % 60))
            flag_add = False
    return


def minus_times():
    print("\n minus Times\n\n")

    big_time = input(" larger time  >> ")
    small_time = input(" smaller time  >> ")

    big_time_temp = int(str(big_time.split(":")[0])) * 60 + int(str(big_time.split(":")[1]))
    small_time_temp = int(str(small_time.split(":")[0])) * 60 + int(str(small_time.split(":")[1]))
    time_sum = big_time_temp - small_time_temp
    print("                     result: " + str(int(time_sum / 60)) + ":" + str(time_sum % 60))

    return


def presence_add_times():
    print("\n enter -1 to stop\n\n")
    flag_add = True
    time_sum = 0
    while flag_add:
        temp_time = presence_minus_times()
        if temp_time != "-1":
            time_sum = temp_time + time_sum
            print("                     result: " + str(int(time_sum / 60)) + ":" + str(time_sum % 60))
        else:
            print("                     result: " + str(int(time_sum / 60)) + ":" + str(time_sum % 60))
            flag_add = False
    return


def presence_minus_times():
    big_time = input("  Exit time  >> ")
    if (big_time == "-1"):
        return "-1" 
    small_time = input("    Enter time  >> ")
    if (small_time == "-1"):
        return "-1"
        
    big_time_temp = int(str(big_time.split(":")[0])) * 60 + int(str(big_time.split(":")[1]))
    small_time_temp = int(str(small_time.split(":")[0])) * 60 + int(str(small_time.split(":")[1]))
    time_sum = big_time_temp - small_time_temp
    print("                 : " + str(int(time_sum / 60)) + ":" + str(time_sum % 60) + "\n")

    return time_sum




print("\n**** Time Calculation ****\nTime Format: 24h like: 19:05,02:36")

flag = True

while flag:
    print("\nchoose:\n 1 - add time\n 2 - minus\n 3 - presence hour\n 4 - exit\n\n")
    mood = input("\nenter: ")

    if mood == "1":
        add_times()
    elif mood == "2":
        minus_times()
    elif mood == "3":
        presence_add_times()
    else:
        flag = False
