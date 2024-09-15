import pygame
from email import Email

def make_emails(screen):
    WIDTH, HEIGHT = screen.get_size()
    emails = []
   
    # Sample emails
    body_font = pygame.font.Font(None, 100)

    legit1_body = pygame.Surface((WIDTH * (1 - 0.2488 + 0.001), HEIGHT))
    legit1_text = body_font.render("lazy ahhhh boy", True, (0, 0, 0))
    legit1_body.fill("white")
    legit1_body.blit(legit1_text, (0, 0))

    legit1 = Email("Do your homework!", "Ms. Teacher", "t.cher@gmail.com", legit1_body, "reply", "real teacher")
    emails.append(legit1)

    evil1_body = pygame.Surface((WIDTH * (1 - 0.2488), HEIGHT))
    evil1_text = body_font.render("CLICK THE LINK BELOW \\/ \\/ \\/", True, (0, 0, 0))
    evil1_body.fill("white")
    evil1_body.blit(evil1_text, (0, 0))

    evil1 = Email("1,000,000 FREE ROBUX!", "Robux Raider", "3yd98@hotmail.to", evil1_body, "report", "malicious link")
    emails.append(evil1)

    evil2_body = pygame.Surface((WIDTH * (1 - 0.2488), HEIGHT))
    evil2_text = body_font.render("go to my ig <3 \\/ \\/ \\/", True, (0, 0, 0))
    evil2_body.fill("white")
    evil2_body.blit(evil2_text, (0, 0))

    evil2 = Email("i wuv u :3", "Bethany Aberdale", "baberd@yahoo.com", evil2_body, "report", "malicious link")
    emails.append(evil2)

    return emails