import pygame, math

pygame.init()

class Node(object):
    visited = False

    def __init__(self, x, y, x_area, y_area, id):
        self.rect = pygame.Rect(x, y, x_area, y_area)
        self.id = id


class Block(object):
    moved = False
    path = []

    def __init__(self, x, y, x_area, y_area, id, type):
        self.rect = pygame.Rect(x, y, x_area, y_area)
        self.id = id
        self.type = type
    def move(self, x, y):
        collision_walls = self.rect.move(x,y).collidelist(walls)
        collision_rects = self.rect.move(x,y).collidelist([e.rect for e in blocks if e is not self])
        if collision_walls < 0 and collision_rects < 0:
            self.rect = self.rect.move(x,y)
            self.moved = True

    def simple_move(self, x, y):
        self.rect.move(x, y)

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
orchid = (218, 112, 214)
paleviolet = (199, 21, 133)
seashell = (255, 245, 238)
greenyellow = (173, 255, 47)
maroon = (128, 0, 0)
darkblue = (72, 61, 139)
lavender = (230, 230, 250)
tomato = (255, 99, 71)

size = (640, 790)
screen = pygame.display.set_mode(size)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

block1 = Block(20, 20, 150, 300, "block1", "vert_block")
block2 = Block(470, 20, 150, 300, "block2", "vert_block")
block3 = Block(20, 320, 150, 300, "block3", "vert_block")
block4 = Block(470, 320, 150, 300, "block4", "vert_block")
block5 = Block(170, 320, 300, 150, "block5", "vert_block")
smallblock1 = Block(20, 620, 150, 150, "smallblock1", "small_block")
smallblock2 = Block(170, 470, 150, 150, "smallblock2", "small_block")
smallblock3 = Block(320, 470, 150, 150, "smallblock3", "small_block")
smallblock4 = Block(470, 620, 150, 150, "smallblock4", "small_block")
center_block = Block(170, 20, 300, 300, "center_block", "center_block")


walls = [pygame.Rect(0, 0, 20, 770), pygame.Rect(0, 0, 620, 20), pygame.Rect(620, 0, 20, 770), pygame.Rect(0, 770, 770, 20)]
blocks = [block1, block2, block3, block4, block5, smallblock1, smallblock2, smallblock3, smallblock4, center_block]

small_block_matrix = [Node(20, 20, 150, 150, 'a'), Node(170, 20, 150, 150, 'b'), Node(320, 20, 150, 150, 'c'),
                      Node(470, 20, 150, 150, 'd'),
                      Node(20, 170, 150, 150, 'e'), Node(170, 170, 150, 150, 'f'), Node(320, 170, 150, 150, 'g'),
                      Node(470, 170, 150, 150, 'h'),
                      Node(20, 320, 150, 150, 'i'), Node(170, 320, 150, 150, 'j'), Node(320, 320, 150, 150, 'k'),
                      Node(470, 320, 150, 150, 'l'),
                      Node(20, 470, 150, 150, 'm'), Node(170, 470, 150, 150, 'n'), Node(320, 470, 150, 150, 'o'),
                      Node(470, 470, 150, 150, 'p'),
                      Node(20, 620, 150, 150, 'q'), Node(170, 620, 150, 150, 'r'), Node(320, 620, 150, 150, 's'),
                      Node(470, 620, 150, 150, 't')]

center_block_matrix = [Node(20, 20, 300, 300, 'a'), Node(170, 20, 300, 300, 'b'), Node(320, 20, 300, 300, 'c'),
                       Node(20, 170, 300, 300, 'd'), Node(170, 170, 300, 300, 'c'), Node(320, 170, 300, 300, 'e'),
                       Node(20, 320, 300, 300, 'f'), Node(170, 320, 300, 300, 'g'), Node(320, 320, 300, 300, 'h'),
                       Node(20, 470, 300, 300, 'i'), Node(170, 470, 300, 300, 'j'), Node(320, 470, 300, 300, 'k')]

