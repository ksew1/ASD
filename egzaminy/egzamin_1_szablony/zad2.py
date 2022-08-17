from zad2testy import runtests
from queue import PriorityQueue
def dijsktra(G, W, A):
    steps = ((-1, 0), (1, 0), (0, -1), (0, 1))
    D = [[[[float('inf') for _ in range(3)] for _ in range(4)] for _ in range(len(G))] for _ in range(G)]
    V = [[[[False for _ in range(3)] for _ in range(4)] for _ in range(len(G))] for _ in range(G)]

    q = PriorityQueue()
    for i in range(4):
        for j in range(3):
            D[A[0]][A[1]][i][j] = 0
            V[A[0]][A[1]][i][j] = True
    q.put((0, A, (0, 0), 0))
    """while q.empty() is False:
        _, u, f, k = q.get()
        V[u[0]][u[1]][f][k] = True
        for s in steps:
            v = (u[0]+s[0], u[1]+s[1] )
            #if G[v[0]][v[1]] == ' ' and V[v[0]][v[1]][3] is False:
            #    if f == s:
            #        if k == 2:
            #            w = 30
            #        elif k == 1:
            #            w = 40
            #        else:
            #            w = 60
            #    else:
            #        w = 45

                if D[v[0]][v[1]] > D[u] + w:
                    D[v] = D[u] + w:
                    q.put((D[v],v))
    print(W)

def robot( L, A, B ):


    return 0

    
runtests( robot )"""


