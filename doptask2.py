def digital_root(number):
    if number < 10:
        return number
    final_sum = 0
    for i in str(number):
        final_sum += int(i)
    return digital_root(final_sum)
print(digital_root(889987))