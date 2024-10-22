def dfs (graphh,currSta,goal):
        done=[]
        stack = [[currSta]]
        print(stack)
        
        while stack:
            #print(stack)
            path = stack.pop()
            node = path[-1]
            
            if node in done:
                continue
            done.append(node)
            if node == goal:
                return path
            else:
                adjacent_nodes = graphh.get(node , [])
                
                for node2 in adjacent_nodes:
   
                    new_path = path.copy()
                    new_path.append(node2)
                    stack.append(new_path)
def bfs (graph , start , goal):
    done=[]    
    queue = [[start]]
    while queue:    
        path = queue.pop(0)  
        node = path[-1]
        if node in done:
            continue
        done.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node , [])
            for node2 in adjacent_nodes:

                new_path = path.copy()
                new_path.append(node2)
                queue.append(new_path)
graph={}
graph = {
    
    (0,0):[(4,0), (0,3)],
    (0,1):[(1,0),(4,1),(0,0)],
    (0,2):[(2,0),(4,2),(0,0)],
    (0,3):[(3,0),(4,3),(0,0)],
    (1,0):[(0,1),(1,3),(0,0)],
    (1,3):[(4,0),(0,3),(1,0)],
    (2,0):[(0,2),(2,3),(0,0)],
    (2,3):[(4,1),(0,3),(2,0)],
    (3,0):[(0,3),(3,3),(0,0)],
    (3,3):[(4,2),(0,3),(3,0)],
    (4,0):[(1,3),(4,3),(0,0)],
    (4,1):[(2,3),(0,1),(4,0)],
    (4,2):[(3,3),(4,0),(0,2)],
    (4,3):[(0,3),(4,0)]
  }
"""
n=int(input("Enter the number of Nodes : "))
for i in range(n):
    nName=input("Enter the name of the "+str(i+1)+"'th Node :")
    m=int(input("Enter the number of the Nodes for the "+str(i+1)+"'th Node :"))
    subg=set()
    for s in range(m):
        e=input("Enter the name of the Node :")
        subg.add(e)
    graph[nName]=subg
init=input("Enter the inital State : ")
goal=input("Enter the Goal state : ")
"""
#if(input("choose bfs or dfs :")=="dfs"):
print("BFS :"+str(bfs(graph,(0,0),(4,1))))
#else:
print("DFS :"+str(dfs(graph,(0,0),(4,1))))