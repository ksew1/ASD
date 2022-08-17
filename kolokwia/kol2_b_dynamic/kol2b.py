# Karol Sewiło

#Mamy 3 możliowści
# jak napotkamy parkin algbo pierzemy pój albo nie
# albo znosimy ograniszanie

from kol2btesty import runtests



def f(i, fuel, p, boost, new_tab, T, L, cost, F):
    if i == L and fuel >= 0:
        F[i][fuel] = cost
        return F[i][fuel]
    if p < len(new_tab) and fuel <= 0 and not (new_tab[p][0] == i):
        F[i][fuel] = float('inf')
        return F[i][fuel]
    if T > fuel > 0 and L > i >= 0 and F[i][fuel] != -1:
        return F[i][fuel]
    if p < len(new_tab) and fuel <= 0 and new_tab[p][0] == i:
        if boost == True:
            F[i][fuel] = min(f(i+1, T-1, p+1, True, new_tab, T, L, cost + new_tab[p][1], F),
                             f(i+1, (2*T)-1, p+1, False, new_tab, T, L, cost + new_tab[p][1], F))
            return F[i][fuel]
        else:
            return f(i+1, T-1, p+1, True,new_tab, T, L, cost + new_tab[p][1], F)
    if p < len(new_tab) and new_tab[p][0] == i:
        if boost == True:
            F[i][fuel] = min(f(i+1, T-1, p+1, True,new_tab, T, L, cost + new_tab[p][1], F),
                   f(i+1, (2*T)-1, p+1, False, new_tab, T, L, cost + new_tab[p][1], F),
                   f(i+1, fuel -1, p+1, True,new_tab, T, L, cost, F))
            return F[i][fuel]
        else:
            F[i][fuel] =  min(f(i+1, T-1, p+1, True,new_tab, T, L, cost + new_tab[p][1], F),
                   f(i+1, fuel -1, p+1, True,new_tab, T, L, cost, F))
            return F[i][fuel]
    else:
        F[i][fuel] = f(i+1, fuel -1, p+1, True,new_tab, T, L, cost, F)
        return F[i][fuel]



def min_cost( O, C, T, L ):
    F = [ [-1 for _ in range(T+1)]  for _ in range(L+1)]
    new_tab = [(O[i], C[i]) for i in range(len(C))]
    new_tab.sort(key=lambda x: x[0])

    return f(0, T, 0, True, new_tab, T, L, 0, F)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = False )
