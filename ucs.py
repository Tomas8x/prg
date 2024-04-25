from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    # def search(grid: Grid) -> Solution:
    #     """Find path between two points in a grid using Breadth First Search

    #     Args:
    #         grid (Grid): Grid of points
            
    #     Returns:
    #         Solution: Solution found
    #     """
    #     # Initialize a node with the initial position
    #     node = Node("", grid.start, 0)

    #     # Initialize the explored dictionary to be empty
    #     explored = {} 
        
    #     # Add the node to the explored dictionary
    #     explored[node.state] = True
        
    #     return NoSolution(explored)




    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Go Right

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        
        node = Node("", state=grid.start, cost=0, parent=None, action=None)
        
        frontier = PriorityQueueFrontier()
        frontier.add(node, node.cost)

        
        reached = {node.state: node.cost}
       


        while not frontier.is_empty():
            
            node = frontier.pop()
          
            if node.state == grid.end:
                return Solution(node, reached)
           
            successors = grid.get_neighbours(node.state)
            
            for i, new_state in successors.items():

                  
                    
                    new_cost = node.cost + grid.get_cost(new_state)

                    if new_state not in reached or new_cost < reached[new_state]:# Check if the successor is not reached

                       
                        new_node = Node("", new_state,
                                        new_cost,
                                        parent=node, action=i)
                    
                        reached[new_state] = new_cost
                        frontier.add(new_node, new_cost)
        
        return NoSolution(reached)
