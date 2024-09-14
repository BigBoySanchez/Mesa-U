import pygame

def initial_page(screen):
    # fill the background first, then add stuff later
    screen.fill("white")

    # Here is a basic button
    green_button = pygame.Surface((200, 50))
    green_button.fill((0, 255, 0))
    screen.blit(green_button, (550, 500))

    #for event in pygame.event.get():
    #    if green_button.get_rect().collidepoint(pos):
    #        print("Button Clicked")


def main():
    pygame.init()
    screen = pygame.display.set_mode((1270, 700))
    clock = pygame.time.Clock()
    running = True

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                print("mouse clicked")
                pos = pygame.mouse.get_pos()

        # Fill the screen with blue
        initial_page(screen)

        pygame.display.flip()
        
        clock.tick(60)


if __name__ == "__main__":
    main()
