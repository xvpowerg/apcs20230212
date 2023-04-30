def bfs(node):
    ''' 廣度優先搜尋法 '''
    global graph, queue, visited
    if node not in visited:
        visited.append(node)            # 加入已拜訪行列 
        for n in graph[node]:           # 取得已拜訪節點的相鄰節點
            if n not in visited:
                queue.append(n)         # 將相鄰節點放入佇列
    if not queue and visited:
        return
    else:
        nextNode = queue.pop(0)         # 取索引0的值
        bfs(nextNode)

graph = {'V0':['V1', 'V2'],
         'V1':['V0', 'V3', 'V4'],
         'V2':['V0', 'V5', 'V6'],
         'V3':['V1', 'V7',],
         'V4':['V1', 'V7',],
         'V5':['V2', 'V7',],
         'V6':['V1', 'V7',],
         'V7':['V3', 'V4', 'V5', 'V6',]}
visited = []                            # 拜訪過的頂點
queue = []                              # 模擬佇列
bfs('V0')
print(visited)
