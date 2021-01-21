import pygame
import sys


def check_win(mas, sign):
    zeroes = 0
    for row in mas:
        zeroes += row.count(0)
        if row.count(sign) == 3:
            return sign
    for column in range(3):
        if mas[0][column] == sign and mas[1][column] == sign and mas[2][column] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[2][0] == sign and mas[1][1] == sign and mas[0][2] == sign:
        return sign
    if zeroes == 0:
        return 'Piece'
    game_over = True


pygame.init()

size_block = 100
margin = 5
width = size_block * 3 + margin * 4
heigth = size_block * 3 + margin * 4 + 60
size_window = (width, heigth)

screen = pygame.display.set_mode(size_window)
pygame.display.set_caption('Крестики-нолики')
img = pygame.image.load('ХО.png')
pygame.display.set_icon(img)

orange = (255, 172, 58)
green = (45, 196, 135)
white = (255, 255, 255)
blue = (66, 139, 202)
mas = [[0] * 3 for i in range(3)]
query = 0
game_over = False
player = 'X'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            column = x_mouse // (size_block + margin)
            row = (y_mouse - 60) // (size_block + margin)
            if mas[row][column] == 0:
                if query % 2 == 0:
                    mas[row][column] = 'X'
                    player = 'O'
                else:
                    mas[row][column] = 'O'
                    player = 'X'
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query = 0
            screen.fill(white)
            player = 'X'
    if not game_over:
        screen.fill(white)
        font = pygame.font.SysFont('verdana', 25)
        player_text = font.render(f'Ходит игрок: {player}', True, blue)
        player_text_rect = player_text.get_rect()
        player_text_x = screen.get_width() / 2 - player_text_rect.width / 2
        screen.blit(player_text, [player_text_x, 20])
        for row in range(3):
            for column in range(3):
                if mas[row][column] == 'X':
                    color = orange
                elif mas[row][column] == 'O':
                    color = green
                else:
                    color = blue
                x = column * size_block + (column + 1) * margin
                y = row * size_block + (row + 1) * margin + 60
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == orange:
                    pygame.draw.line(screen, white, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 5)
                    pygame.draw.line(screen, white, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 5)
                elif color == green:
                    pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3,
                                       5)
        if (query - 1) % 2 == 0:
            game_over = check_win(mas, 'X')
        else:
            game_over = check_win(mas, 'O')

    if game_over:
        screen.fill(blue)
        font = pygame.font.SysFont('verdana', 25)
        if not game_over == 'Piece':
            end_text = font.render(f'Выиграл игрок: {game_over}', True, white)
        else:
            end_text = font.render(f'Выиграла дружба', True, white)
        end_text_rect = end_text.get_rect()
        end_text_x = screen.get_width() / 2 - end_text_rect.width / 2
        end_text_y = screen.get_height() / 2 - end_text_rect.height / 2
        screen.blit(end_text, [end_text_x, end_text_y])

    pygame.display.update()
