from zad2ktesty import runtests

def palindrom( S ):
    T = [[0 for _ in range(len(S))] for _ in range(len(S))]
    for i in range(len(S)-1):
        T[i][i] = True
        if S[i] == S[i+1]:
            T[i][i+1] = True
    T[len(S)-1][len(S)-1] = True
    for i in range(len(S)-1):
        a = i
        b = i
        while a >= 0 and b < len(S):
            try:
                if S[a] == S[b] and T[a+1][b-1] is True:
                    T[a][b] = True
                else:
                    T[a][b] = False
                b += 1
                a -= 1
            except:
                print(len(S))
                print(a, b)


    max_l = (0, 1)
    for a in range(len(S)):
        for b in range(len(S)):
            if T[a][b] is True and b - a > max_l[1] - max_l[0]:
                max_l = (a, b)

    return S[max_l[0]:max_l[1] + 1]


runtests ( palindrom )