import pygame
import math
#pygame.init()
class Search:
    def __init__(self, start, goal, blocks, screen):
        self.start = start
        self.goal = goal
        self.blocks = blocks
        self.screen = screen
        self.unvisited = [start]
        self.visited = [start]
        self.completed = 0

    def check(self, element, inlist):
        for node in inlist:
            #print(node)
            if(node == element):
                #print("-----")
                return 1
        return 0 
            

    def expand(self,node):
        k = -10
        j = -10
        i = -10
        while k<1:
            while i<20:
                while j<20:
                    ans = 0  
                    newpos = (node[0]+i,node[1]+j)
                    #print("expansion")
                    #print(newpos)
                    ans = self.check(newpos,self.unvisited)
                    ans = ans + self.check(newpos,self.visited)
                    ans = ans + self.check(newpos, self.blocks)
                    if (ans == 0):
                        self.unvisited.append(newpos)
                        #pygame.draw.rect(self.screen, (0, 255, 0), (newpos[0],newpos[1],9,9))
                        #print("added")
                    j = j+10
                i = i+10
                j = -10
            k = k+1
    def completion(self):
        print("completed")
        self.completed = 1


    def A_Star(self):
        run = 0
        #self.unvisited = [self.start]

        store = 100000
        while (run == 0):
            #opt_node = start
            store = 100000    
            for pos in self.unvisited:
                f_cost = self.cost(pos)
                if (f_cost<store):
                    store = f_cost
                    opt_node = pos
            #now we have the optimum node, we add it to visited, add all the nodes around it to unvisited and repeat
            if (opt_node == self.goal):
                run = 1
                self.completion()
            #print("unvisited")
            #print(self.unvisited)
            #print("candidate node")
            #print(opt_node)
            self.expand(opt_node)
            self.visited.append(opt_node)
            #print("visited")
            #print(self.visited)
            #pygame.draw.rect(self.screen, (0, 0, 255), (opt_node[0],opt_node[1],9,9))
            self.unvisited.remove(opt_node)
            run = 1
            
    def cost(self, node):
        x = self.start[0]-node[0]
        y = self.start[1]-node[1]
        gcost = math.sqrt((x*x)+(y*y))
        x = self.goal[0]-node[0]
        y = self.goal[1]-node[1]
        hcost = math.sqrt((x*x)+(y*y))
        cost = hcost + hcost
        #print("cost")
        #print(node)
        #print(cost)
        return cost


screen = pygame.display.set_mode([500, 500])
running = True
store_visited = []
store_unvisited = []
store_blocks = []
store_start = []
store_goal = []
blocks = store_blocks
start = (50,50)
goal = (300,300)
aSearch = Search(start, goal, blocks,screen)
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                completed = 0
                while(completed == 0):
                    aSearch.A_Star()
                    store_start.append(aSearch.start)
                    store_goal.append(aSearch.goal)
                    store_unvisited = aSearch.unvisited
                    store_visited = aSearch.visited
                    store_blocks = aSearch.blocks
                    completed = aSearch.completed
                    while i<500:
                        while j<500:
                            pygame.draw.rect(screen, (255, 255, 255), (i,j,9,9))
                            j = j+10
                        i = i + 10
                        j = 0
                    for pos in store_blocks:
                        pygame.draw.rect(screen, (100, 100, 100), (pos[0],pos[1],9,9))
                    for pos in store_visited:
                        pygame.draw.rect(screen, (0, 0, 255), (pos[0],pos[1],9,9))
                    for pos in store_unvisited:
                        pygame.draw.rect(screen, (0, 255, 0), (pos[0],pos[1],9,9))
                    for pos in store_goal:
                        pygame.draw.rect(screen, (255, 0, 0), (pos[0],pos[1],9,9))
                    for pos in store_start:
                        pygame.draw.rect(screen, (255, 255, 0), (pos[0],pos[1],9,9))
                    pygame.display.flip()
                    pygame.time.delay(20)
                #print(store_start)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #print("You pressed the left mouse button")
            pos = pygame.mouse.get_pos()
            posx = round(pos[0],-1)
            posy = round(pos[1],-1)
            store_blocks.append((posx,posy))
            k = -10
            j = -10
            i = -10
            while k<1:
                while i<20:
                    while j<20:
                        store_blocks.append((posx+i,posy+j))
                        j = j+10
                    i = i+10
                    j = -10
                k = k +1

            


    # Fill the background with white
    screen.fill((0, 0, 0))

 
    i = 0
    j = 0 
   
    while i<500:
        while j<500:
            pygame.draw.rect(screen, (255, 255, 255), (i,j,9,9))
            j = j+10
        i = i + 10
        j = 0
    for pos in store_blocks:
        pygame.draw.rect(screen, (100, 100, 100), (pos[0],pos[1],9,9))
    for pos in store_visited:
        pygame.draw.rect(screen, (0, 0, 255), (pos[0],pos[1],9,9))
    for pos in store_unvisited:
        pygame.draw.rect(screen, (0, 255, 0), (pos[0],pos[1],9,9))

    pygame.draw.rect(screen, (255, 255, 0), (start[0],start[1],9,9))

    pygame.draw.rect(screen, (255, 0, 0), (goal[0],goal[1],9,9))
   
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()