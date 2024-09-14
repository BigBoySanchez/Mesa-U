import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((1270, 700))
    clock = pygame.time.Clock()
    running = True

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with blue
        screen.fill("blue")

        pygame.display.flip()
        
        clock.tick(60)


if __name__ == "__main__":
    main()
