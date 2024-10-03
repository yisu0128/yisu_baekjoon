def solution(n, computers):
    visited = [False]*n
    def dfs(computer):
        visited[computer]=True
        if computers[computer][i] == 1 and visited[computer]==False:
            dfs(i)
    network_count = 0
    for i in range(n):
        if visited[computer]==False:
            dfs[i]
    return dfs[0]









def solution(n, computers):
    visited = [False]*n
    def dfs(computer):
        visited[computer] = True
        for i in range(n):
            if computers[computer][i] == 1 and not visited[i]:
                dfs(i)
    network_count = 0  
    for i in range(n):
        if not visited[i]:  
            dfs(i)
            network_count += 1     
    return network_count