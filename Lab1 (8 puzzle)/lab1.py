from myalgo import *
import time
import sys
import os


# this function opens a file with the given path and read
# the 8 puzzle lines into a tuple
def read_file(name):

    with open(name) as f:
        l = f.readlines()
        arr = []
        for i in l:
            x = i.split()
            for j in x:
                if j == '_':
                    arr.append(0)
                    continue
                arr.append(int(j))
        tuple1 = tuple(arr)
        #print(tuple1)
        return tuple1

#this function convert an array to a string and return the string
def convert(s):
    # initialization of string to ""
    new = ""

    # traverse in the string
    for x in s:
        new += x

    # return string
    return new

# use for terminal input the path and algorithm
file_path = sys.argv[1]
alg = sys.argv[2]

# file_path = "/Users/benjaminlee/Desktop/572Lab/Part3/L8/152.txt"
# alg = "h3"
#check if each file is a .txt file
if file_path.endswith(".txt"):
    #implement the read_file function with the given filepath
    #problem will give a tuple of the order of the tiles
    problem = read_file(file_path)
    #check_sol will give a true or false statement to see if
    #the tuple can be solvable.
    check_sol = EightPuzzle(problem).check_solvability(problem)
    #alg is the algorithm being used(bfs, ids, h1, h2 or h3)
    #set the intended algorithm to be used here
    if check_sol:
        #this is for bfs algorithm
        if alg.lower() == "bfs":
            #print(fPath)
            print("BFS")
            #create a 8 puzzle object
            puzzle = EightPuzzle(problem)
            try:
                #run the breadth_first_graph_search() function
                #will return an array of actions
                arr = breadth_first_graph_search(puzzle).solution()
            except:
                pass
            try:
                if (len(arr) > 0):
                    newarr = []
                    #the for loop extract the first character of each
                    #element in the array
                    for i in arr:
                        newarr.append(i[0])
                    #print the path length and the path
                    print("Path Length: " + str(len(newarr)))
                    print("Path: " + convert(newarr))
            except:
                pass
        # this is for ids algorithm
        elif alg.lower() == "ids":
            #print(fPath)
            print("IDS")
            # create a 8 puzzle object
            puzzle = EightPuzzle(problem)
            try:
                # run the iterative_deepening_search() function
                # will return an array of actions
                arr = iterative_deepening_search(puzzle).solution()
            except:
                pass
            try:
                if(len(arr) > 0):
                    newarr = []
                    # the for loop extract the first character of each
                    # element in the array
                    for i in arr:
                        newarr.append(i[0])
                    # print the path length and the path
                    print("Path Length: " + str(len(newarr)))
                    print("Path: " + convert(newarr))
            except:
                pass
        # this is for h1 algorithm
        elif alg.lower() == "h1":
            print("h1")
            # create a 8 puzzle object
            puzzle = EightPuzzle(problem)
            try:
                # run the astar_search() function with misplaced title heuristic
                # will return an array of actions
                arr = astar_search(puzzle).solution()
            except:
                pass
            try:
                if (len(arr) > 0):
                    newarr = []
                    # the for loop extract the first character of each
                    # element in the array
                    for i in arr:
                        newarr.append(i[0])
                    # print the path length and the path
                    print("Path Length: " + str(len(newarr)))
                    print("Path: " + convert(newarr))
            except:
                pass
        # this is for h2 algorithm
        elif alg.lower() == "h2":
            print("h2")
            # create a 8 puzzle object
            puzzle = EightPuzzle(problem)
            try:
                # run the astar_search() function with Manhattan distance heuristic
                # will return an array of actions
                arr = astar_search(puzzle, h=manhattan).solution()
            except:
                pass
            try:
                if (len(arr) > 0):
                    newarr = []
                    # the for loop extract the first character of each
                    # element in the array
                    for i in arr:
                        newarr.append(i[0])
                    # print the path length and the path
                    print("Path Length: " + str(len(newarr)))
                    print("Path: " + convert(newarr))
            except:
                pass
        # this is for h3 algorithm
        elif alg.lower() == "h3":
            print("h3")
            # create a 8 puzzle object
            puzzle = EightPuzzle(problem)
            try:
                # run the astar_search() function with square root Manhattan distance heuristic
                # will return an array of actions
                arr = astar_search(puzzle, h=h3_heuristic).solution()
            except:
                pass
            try:
                if (len(arr) > 0):
                    newarr = []
                    # the for loop extract the first character of each
                    # element in the array
                    for i in arr:
                        newarr.append(i[0])
                    # print the path length and the path
                    print("Path Length: " + str(len(newarr)))
                    print("Path: " + convert(newarr))
            except:
                pass
        #if other algorithm were type in alg
        else:
            print("No such Algorithm")
    #if problem is not solvable. Execute the code below
    else:
        print("The inputted puzzle is not solvable")
        not_solve = []
        for i in problem:
            if i == 0:
                not_solve.append("_")
            else:
                not_solve.append(str(i))
        x = 0
        print(not_solve[x] + " " + not_solve[x + 1] + " " + not_solve[x + 2])
        x += 3
        print(not_solve[x] + " " + not_solve[x + 1] + " " + not_solve[x + 2])
        x += 3
        print(not_solve[x] + " " + not_solve[x + 1] + " " + not_solve[x + 2])

    print("")
    print("")








