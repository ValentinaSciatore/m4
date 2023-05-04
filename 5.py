if __name__ == '__main__':
    stringa = input("inserire una stringa")
    output = ""
    for c in stringa:
        if c == 'a':
            output += 'e'
        elif c == 'e':
            output += 'a'
        else:
            output += c

    print(output)