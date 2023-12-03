import sys

cal_strings = sys.stdin.readlines()

def cleanup(line):
    cleaned_up = ''
    idx = 0
    while idx < len(line):
        if line[idx].isdigit():
            cleaned_up += line[idx]
            idx += 1
        elif line[idx: idx + 3] == "one":
            cleaned_up += "1"
            idx += 2
        elif line[idx: idx + 3] == "two":
            cleaned_up += "2"
            idx += 2
        elif line[idx: idx + 5] == "three":
            cleaned_up += "3"
            idx += 4
        elif line[idx: idx + 4] == "four":
            cleaned_up += "4"
            idx += 4
        elif line[idx: idx + 4] == "five":
            cleaned_up += "5"
            idx += 3
        elif line[idx: idx + 3] == "six":
            cleaned_up += "6"
            idx += 3
        elif line[idx: idx + 5] == "seven":
            cleaned_up += "7"
            idx += 4
        elif line[idx: idx + 5] == "eight":
            cleaned_up += "8"
            idx += 4
        elif line[idx: idx + 4] == "nine":
            cleaned_up += "9"
            idx += 3
        elif line[idx: idx + 4] == "zero":
            cleaned_up += "0"
            idx += 3
        else:
            idx += 1
    return cleaned_up

def calibration_sum():
    cal_sum = 0
    for line in cal_strings:
        idx = 0
        while idx < len(line):
            char = line[idx]
            if char.isdigit():
                cal_sum += 10 * int(char)
                break
            idx += 1
        idx = len(line) - 1
        while idx >= 0:
            char = line[idx]
            if char.isdigit():
                cal_sum += int(char)
                break
            idx -= 1
    return cal_sum
            
def calibration_sum_with_words():
    cal_sum = 0
    for line in cal_strings:
        cal_str = cleanup(line)
        cal_val = cal_str[0] + cal_str[len(cal_str) - 1]
        cal_sum += int(cal_val)
    return cal_sum

# Part 1
print(calibration_sum())
# Part 2
print(calibration_sum_with_words())