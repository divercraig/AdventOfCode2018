current_frequency = 0
frequency_history = {0}
found_reoccurance = False

while not found_reoccurance:
    for line in open('input.txt'):
        change = int(line)
        new_frequency = current_frequency + change
        print("Current Frequency is {}, change of {}, resulting frequency is {}"
              .format(current_frequency, change, new_frequency)
              )
        current_frequency = new_frequency
        if current_frequency in frequency_history:
            print("The first re-occurence is {}".format(current_frequency))
            found_reoccurance = True
            break
        else:
            frequency_history.add(current_frequency)


