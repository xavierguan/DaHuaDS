cmake_minimum_required (VERSION 2.6)
project (DaHuaDS)

# c03_list
add_executable(c03_list_f01_List c03_list/f01_List.c)
add_executable(c03_list_f02_LinkList c03_list/f02_LinkList.c)
add_executable(c03_list_f03_StaticLinkList c03_list/f03_StaticLinkList.c)

# c04_stackqueue
add_executable(c04_stackqueue_f01_Stack c04_stackqueue/f01_Stack.c)
add_executable(c04_stackqueue_f02_DoubleStack c04_stackqueue/f02_DoubleStack.c)
add_executable(c04_stackqueue_f03_LinkStack c04_stackqueue/f03_LinkStack.c)
add_executable(c04_stackqueue_f04_Fibonacci c04_stackqueue/f04_Fibonacci.c)
add_executable(c04_stackqueue_f05_Queue c04_stackqueue/f05_Queue.c)
add_executable(c04_stackqueue_f06_LinkQueue c04_stackqueue/f06_LinkQueue.c)

# c05_string
add_executable(c05_string_f01_String c05_string/f01_String.c)
add_executable(c05_string_f02_KMP c05_string/f02_KMP.c)

# c06_tree
add_executable(c06_tree_f01_BiTreeArray c06_tree/f01_BiTreeArray.c)
add_executable(c06_tree_f02_BiTreeLink c06_tree/f02_BiTreeLink.c)
add_executable(c06_tree_f03_ThreadBinaryTree c06_tree/f03_ThreadBinaryTree.c)

# c07_graph
add_executable(c07_graph_f01_CreateMGraph c07_graph/f01_CreateMGraph.c)
add_executable(c07_graph_f02_CreateALGraph c07_graph/f02_CreateALGraph.c)
add_executable(c07_graph_f03_DFS_BFS c07_graph/f03_DFS_BFS.c)
add_executable(c07_graph_f04_DFS_BFS c07_graph/f04_DFS_BFS.c)
add_executable(c07_graph_f05_Prim c07_graph/f05_Prim.c)
add_executable(c07_graph_f06_Kruskal c07_graph/f06_Kruskal.c)
add_executable(c07_graph_f07_Dijkstra c07_graph/f07_Dijkstra.c)
add_executable(c07_graph_f08_Floyd c07_graph/f08_Floyd.c)
add_executable(c07_graph_f09_TopologicalSort c07_graph/f09_TopologicalSort.c)
add_executable(c07_graph_f10_CriticalPath c07_graph/f10_CriticalPath.c)

# c08_search
add_executable(c08_search_f01_Search c08_search/f01_Search.c)
add_executable(c08_search_f02_BinarySortTree c08_search/f02_BinarySortTree.c)
add_executable(c08_search_f03_AVLTree c08_search/f03_AVLTree.c)
add_executable(c08_search_f04_BTree c08_search/f04_BTree.c)
add_executable(c08_search_f05_HashTable c08_search/f05_HashTable.c)

# c09_sort
add_executable(c09_sort_f01_Sort c09_sort/f01_Sort.c)
