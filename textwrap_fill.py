#textwap.fill
def textwrap_fill(s,n):
    for i in range((len(s)//n)+1):
        print(s[i*n:(i+1)*n])

textwrap_fill('ABCDEFGHIJKLMNOPQRSTUVWXYZ',4)