vert_block_matrix = [Node(20, 20, 150, 300, 'a'), Node(170, 20, 150, 300, 'b'), Node(320, 20, 150, 300, 'c'),
                     Node(470, 20, 150, 300, 'd'),
                     Node(20, 170, 150, 300, 'e'), Node(170, 170, 150, 300, 'f'), Node(320, 170, 150, 300, 'g'),
                     Node(470, 170, 150, 300, 'h'),
                     Node(20, 320, 150, 300, 'i'), Node(170, 320, 150, 300, 'j'), Node(320, 320, 150, 300, 'k'),
                     Node(470, 320, 150, 300, 'l'),
                     Node(20, 470, 150, 300, 'm'), Node(170, 470, 150, 300, 'n'), Node(320, 470, 150, 300, 'o'),
                     Node(470, 470, 150, 300, 'p')]

horz_block_matrix = [Node(20, 20, 300, 150, 'a'), Node(170, 20, 300, 150, 'b'), Node(320, 20, 300, 150, 'c'),
                     Node(20, 170, 300, 150, 'd'), Node(170, 170, 300, 150, 'c'), Node(320, 170, 300, 150, 'e'),
                     Node(20, 320, 300, 150, 'f'), Node(170, 320, 300, 150, 'g'), Node(320, 320, 300, 150, 'h'),
                     Node(20, 470, 300, 150, 'i'), Node(170, 470, 300, 150, 'j'), Node(320, 470, 300, 150, 'k'),
                     Node(20, 620, 300, 150, 'l'), Node(170, 620, 300, 150, 'm'), Node(320, 620, 300, 150, 'n')]

def select_block(mouse_pos, blocks):
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    for e in blocks:
        if e.rect.left < mouse_x < e.rect.right and e.rect.bottom > mouse_y > e.rect.top:
            return e
    return 0

selected_block = 0

def find_adj_nodes(block, matrix):
    adjacent = []
    block_center_coord_x = block.rect.center[0]
    block_center_coord_y = block.rect.center[1]

    if block.rect.width == 150 and block.rect.height == 300:
        for e in matrix:
            candidate_center_coord_x = e.rect.center[0]
            candidate_center_coord_y = e.rect.center[1]
            abs_x_distance = abs(block_center_coord_x - candidate_center_coord_x)
            abs_y_distance = abs(block_center_coord_y - candidate_center_coord_y)
            if abs_x_distance == 150 and abs_y_distance == 75 or abs_y_distance == 225 and abs_x_distance == 0:
                adjacent.append(e)
    if block.rect.width == 150 and block.rect.height == 150:
        for e in matrix:
            candidate_center_coord_x = e.rect.center[0]
            candidate_center_coord_y = e.rect.center[1]
            abs_x_distance = abs(block_center_coord_x - candidate_center_coord_x)
            abs_y_distance = abs(block_center_coord_y - candidate_center_coord_y)
            if abs_x_distance == 150 and abs_y_distance == 0 or abs_y_distance == 150 and abs_x_distance == 0:
                adjacent.append(e)
    if block.rect.width == 300 and block.rect.height == 300:
        for e in matrix:
            candidate_center_coord_x = e.rect.center[0]
            candidate_center_coord_y = e.rect.center[1]
            abs_x_distance = abs(block_center_coord_x - candidate_center_coord_x)
            abs_y_distance = abs(block_center_coord_y - candidate_center_coord_y)
            if abs_x_distance == 150 and abs_y_distance == 75 or abs_y_distance == 150 and abs_x_distance == 75:
                adjacent.append(e)
    if block.rect.width == 150 and block.rect.height == 300:
        for e in matrix:
            candidate_center_coord_x = e.rect.center[0]
            candidate_center_coord_y = e.rect.center[1]
            abs_x_distance = abs(block_center_coord_x - candidate_center_coord_x)
            abs_y_distance = abs(block_center_coord_y - candidate_center_coord_y)
            if abs_x_distance == 75 and abs_y_distance == 150 or abs_y_distance == 150 and abs_x_distance == 0:
                adjacent.append(e)
    return adjacent


