# Hello World program in Python
"""
a ---> d ---> e <--- c
       ^
       |
       b
"""
from collections import defaultdict
adj_list = defaultdict()
#storing edge informtaiton
adj_list['a'] = ['d']
adj_list['b'] = ['d']
adj_list['c'] = ['e']
adj_list['d'] = ['e']
adj_list['e'] = []
#storing visited vertex information.
visited_list = defaultdict()
visited_list['a']=False
visited_list['b']=False
visited_list['c']=False
visited_list['d']=False
visited_list['e']=False

output_stack=[]
def topology_sort(vertex):
    if not visited_list[vertex]:
        visited_list[vertex] = True
        for neighbor in adj_list[vertex]:
            topology_sort(neighbor)
        output_stack.insert(0, vertex)
        
for vertex in visited_list:
    topology_sort(vertex)
    
print(output_stack) 
