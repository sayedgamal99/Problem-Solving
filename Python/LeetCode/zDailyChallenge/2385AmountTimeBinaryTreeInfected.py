import networkx as nx
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None,path):
        self.val = val
        self.left = left
        self.right = right
        self.path = path

class Solution:
    # def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
    def tree_to_graph(self,root,parent,graph):
        graph[root.val]=[]

        if root.right != None:
            graph[root.val].append(root.right.val)
            self.tree_to_graph(root.right,root,graph)

        if root.left != None:
            graph[root.val].append(root.left.val)
            self.tree_to_graph(root.left, root,graph)

        if parent != None :
            graph[root.val].append(parent.val)

        return graph
    

    graph = nx.Graph()
    myMap = tree_to_graph()
    for key in myMap:
        for vv in myMap[key]:
            graph.add_edge(key, vv)
            
    def breadth_first_search_visited(graph, start, goal):
        print('Searching...')
        node = TreeNode(start,left=None,right=None, path=[start])
        queue_list = [node]

        while queue_list != []:
            node = queue_list.pop(0)
            print(node.val)
            if node.val == goal:
                return node.path
            
            else:
                print('Expanding node: ', node.val)
                print('path so far: ', node.path)

                for child in graph.neighbors(node.val):
                    if child not in node.path:
                        queue_list.append(TreeNode(child, node.path+[child]))

                print('Queue content now: ', queue_list)
        return 'Not Found'

print(Solution().tree_to_graph([1, 5, 3, None, 4, 10, 6, 9, 2],parent=None,graph=dict()))
