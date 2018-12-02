freq_changes = tuple(open("Day 01/day-01.txt", 'r'))
result_freq = 0;

#First part of the day

for freq_change in freq_changes:
    result_freq += int(freq_change)

print("Result frequency: ", result_freq)

#Second part of the day

freq_set = {0}
actual_freq = 0
searching = True

while searching:
    for freq_change in freq_changes:
        actual_freq += int(freq_change)
        print(actual_freq)
        if actual_freq in freq_set:
            print("We reached this frequency again:", actual_freq)
            searching = False
            break
        else:
            freq_set.add(actual_freq)
    print("Start frequency circle again.")

