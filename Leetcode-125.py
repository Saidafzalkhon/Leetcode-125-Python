if __name__ == "__main__":
    s = input()
    j = ''
    for i in s:
        if i.isalpha() or i.isdigit():
            j+=i.lower()
    son = len(j)//2
    son1 = len(j)-1
    mantiq = True
    for i in range(son):
        if j[i] != j[son1]:
            mantiq = False
            break
        son1-=1
    print(mantiq)