def solve_klotski(blocks):
    for e in blocks:
        if e.type == "small_block":
            e.move(0, 150)
            if e.moved:
                for s in small_block_matrix:
                    if s.rect.center == e.rect.center:
                        s.visited = True
                        e.moved = False
                        e.path.append(s.id)
            e.move(150, 0)
            if e.moved:
                for s in small_block_matrix:
                    if s.rect.center == e.rect.center:
                        s.visited = True
                        e.moved = False
                        e.path.append(s.id)
            e.move(0, -150)
            if e.moved:
                for s in small_block_matrix:
                    if s.rect.center == e.rect.center:
                        s.visited = True
                        e.moved = False
                        e.path.append(s.id)
            e.move(-150, 0)
            if e.moved:
                for s in small_block_matrix:
                    if s.rect.center == e.rect.center:
                        s.visited = True
                        e.moved = False
                        e.path.append(s.id)
    print([p.path for p in blocks])


def draw_screen():
    screen.fill(black)
    for e in walls:
        pygame.draw.rect(screen, white, e)
    pygame.draw.rect(screen, black, pygame.Rect(170, 770, 300, 20))
    pygame.draw.rect(screen, red, block1.rect)
    pygame.draw.rect(screen, orchid, block2.rect)
    pygame.draw.rect(screen, paleviolet, block3.rect)
    pygame.draw.rect(screen, green, center_block.rect)
    pygame.draw.rect(screen, seashell, block4.rect)
    pygame.draw.rect(screen, tomato, block5.rect)
    pygame.draw.rect(screen, greenyellow, smallblock1.rect)
    pygame.draw.rect(screen, maroon, smallblock2.rect)
    pygame.draw.rect(screen, darkblue, smallblock3.rect)
    pygame.draw.rect(screen, lavender, smallblock4.rect)
    pygame.display.flip()

# while not done:
#
# for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#         # solve_klotski(blocks)
#         screen.fill(black)
#         for e in walls:
#             pygame.draw.rect(screen, white, e)
#         pygame.draw.rect(screen, black, pygame.Rect(170, 770, 300, 20))
#         pygame.draw.rect(screen, red, block1.rect)
#         pygame.draw.rect(screen, orchid, block2.rect)
#         pygame.draw.rect(screen, paleviolet, block3.rect)
#         pygame.draw.rect(screen, green, center_block.rect)
#         pygame.draw.rect(screen, seashell, block4.rect)
#         pygame.draw.rect(screen, tomato, block5.rect)
#         pygame.draw.rect(screen, greenyellow, smallblock1.rect)
#         pygame.draw.rect(screen, maroon, smallblock2.rect)
#         pygame.draw.rect(screen, darkblue, smallblock3.rect)
#         pygame.draw.rect(screen, lavender, smallblock4.rect)
#         pygame.display.flip()
#     clock.tick(60)
# pygame.quit()





while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif pygame.mouse.get_pressed()[0]:
            selected_block = select_block(pygame.mouse.get_pos(), blocks)
            print(selected_block.id)
            while not pygame.MOUSEBUTTONUP:
                if selected_block and pygame.mouse.get_pos()[1] > selected_block.rect.bottom:
                    selected_block.move(0, pygame.mouse.get_pos[1] - selected_block.rect.bottom)
                    selected_block = 0
                elif selected_block and pygame.mouse.get_pos()[1] < selected_block.rect.top:
                    selected_block.move(0, -150)
                    selected_block = 0
                elif selected_block and pygame.mouse.get_pos()[0] > selected_block.rect.right:
                    selected_block.move(150, 0)
                    selected_block = 0
                elif selected_block and pygame.mouse.get_pos()[0] < selected_block.rect.left:
                    selected_block.move(-150, 0)
                    selected_block = 0
                draw_screen()
        draw_screen()
    clock.tick(60)
pygame.quit()
