import pygame

# Global State
initial_page_load = True
email_page_load = False
blue_screen_page_load = False
running = True


def initial_page(screen):
    # Grab the needed globals
    global running
    global initial_page_load
    global email_page_load

    # fill the background first, then add stuff later
    screen.fill("white")

    # Main text
    start_font = pygame.font.Font(None, 35)
    start_text = start_font.render("Totally secure email client", True, (0, 0, 0))
    screen.blit(start_text, (450, 100))

    # Begin Button
    begin_button_width = 200
    begin_button_height = 50
    begin_button_x = 550
    begin_button_y = 500
    begin_button = pygame.Surface((begin_button_width, begin_button_height))
    begin_button.fill((0, 255, 0))

    begin_button_font = pygame.font.Font(None, 35)
    begin_button_text = begin_button_font.render("Start", True, (0, 0, 0))

    begin_button.blit(begin_button_text, (71, 15))

    # Start button
    begin_button_rect = pygame.Rect((begin_button_x, begin_button_y, begin_button_width, begin_button_height))
    screen.blit(begin_button, begin_button_rect.topleft)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if begin_button_rect.collidepoint(pos):
                # goto next screen
                print("butoon clicked")
                initial_page_load = False
                email_page_load = True

    # for event in pygame.event.get():
    #    if green_button.get_rect().collidepoint(pos):
    #        print("Button Clicked")


def email_page(screen):
    # Globals
    global running
    global initial_page_load
    global email_page_load
    screen.fill("white")

    # Back button
    back_button_width = 30
    back_button_height = 30

    back_button = pygame.Surface((back_button_width, back_button_height))
    back_button.fill((125, 95, 125))
    back_button_rect = pygame.Rect((5, 5, back_button_width, back_button_height))
    back_button_font = pygame.font.Font(None, 35)

    back_button_text = back_button_font.render("B", True, (0, 0, 0))
    back_button.blit(back_button_text, (6, 4))

    screen.blit(back_button, back_button_rect.topleft)

    # Event loop
    for event in pygame.event.get():
        # Quit the game
        if event.type == pygame.QUIT:
            running = False

        # Buttons alone
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            # Back button
            if back_button_rect.collidepoint(pos):
                print("Going back to start")
                initial_page_load = True
                email_page_load = False

            # Other buttons


def main():
    pygame.init()
    screen = pygame.display.set_mode((1270, 700))
    clock = pygame.time.Clock()
    while running:
        # Fill the screen with blue
        if initial_page_load:
            initial_page(screen)
        elif email_page_load:
            email_page(screen)
        elif blue_screen_page_load:
            pass

        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()
