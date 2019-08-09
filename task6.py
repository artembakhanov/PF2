# Relatives #

def dfs(graph, used, cur):
    used[cur] = True
    for adj in graph[cur]:
        if not used[adj]:
            dfs(graph, used, adj)


graph = [[], []]
names = {"Polina": 0, "Max": 1}

n = int(input())
for i in range(n):
    rel1, rel2 = input().split()
    if rel1 not in names:
        names[rel1] = len(graph)
        graph.append([])
    if rel2 not in names:
        names[rel2] = len(graph)
        graph.append([])

    graph[names[rel1]].append(names[rel2])
    graph[names[rel2]].append(names[rel1])

used = [False] * len(graph)
dfs(graph, used, 0)
print("He is!" if used[1] else "idk")
