import random
import numpy as np
from numpy.core.fromnumeric import size
from person import Person
from virus_util import Virus

class Population(object):
    """
    Class representing the self.person.persons 
    """

    #_instance = Population()
    # def getInstance():
    #     return Population._instance

    def __init__(self, size: int, x_bounds: list, y_bounds: list, r: float, k: float):
        self.person = Person(size) 
        self.virus  = Virus()
        self.size         = size
        self.x_bounds     = x_bounds
        self.y_bounds     = y_bounds
        self.k            = k
        self.r            = r
        self.destinations = np.zeros((size, 2))
        self.initialize_persons()

    def initialize_persons(self):

        ID = list(range(1,self.size + 1))
        self.person.persons[:,0] = ID


        ages = np.int32(np.random.normal(loc=45, scale= 30, size=self.size))

        x_bound_list = np.random.uniform(low=self.x_bounds[0] + 0.1, 
                                            high=self.x_bounds[1] - 0.1, size=self.size)
        y_bound_list = np.random.uniform(low=self.y_bounds[0] + 0.1, 
                                            high=self.y_bounds[1] - 0.1, size=self.size)

        g_value = np.random.normal(loc=self.r, scale=(1/self.k),size=self.size)
        g_value[g_value<0] = 0.00000



        self.person.set_age(ages)

        self.person.set_x_axis(x_bound_list)
        self.person.set_y_axis(y_bound_list)

        self.person.persons = self.update_persons(self.person.persons, self.size, 1, 1, )


    def update_persons(self, person :np.array, size, speed=0.1, heading_update_chance=0.02, speed_update_chance=0.1):

        update = np.random.random(size=(size,))

        shp = update[update <= heading_update_chance].shape
        person[:,4][update <= heading_update_chance] = np.random.normal(loc = 0, scale = 1/3, size = shp)

        #y
        update = np.random.random(size=(self.size,))
        shp = update[update <= heading_update_chance].shape
        person[:,5][update <= heading_update_chance] = np.random.normal(loc = 0, scale = 1/3, size = shp)
        
        #randomize speeds
        update = np.random.random(size=(self.size,))
        shp = update[update <= heading_update_chance].shape
        person[:,6][update <= heading_update_chance] = np.random.normal(loc = speed, scale = speed / 3, size = shp)

        person[:,6] = np.clip(person[:,6], a_min=0.0005, a_max=0.01)
        return person

    def set_destination(self):
        active_dests = np.unique(self.person.persons[:,11][self.person.persons[:,11] != 0])

    #set destination
        for d in active_dests:
            dest_x = self.destinations[:,int((d - 1) * 2)]
            dest_y = self.destinations[:,int(((d - 1) * 2) + 1)]

            #compute new headings
            head_x = dest_x - self.person.persons[:,2]
            head_y = dest_y - self.person.persons[:,3]

            #head_x = head_x / np.sqrt(head_x)
            #head_y = head_y / np.sqrt(head_y)

            #reinsert headings into self.person.persons of those not at destination yet
            self.person.persons[:,4][(self.person.persons[:,7] == d) &
                            (self.person.persons[:,8] == 0)] = head_x[(self.person.persons[:,7] == d) &
                                                                (self.person.persons[:,8] == 0)]
            self.person.persons[:,5][(self.person.persons[:,7] == d) &
                            (self.person.persons[:,8] == 0)] = head_y[(self.person.persons[:,7] == d) &
                                                                (self.person.persons[:,8] == 0)]
            #set speed to 0.01
            self.person.persons[:,6][(self.person.persons[:,7] == d) &
                            (self.person.persons[:,8] == 0)] = 0.02


    def check_at_destination(self, wander_factor=1.5, speed = 0.01):
        active_dests = np.unique(self.person.persons[:,7][(self.person.persons[:,7] != 0)])

        #see who is at destination
        for d in active_dests:
            dest_x = self.destinations[:,int((d - 1) * 2)]
            dest_y = self.destinations[:,int(((d - 1) * 2) + 1)]

            #see who arrived at destination and filter out who already was there
            at_dest = self.person.persons[(np.abs(self.person.persons[:,2] - dest_x) < (self.person.persons[:,10] * wander_factor)) & 
                                    (np.abs(self.person.persons[:,3] - dest_y) < (self.person.persons[:,11] * wander_factor)) &
                                    (self.person.persons[:,8] == 0)]

            if len(at_dest) > 0:
                #mark those as arrived
                at_dest[:,12] = 1
                #insert random headings and speeds for those at destination
                at_dest = self.update_persons(at_dest, pop_size = len(at_dest), speed = speed,
                                        heading_update_chance = 1, speed_update_chance = 1)

                #at_dest[:,5] = 0.001

                #reinsert into self.person.persons
                self.person.persons[(np.abs(self.person.persons[:,2] - dest_x) < (self.person.persons[:,10] * wander_factor)) & 
                            (np.abs(self.person.persons[:,3] - dest_y) < (self.person.persons[:,11] * wander_factor)) &
                            (self.person.persons[:,8] == 0)] = at_dest




    def keep_at_destination(self, wander_factor=1.0):
        active_dests = np.unique(self.person.persons[:,11][(self.person.persons[:,7] != 0) &
                                                (self.person.persons[:,8] == 1)])

        for d in active_dests:
            dest_x = self.destinations[:,int((d - 1) * 2)][(self.person.persons[:,8] == 1) &
                                                        (self.person.persons[:,7] == d)]
            dest_y = self.destinations[:,int(((d - 1) * 2) + 1)][(self.person.persons[:,8] == 1) &
                                                            (self.person.persons[:,7] == d)]

            #see who is marked as arrived
            arrived = self.person.persons[(self.person.persons[:,8] == 1) &
                                    (self.person.persons[:,7] == d)]

            ids = np.int32(arrived[:,0]) # find unique IDs of arrived persons
            
            #check if there are those out of bounds
            #replace x oob
            #where x larger than destination + wander, AND heading wrong way, set heading negative
            shp = arrived[:,4][arrived[:,2] > (dest_x + (arrived[:,10] * wander_factor))].shape

            arrived[:,4][arrived[:,2] > (dest_x + (arrived[:,10] * wander_factor))] = -np.random.normal(loc = 0.5,
                                                                    scale = 0.5 / 3,
                                                                    size = shp)


            #where x smaller than destination - wander, set heading positive
            shp = arrived[:,4][arrived[:,2] < (dest_x - (arrived[:,10] * wander_factor))].shape
            arrived[:,4][arrived[:,2] < (dest_x - (arrived[:,10] * wander_factor))] = np.random.normal(loc = 0.5,
                                                                scale = 0.5 / 3,
                                                                size = shp)
            #where y larger than destination + wander, set heading negative
            shp = arrived[:,5][arrived[:,3] > (dest_y + (arrived[:,11] * wander_factor))].shape
            arrived[:,5][arrived[:,3] > (dest_y + (arrived[:,11] * wander_factor))] = -np.random.normal(loc = 0.5,
                                                                    scale = 0.5 / 3,
                                                                    size = shp)

            #where y smaller than destination - wander, set heading positive
            shp = arrived[:,5][arrived[:,3] < (dest_y - (arrived[:,11] * wander_factor))].shape
            arrived[:,5][arrived[:,3] < (dest_y - (arrived[:,11] * wander_factor))] = np.random.normal(loc = 0.5,
                                                                scale = 0.5 / 3,
                                                                size = shp)

            #slow speed
            arrived[:,6] = np.random.normal(loc = 0.005,
                                            scale = 0.005 / 3, 
                                            size = arrived[:,6].shape)

            #reinsert into self.person.persons
            self.person.persons[(self.person.persons[:,8] == 1) &
                        (self.person.persons[:,7] == d)] = arrived
    
    def out_of_bounds(self, xbounds, ybounds):
        shp = self.person.persons[:,4][(self.person.persons[:,2] <= xbounds[:,0]) &
                            (self.person.persons[:,4] < 0)].shape
        self.person.persons[:,4][(self.person.persons[:,2] <= xbounds[:,0]) &
                        (self.person.persons[:,4] < 0)] = np.clip(np.random.normal(loc = 0.5, 
                                                                            scale = 0.5/3,
                                                                            size = shp),
                                                            a_min = 0.05, a_max = 1)

        shp = self.person.persons[:,4][(self.person.persons[:,2] >= xbounds[:,1]) &
                                (self.person.persons[:,4] > 0)].shape
        self.person.persons[:,4][(self.person.persons[:,2] >= xbounds[:,1]) &
                        (self.person.persons[:,4] > 0)] = np.clip(-np.random.normal(loc = 0.5, 
                                                                            scale = 0.5/3,
                                                                            size = shp),
                                                            a_min = -1, a_max = -0.05)

        #update y heading
        shp = self.person.persons[:,5][(self.person.persons[:,3] <= ybounds[:,0]) &
                                (self.person.persons[:,5] < 0)].shape
        self.person.persons[:,5][(self.person.persons[:,3] <= ybounds[:,0]) &
                        (self.person.persons[:,5] < 0)] = np.clip(np.random.normal(loc = 0.5, 
                                                                            scale = 0.5/3,
                                                                            size = shp),
                                                            a_min = 0.05, a_max = 1)

        shp = self.person.persons[:,5][(self.person.persons[:,3] >= ybounds[:,1]) &
                                (self.person.persons[:,5] > 0)].shape
        self.person.persons[:,5][(self.person.persons[:,3] >= ybounds[:,1]) &
                        (self.person.persons[:,5] > 0)] = np.clip(-np.random.normal(loc = 0.5, 
                                                                            scale = 0.5/3,
                                                                            size = shp),
                                                            a_min = -1, a_max = -0.05)
    def update_pop(self):
                 #x
        self.person.persons[:,2] = self.person.persons[:,2] + (self.person.persons[:,4] * self.person.persons[:,6])
                    #y
        self.person.persons[:,3] = self.person.persons[:,3] + (self.person.persons [:,5] * self.person.persons[:,6])


    def move(self):
        active_dests = len(self.person.persons[self.person.persons[:,7] != 0])
        
        if active_dests > 0 and len(self.person.persons[self.person.persons[:,8] == 0]) > 0:
            self.set_destination()
            self.check_at_destination()
        
        if active_dests > 0 and len(self.person.persons[self.person.persons[:,8] == 1]) > 0:
            self.keep_at_destination()
        
        _xbounds = np.array([[0,1]] * self.size)
        _ybounds = np.array([[0,1]] * self.size)
        self.out_of_bounds( _xbounds, _ybounds)

        self.person.persons = self.update_persons(self.person.persons, self.size)
        
        self.update_pop()

if __name__ == "__main__":
    p = Population(100, [0, 1], [0, 1], 3, 0.5)
    #p.move()
    #virus = Virus()
    #p.person = virus.infect(p.person)
    



            


