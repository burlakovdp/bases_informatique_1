def ft_ascii():
    counter = 0
    for i in range(ord(' '), ord('~')+1):
        counter += 1
        if i < 100:
            print(' ', end='')
            print(ord(chr(i)), chr(i), end='    ')
        else:
            print(ord(chr(i)), chr(i), end='    ')
        if counter % 8 == 0 and counter != 0:
            print()