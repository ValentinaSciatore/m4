if __name__ == '__main__':
    stringa = ""
    while len(stringa) < 6:
        stringa = input("inserisci una stringa superiore a 6")
    output = stringa[0:3]
    output += "..."
    output += stringa[-3:]
    print(output)