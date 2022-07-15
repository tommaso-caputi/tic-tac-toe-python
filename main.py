import numpy as np
import pygame

pygame.init()

screen = pygame.display.set_mode((300, 400))
pygame.display.set_caption('Tic Tac Toe')
screen.fill((255,255,255))
pygame.display.flip()

end = True 
running = True
player = 0
last_player = player
board = [[1,2,3],
         [4,5,6],
         [7,8,9]]
    

def checkRows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return 0
def checkDiagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    return 0
def checkWin(board):
    for newBoard in [board, np.transpose(board)]:
        result = checkRows(newBoard)
        if result:
            return result
    return checkDiagonals(board)

def game(m_pos):
    global player, running, end
    x = m_pos[0]
    y = m_pos[1]
    if x<=100:
        x = 0
    elif x<=200 and x>100:
        x = 1
    else:
        x = 2
    if y<=100:
        y = 0
    elif y<=200 and y>100:
        y = 1
    else:
        y = 2 
    
    if board[y][x] != 'x' and board[y][x] != 'o':
        if player == 0:
            board[y][x] = 'x'
            player = 1
        else:
            board[y][x] = 'o'
            player = 0
    
    if checkWin(board) != 0:
        end = False
        

while running:

    pygame.draw.line(screen, (0,0,0), (100, 0), (100, 300), 5)
    pygame.draw.line(screen, (0,0,0), (200, 0), (200, 300), 5)
    pygame.draw.line(screen, (0,0,0), (0, 100), (300, 100), 5)
    pygame.draw.line(screen, (0,0,0), (0, 200), (300, 200), 5)
    pygame.draw.line(screen, (0,0,0), (0, 300), (300, 300), 5)
    
    for x in range(0 , 300, 100):
        for y in range(0, 300, 100):
            if str(board[int(y/100)][int(x/100)]) in ['o','x']:
                img = pygame.image.load(str(board[int(y/100)][int(x/100)])+'.png')
                img = pygame.transform.scale(img, (90, 90))
                screen.blit(img, (x+5,y+5))
    if end:
        player_= 'x' if player == 0 else 'o'
        text = "Player " + str(player_)
        font = pygame.font.Font(pygame.font.get_default_font(), 36)
        text = font.render(text, True, (0,255,0))
        text_rect = text.get_rect(center=(300/2, 350))
        screen.blit(text, text_rect)
        if last_player != player:
            screen.fill((255,255,255), text_rect)
        last_player = player
    else:
        screen.fill((255,255,255), text_rect)
        winner = checkWin(board)
        text = "Winner " + str(winner)
        font = pygame.font.Font(pygame.font.get_default_font(), 36)
        text = font.render(text, True, (0,255,0))
        text_rect = text.get_rect(center=(300/2, 350))
        screen.blit(text, text_rect)

    pygame.display.flip()

    m_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP and m_pos[1]<300 and end:
            game(m_pos)

        if event.type == pygame.QUIT:
            pygame.quit()
