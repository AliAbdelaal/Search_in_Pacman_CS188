# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from pacman import GameState


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    """"VERSION 1"""
    "My pseudocode"
    """
    stack  <- home_state
    closed <- home_state
    state  <- home_state
    loop
        if state is goal :
            return directions
        for child in getChilds(state):
            if child not in closed :
                stack  <- child
                closed <- child
                state  <- child
                break
        if no free child :
            pop from stack
            state <- stack.peek
    end
    """
    # stack = util.Stack()
    # closed =[]
    # free_child = False
    # state = [problem.getStartState(),]
    # stack.push(state)
    # closed.append(state[0])
    # while True:
    #
    #     "########DEBUG########"
    #     # print "\n\n#######DEBUG#########"
    #     # print "stack peek :",stack.peek()
    #     # print "closed states:",closed
    #     # print "cur_state:",state
    #     # print "#######DEBUG#########\n\n"
    #     #okay = input("procceed ?")
    #     if problem.isGoalState(state[0]):
    #         "here goes the returning part"
    #         "########DEBUG########"
    #         #print "\n\n\n****i think i found it !"
    #         directions =[]
    #         "########DEBUG########"
    #         #size = stack.getSize()
    #         while not stack.isEmpty():
    #             element = stack.pop()
    #             if len(element) > 1:
    #                 #print element
    #                 directions.insert(0,element[1])
    #         #directions.remove(directions[0])
    #         "########DEBUG########"
    #         #print directions
    #         #print "size is ",size
    #         return directions
    #
    #     free_child = False
    #
    #     for child in problem.getSuccessors(state[0]):
    #         if child[0] not in closed :
    #             free_child = True
    #             "########DEBUG########"
    #             #print "found a free child !"
    #             stack.push(child)
    #             closed.append(child[0])
    #             state = child
    #             break
    #     if not free_child:
    #         "########DEBUG########"
    #         #print "no free child were found !"
    #         stack.pop()
    #         state = stack.peek()
    """VERSION 2"""
    """
     My pseudocode
     queue <- home,prio=0
     closed <- empty
     priority = 9999
     loop
         state <- queue.pop()
         if state not in closed :
             if state is goal :
                 return victory
             closed <- state
             priority -=1
             for child in getChilds(state):
                 queue.push(child,priority)
     end

     """
    queue = util.PriorityQueue()
    closed = []
    priority = 9999
    homeState = [problem.getStartState(), ]
    queue.push(homeState, priority)

    while True:
        state = queue.pop()

        "####DEBGUG#####"
        # print 'state is: ',state
        # print "state len: ",len(state)
        # print type(state)
        # print type(state[0])
        # print type(state[1])
        # okay = input("okay?")

        if state[0] not in closed:
            if problem.isGoalState(state[0]):
                "####DEBGUG#####"
                # print "wining solution is:", state[1]
                # okay = input("solution found !\nin theory :D")
                return state[1]
            closed.append(state[0])
            priority -= 1
            for child in problem.getSuccessors(state[0]):
                new_state = [child[0], []]
                if len(state) > 1:
                    for direction in state[1]:
                        new_state[1].append(direction)
                new_state[1].append(child[1])
                # print "new State :", new_state
                queue.push(new_state, priority)


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    """
    My pseudocode
    queue <- home,prio=0
    closed <- empty
    priority = 0
    loop
        state <- queue.pop()
        if state not in closed :
            if state is goal :
                return victory
            closed <- state
            priority +=1
            for child in getChilds(state):
                  queue.push(child,priority)
    end

    """

    "*** YOUR CODE HERE ***"
    queue = util.PriorityQueue()
    closed = []
    directions = util.PriorityQueue()
    priority = 0

    homeState = problem.getStartState()
    startDir  = []
    queue.push(homeState, priority)
    directions.push(startDir,priority)

    while True:
        state = queue.pop()
        direction = directions.pop()
        # print "last direction list is :", direction
        # print "BFS current state:",state
        # print "directions :",direction
        # input("okay?")

        "####DEBGUG#####"
        # print 'state is: ',state
        # print "state len: ",len(state)
        # print type(state)
        # print type(state[0])
        # print type(state[1])
        # okay = input("okay?")

        if state not in closed:
            if problem.isGoalState(state):
                "####DEBGUG#####"
                # print "to go to",state
                # print "wining solution is:", direction
                # okay = input("solution found !\nin theory :D")
                return direction
            closed.append(state)
            priority += 1
            for child in problem.getSuccessors(state):
                new_state = child[0]
                new_direction = []
                for oneWay in direction:
                    new_direction.append(oneWay)
                if isinstance(child[1],list):
                    for oneWay in child[1]:
                        new_direction.append(oneWay)
                else:
                    new_direction.append(child[1])
                queue.push(new_state, priority)
                directions.push(new_direction,priority)


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    "VERSION 1"
    """My pseudocode

    queue  <- home,priority=0
    closed <- empty
    loop
        state <- queue.pop()
        if state not in closed:
            if state is goal:
                claim vectory
            closed <- state
            for child in getChilds(state):
                priority = state[cost]+child[cost]
                queue.push(child,priority)
    end
    """
    queue = util.PriorityQueue()
    closed = []
    state = [problem.getStartState(), [], 0]
    queue.push(state, 0)
    while True:
        state = queue.pop()

        "####DEBGUG#####"
        # print 'state is: ',state
        # print "state len: ",len(state)
        # for item in state:
        #    print item,"of type",type(item)
        # input("okay?")


        if state[0] not in closed:
            if problem.isGoalState(state[0]):
                """claim victory!!"""
                "####DEBGUG#####"
                # print "road:",state[1],"cost:",state[2]
                # input("found solution in theory")
                return state[1]
            closed.append(state[0])
            for child in problem.getSuccessors(state[0]):
                priority = state[2] + child[2]
                new_state = [child[0], []]
                if len(state[1]) >= 1:
                    for direction in state[1]:
                        new_state[1].append(direction)
                new_state[1].append(child[1])
                new_state.append(priority)
                "####DEBGUG#####"
                # print "like father :",state
                # print "like son :",new_state
                # input("okay?")
                queue.push(new_state, priority)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    "VERSION 1"
    """My pseudocode

    queue  <- home,priority=0
    closed <- empty
    loop
        state <- queue.pop()
        if state not in closed:
            if state is goal:
                claim vectory
            closed <- state
            for child in getChilds(state):
                priority = heuristic(child)+total_cost
                queue.push(child,priority)
    end
    """
    queue = util.PriorityQueue()
    closed = []
    state = [problem.getStartState(), [], 0]
    queue.push(state, heuristic(problem.getStartState(), problem))
    while True:
        state = queue.pop()

        "####DEBGUG#####"
        # print 'state is: ',state
        # print "state len: ",len(state)
        # for item in state:
        #    print item,"of type",type(item)
        # input("okay?")


        if state[0] not in closed:
            if problem.isGoalState(state[0]):
                """claim victory!!"""
                "####DEBGUG#####"
                # print "road:",state[1],"cost:",state[2]
                # input("found solution in theory")
                return state[1]
            closed.append(state[0])
            for child in problem.getSuccessors(state[0]):
                priority = heuristic(child[0], problem) + state[2] + child[2]
                total_cost = state[2] + child[2]
                new_state = [child[0], []]
                if len(state[1]) >= 1:
                    for direction in state[1]:
                        new_state[1].append(direction)
                new_state[1].append(child[1])
                new_state.append(total_cost)
                "####DEBGUG#####"
                # print "like father :",state
                # print "like son :",new_state
                # input("okay?")
                queue.push(new_state, priority)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
