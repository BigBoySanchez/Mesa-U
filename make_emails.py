import pygame
from email import Email

def line_wrap(body, text):
    max_width = 810 # WIP: tweak this as needed 
    body_font = pygame.font.Font(None, 30)
    words = text.split(' ')  # Split the text by spaces
    lines = []
    current_line = ""
    
    for word in words:
        # Check the width of the current line with the new word added
        test_line = current_line + word + " "
        text_width, _ = body_font.size(test_line)
        
        if text_width > max_width:
            # If the line width exceeds the max width, append it and start a new line
            lines.append(current_line.strip())
            current_line = word + " "
        else:
            current_line = test_line

    # Append the last line
    if current_line:
        lines.append(current_line.strip())

    # Starting position for the text
    x, y = 0, 0

    # Render and blit each line
    for line in lines:
        text_surface = body_font.render(line, True, (0, 0, 0))
        body.blit(text_surface, (x, y))
        y += body_font.get_height() + 5  # Move the y-coordinate down by the font height for the next line


def make_emails(screen, body_color):
    WIDTH, HEIGHT = screen.get_size()
    emails = []
   
    # Sample emails
    body_font = pygame.font.Font(None, 30)

    legit1_body = pygame.Surface((WIDTH * (1 - 0.2488 + 0.001), HEIGHT))
    legit1_body.fill(body_color)
    line_wrap(legit1_body, "lazy ahhhh boy")

    legit1 = Email("Do your homework!", "Ms. Teacher", "t.cher@gmail.com", legit1_body, "reply", "real teacher")
    emails.append(legit1)

    evil1_body = pygame.Surface((WIDTH * (1 - 0.2488), HEIGHT))
    evil1_body_rect = evil1_body.get_rect()
    evil1_body.fill(body_color)
    line_wrap(evil1_body, "CLICK THE LINK BELOW \\/ \\/ \\/")

    evil1 = Email("1,000,000 FREE ROBUX!", "Robux Raider", "3yd98@hotmail.to", evil1_body, "report", "malicious link")
    emails.append(evil1)

    evil2_body = pygame.Surface((WIDTH * (1 - 0.2488), HEIGHT))
    evil2_body.fill(body_color)
    line_wrap(evil2_body, "go to my ig <3 \\/ \\/ \\/")

    evil2 = Email("i wuv u :3", "Bethany Aberdale", "baberd@yahoo.com", evil2_body, "report", "malicious link")
    emails.append(evil2)

    evil3_body = pygame.Surface((WIDTH * (1 - 0.2488), HEIGHT))
    evil3_body.fill("white")
    line_wrap(evil3_body, "Congratulations!! You’ve been randomly selected to receive 10,000 Robux. Click here to claim your reward")

    evil3 = Email("You've Won 10,000 Robux!", "Roblox Rewards Team", "rewards@roblox-rewards.com", evil3_body, "report", "phishing")
    emails.append(evil3)

    legit2_body = pygame.Surface((WIDTH * (1 - 0.2488 + 0.001), HEIGHT))
    legit2_body.fill("white")
    line_wrap(legit2_body, "Your application has been successfully submitted. You can view your submission details by logging into your account at fafsa.gov.")

    legit2 = Email("FAFSA Application Submitted", "Federal Student Aid", "noreply@fafsa.gov", legit2_body, "reply", "legit domain")
    emails.append(legit2)

    evil4_body = pygame.Surface((WIDTH * (1 - 0.2488), HEIGHT))
    evil4_body.fill("white")
    line_wrap(evil4_body, "heyy i want to start a new life with u but my bank account is frozen rn. :( Send me $1,000 to help me fix the issue? I'll pay u back when we're together, promise!!")

    evil4 = Email("Can't stop thinking about u", "Your Admirer", "babe@hotmail.com", evil4_body, "report", "scamming")
    emails.append(evil4)

    legit3_body = pygame.Surface((WIDTH * (1 - 0.2488 + 0.001), HEIGHT))
    legit3_body.fill("white")
    line_wrap(legit3_body, "Your recent order #9283 has shipped. Log in to track your package")

    legit3 = Email("Your Order Has Shipped", "Amazon", "shipment-tracking@amazon.com", legit3_body, "reply", "legit domain & specific order")
    emails.append(legit3)

    evil5_body = pygame.Surface((WIDTH * (1 - 0.2488), HEIGHT))
    evil5_body.fill("white")
    line_wrap(evil5_body, "We've detected unusual activity on your Netflix account. Click here to verify your identity.")

    evil5 = Email("You're Account is locked, ACT NOW", "Netflix Support", "netflix-support@hotmail.com", evil5_body, "report", "scamming")
    emails.append(evil5)

    evil6_body = pygame.Surface((WIDTH * (1 - 0.2488), HEIGHT))
    evil6_body.fill("white")
    line_wrap(evil6_body, "We’ve detected unauthorized activity on your account. Click here to verify your identity.")

    evil6 = Email("Your Bank Account Is Compromised", "Wells Fargo Support", "support@wellsfargo-secure.com", evil6_body, "report", "scamming")
    emails.append(evil6)

    evil7_body = pygame.Surface((WIDTH * (1 - 0.2488), HEIGHT))
    evil7_body.fill("white")
    line_wrap(evil7_body, "We noticed a new sign-in to your Google Account. Click here to check account activity.")

    evil7 = Email("Security alert", "Google", "no-reply@accounts.goog1e.com", evil7_body, "report", "spelling error in domain")
    emails.append(evil7)

    legit4_body = pygame.Surface((WIDTH * (1 - 0.2488 + 0.001), HEIGHT))
    legit4_body.fill("white")
    line_wrap(legit4_body, "Welcome to LinkedIn! Start building your professional network by connecting with people you know. Log in now to get started")

    legit4 = Email("Welcome to LinkedIn!", "LinkedIn", "welcome@linkedin.com", legit4_body, "reply", "legit domain & clear purpose")
    emails.append(legit4)

    return emails

