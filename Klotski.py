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
    displace_x = 0
    displace_y = 0


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
            self.displace_x += x
            self.displace_y += y

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

screen_size = pygame.display.Info()
# size = (640, 790)


board_height = (screen_size.current_h * 2 / 3)

wall_size = 0
block_size = (board_height - (2 * wall_size)) / 5
board_width = 4 * block_size + 2 * wall_size
print(
"board width", screen_size.current_w / 4, "board_height", screen_size.current_h, "block size", block_size, "wall size",
wall_size)
#print(pygame.display.Info())
screen = pygame.display.set_mode((board_width, board_height))
#screen = pygame.display.set_mode(size)
pygame.display.set_caption('Klotski')

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Keeps track of moves made
moveCount = 0

block1 = Block(wall_size, wall_size, block_size, block_size * 2, "block1", "vert_block")
block2 = Block(block_size * 3 + wall_size * 2, wall_size, block_size, block_size * 2, "block2", "vert_block")
block3 = Block(wall_size, block_size * 2 + wall_size * 2, block_size, block_size * 2, "block3", "vert_block")
block4 = Block(block_size * 3 + wall_size * 2, 3 * block_size + wall_size * 2, block_size, block_size * 2, "block4",
               "vert_block")
block5 = Block(block_size + wall_size * 2, 2 * block_size + wall_size * 2, 3 * block_size, block_size, "block5",
               "vert_block")
smallblock1 = Block(wall_size, 4 * block_size + wall_size * 2, block_size, block_size, "smallblock1", "small_block")
smallblock2 = Block(block_size + wall_size, 3 * block_size + wall_size * 2, block_size, block_size, "smallblock2",
                    "small_block")
smallblock3 = Block(2 * block_size + wall_size * 2, 3 * block_size + wall_size * 2, block_size, block_size,
                    "smallblock3", "small_block")
smallblock4 = Block(3 * block_size + wall_size * 2, 4 * block_size + wall_size * 2, block_size, block_size,
                    "smallblock4", "small_block")
center_block = Block(block_size + wall_size, wall_size, block_size * 2, block_size * 2, "center_block", "center_block")

walls = [pygame.Rect(0, 0, wall_size, board_width - wall_size), pygame.Rect(0, 0, board_width - wall_size, wall_size),
         pygame.Rect(board_width - wall_size, 0, wall_size, board_height - wall_size),
         pygame.Rect(0, board_height - wall_size, board_height, wall_size)]
blocks = [block1, block2, block3, block4, block5, smallblock1, smallblock2, smallblock3, smallblock4, center_block]



def select_block(mouse_pos, blocks):
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    for e in blocks:
        if e.rect.left < mouse_x < e.rect.right and e.rect.bottom > mouse_y > e.rect.top:
            return e
    return 0


def draw_screen():
    screen.fill(black)
    for e in walls:
        pygame.draw.rect(screen, darkblue, e)
    #pygame.draw.rect(screen, black, pygame.Rect(170, 770, 300, 20))
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


selected_block = 0
mouseHeldDown = False
blockMove = (0, 0)

tmp_x = 0
tmp_y = 0

# Decides when to shift block
threshold = block_size / 2

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseHeldDown = True
            selected_block = select_block(pygame.mouse.get_pos(), blocks)
            pygame.mouse.get_rel()
        elif event.type == pygame.MOUSEBUTTONUP:
            mouseHeldDown = False
            moveCount += 1

            if selected_block in blocks:
                tmp_x = selected_block.displace_x % block_size
                if tmp_x > threshold:
                    selected_block.move(block_size - tmp_x, 0)
                else:
                    selected_block.move(-tmp_x, 0)

                tmp_y = selected_block.displace_y % block_size
                if tmp_y > threshold:
                    selected_block.move(0, block_size - tmp_y)
                else:
                    selected_block.move(0, -tmp_y)
            selected_block = 0
        elif mouseHeldDown:
            blockMove = pygame.mouse.get_rel()
            if selected_block in blocks:
                selected_block.move(blockMove[0], 0)
                selected_block.move(0, blockMove[1])

        draw_screen()
    clock.tick(60)
pygame.quit()
