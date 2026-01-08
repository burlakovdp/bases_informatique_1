def justification_a_gauche(s, n):
    counter = 0
    counter_save = 0
    line = ''
    line_save= ''
    for i in range(len(s)):
        if s[i] == ' ':
            if counter + counter_save < n:
                counter_save += counter
                line_save += line
                line = ''
                counter = 0
            elif counter + counter_save == n:
                line_save += line
                print(line_save)
                counter = 0
                counter_save = 0
                line = ''
                line_save = ''
            elif  counter + counter_save > n:
                counter_save = 0
                print(line_save)
                line_save = line
                counter = len(line_save)
                line = ''
        line += s[i]
        counter += 1
        if i == len(s)-1:
            line_save += line
            print(line_save)
                