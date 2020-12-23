# n: 頂点数
# g[v] = {(w, cost)}:
#     頂点vから遷移可能な頂点(w)とそのコスト(cost)
# s: 始点の頂点

from heapq import heappush, heappop
INF = float("inf")

def dijkstra(n, g, s):
    dist = [INF] * n
    que = [(0, s)]
    dist[s] = 0
    while que:
        c, v = heappop(que)
        if dist[v] < c:
            continue
        for t, cost in g[v]:
            if dist[v] + cost < dist[t]:
                dist[t] = dist[v] + cost
                heappush(que, (dist[t], t))
    return dist
