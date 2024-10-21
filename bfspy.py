# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:22:23 2024

@author: mbada
"""

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


solution = bfs(graph,(0,0),(2,0))
print('solution is', solution)