class Player:

    def __init__(self, id, current, goal):
        self.id = id
        self.current = current
        self.goal = goal
    
    def __str__(self):
        return str(self.id + " at " + str(self.current) + " with goal " + str(self.goal))
    
    def change_current(self, new_current):
        self.current = new_current
    
    def change_goal(self, new_goal):
        self.goal = new_goal