# for loop to go into each .txt file in a folder given a file path to the folder
# for filename in os.listdir("/Users/benjaminlee/Desktop/572Lab/Part3/L24/"):
#     #check if each file is a .txt file
#     if filename.endswith(".txt"):
#         #fd is the filepath, but with the filename in it
#         #this is where the filepath should be
#         file_path = "/Users/benjaminlee/Desktop/572Lab/Part3/L24/" + filename
#         # alg is the algorithm being used(bfs, ids, h1, h2 or h3)
#         # set the intended algorithm to be used here
#         alg = "h2"
#         print(file_path)
#         #implement the read_file function with the given filepath
#         #problem will give a tuple of the order of the tiles
#         problem = read_file(file_path)
#         #check_sol will give a true or false statement to see if
#         #the tuple can be solvable.
#         check_sol = EightPuzzle(problem).check_solvability(problem)
#
#         if check_sol:
#             #this is for bfs algorithm
#             if alg.lower() == "bfs":
#                 #print(fPath)
#                 print("BFS")
#                 #create a 8 puzzle object
#                 puzzle = EightPuzzle(problem)
#                 try:
#                     #run the breadth_first_graph_search() function
#                     #will return an array of actions
#                     arr = breadth_first_graph_search(puzzle).solution()
#                 except:
#                     pass
#                 try:
#                     if (len(arr) > 0):
#                         newarr = []
#                         #the for loop extract the first character of each
#                         #element in the array
#                         for i in arr:
#                             newarr.append(i[0])
#                         #print the path length and the path
#                         print("Path Length: " + str(len(newarr)))
#                         print("Path: " + convert(newarr))
#                 except:
#                     pass
#             # this is for ids algorithm
#             elif alg.lower() == "ids":
#                 #print(fPath)
#                 print("IDS")
#                 # create a 8 puzzle object
#                 puzzle = EightPuzzle(problem)
#                 try:
#                     # run the iterative_deepening_search() function
#                     # will return an array of actions
#                     arr = iterative_deepening_search(puzzle).solution()
#                 except:
#                     pass
#                 try:
#                     if(len(arr) > 0):
#                         newarr = []
#                         # the for loop extract the first character of each
#                         # element in the array
#                         for i in arr:
#                             newarr.append(i[0])
#                         # print the path length and the path
#                         print("Path Length: " + str(len(newarr)))
#                         print("Path: " + convert(newarr))
#                 except:
#                     pass
#             # this is for h1 algorithm
#             elif alg.lower() == "h1":
#                 print("h1")
#                 # create a 8 puzzle object
#                 puzzle = EightPuzzle(problem)
#                 try:
#                     # run the astar_search() function with misplaced title heuristic
#                     # will return an array of actions
#                     arr = astar_search(puzzle).solution()
#                 except:
#                     pass
#                 try:
#                     if (len(arr) > 0):
#                         newarr = []
#                         # the for loop extract the first character of each
#                         # element in the array
#                         for i in arr:
#                             newarr.append(i[0])
#                         # print the path length and the path
#                         print("Path Length: " + str(len(newarr)))
#                         print("Path: " + convert(newarr))
#                 except:
#                     pass
#             # this is for h2 algorithm
#             elif alg.lower() == "h2":
#                 print("h2")
#                 # create a 8 puzzle object
#                 puzzle = EightPuzzle(problem)
#                 try:
#                     # run the astar_search() function with Manhattan distance heuristic
#                     # will return an array of actions
#                     arr = astar_search(puzzle, h=manhattan).solution()
#                 except:
#                     pass
#                 try:
#                     if (len(arr) > 0):
#                         newarr = []
#                         # the for loop extract the first character of each
#                         # element in the array
#                         for i in arr:
#                             newarr.append(i[0])
#                         # print the path length and the path
#                         print("Path Length: " + str(len(newarr)))
#                         print("Path: " + convert(newarr))
#                 except:
#                     pass
#             # this is for h3 algorithm
#             elif alg.lower() == "h3":
#                 print("h3")
#                 # create a 8 puzzle object
#                 puzzle = EightPuzzle(problem)
#                 try:
#                     # run the astar_search() function with square root Manhattan distance heuristic
#                     # will return an array of actions
#                     arr = astar_search(puzzle, h=h3_heuristic).solution()
#                 except:
#                     pass
#                 try:
#                     if (len(arr) > 0):
#                         newarr = []
#                         # the for loop extract the first character of each
#                         # element in the array
#                         for i in arr:
#                             newarr.append(i[0])
#                         # print the path length and the path
#                         print("Path Length: " + str(len(newarr)))
#                         print("Path: " + convert(newarr))
#                 except:
#                     pass
#             #if other algorithm were type in alg
#             else:
#                 print("No such Algorithm")
#         #if problem is not solvable. Execute the code below
#         else:
#             print("The inputted puzzle is not solvable")
#             not_solve = []
#             for i in problem:
#                 if i == 0:
#                     not_solve.append("_")
#                 else:
#                     not_solve.append(str(i))
#             x = 0
#             print(not_solve[x] + " " + not_solve[x + 1] + " " + not_solve[x + 2])
#             x += 3
#             print(not_solve[x] + " " + not_solve[x + 1] + " " + not_solve[x + 2])
#             x += 3
#             print(not_solve[x] + " " + not_solve[x + 1] + " " + not_solve[x + 2])
#
#         print("")
#         print("")