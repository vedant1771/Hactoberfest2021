import pygame
import numpy as np

def TIC_TAC_TOE_GAME():
    pygame.init()

    # rgb or (RED,GREEN,BLUE)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    BGCOLOR = (20,170,156)
    LINE_COLOR = (23,145,135)

    ROW = 3
    COL = 3

    WIDTH = 600
    HEIGHT = 690

    board = np.zeros((ROW,COL))
    print(board)
    SQUARE_SIZE = 200
    SPACE = 55
    CROSS_WIDTH = 15

    font = pygame.font.SysFont(None,57)
    def text_screen(text, coor, x, y):
        screen_text = font.render(text, True, coor)
        gameWindow.blit(screen_text, [x, y])
    def mark_square(row,col,player):
        board[row][col] = player
    def available_square(row,col):
        return board[row][col] == 0
    def board_is_full():
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == 0:
                    return False
        return True

    gameWindow = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption('TIC TAC TOE')
    gameWindow.fill(BGCOLOR)

    name = 'O'
    player = 2
    board_is_full()
    def draw_lines():
        pygame.draw.line(gameWindow, LINE_COLOR, (0,200),  (600,200),  15)
        pygame.draw.line(gameWindow, LINE_COLOR, (0, 400), (600, 400), 15)
        pygame.draw.line(gameWindow, LINE_COLOR, (200, 0), (200, 600), 15)
        pygame.draw.line(gameWindow, LINE_COLOR, (400, 0), (400, 600), 15)

    def draw_figures():
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == 1:
                    pygame.draw.circle(gameWindow, (0, 0, 200), (int( col * 200 + 100 ), int( row * 200 + 100 )), 60, 16)
                elif board[row][col] == 2:
                    pygame.draw.line(gameWindow,(255,0,0),
                                     (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                     (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                    pygame.draw.line(gameWindow, (255,0,0), (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                     (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH )


    def check_win():
        for col in range(COL):
            if board[0][col] == player and board[1][col] == player and board[2][col] == player:
                vertical_line(col,player)
                return True
        for row in range(ROW):
            if board[row][0] == player and board[row][1] == player and board[row][2] == player:
                horizantel_line(row,player)
                return True

        if board[2][0] == player and board[1][1] == player and board[0][2] == player:
            draw_asc_diognal(player)
            return True

        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            draw_desr_digonal(player)

            return True

        return False

    def horizantel_line(row,player):
        posY = row * 200 + 100

        if player == 1:
            color = (0,0,200)
        if player == 2:
            color = RED

        pygame.draw.line(gameWindow, color, (15,posY), (WIDTH-15,posY), 15)
    def vertical_line(col,player):
        posX = col * 200 + 100

        if player == 1:
            color = (0,0,200)
        if player == 2:
            color = RED

        pygame.draw.line(gameWindow,color,(posX,15),(posX,HEIGHT - 15),15)
    def draw_asc_diognal(player):
        if player == 1:
            color = (0, 0, 200)
        if player == 2:
            color = RED

        pygame.draw.line(gameWindow,color,(15,HEIGHT-15),(WIDTH-15,15),15)
    def draw_desr_digonal(player):
        if player == 1:
            color = (0,0,200)
        if player == 2:
            color = RED

        pygame.draw.line(gameWindow,color,(15,15),(WIDTH+15,HEIGHT+15),15)

    game_over = False
    Chance = 'O'
    def restart():
        gameWindow.fill(BGCOLOR)
        draw_lines()
        player = 1
        for row in range(ROW):
            for col in range(COL):
                board[row][col] = 0


    draw_lines()
    while True:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                    game_over = False
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = int(mouseY / 200)
                clicked_col = int(mouseX / 200)

                print(clicked_row)
                print(clicked_col)

                if available_square(clicked_row,clicked_col):
                    if player == 1:
                        mark_square(clicked_row,clicked_col,1)

                        if check_win():
                            game_over = True
                            print('o win')
                        player = 2


                    elif player == 2:
                        mark_square(clicked_row, clicked_col,2)
                        if check_win():
                            game_over = True
                        player = 1


                    draw_figures()

        draw_figures()
        text_screen('Player 1 : O',(0,0,200),0,630)
        text_screen('VS', (255, 255, 255), 260, 600)
        text_screen('Player 2 : X', (255, 0, 0), 350, 630)
        pygame.display.update()

TIC_TAC_TOE_GAME()
