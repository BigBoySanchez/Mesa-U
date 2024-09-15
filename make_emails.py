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

    evil3_body = pygame.Surface((WIDTH * (1 - 0.2488), HEIGHT))
    evil3_text = body_font.render("Congratulations!! You’ve been randomly selected to receive 10,000 Robux. Click here to claim your reward", True, (0, 0, 0))
    evil3_body.fill("white")
    evil3_body.blit(evil3_text, (0, 0))

    evil3 = Email("You've Won 10,000 Robux!", "Roblox Rewards Team", "rewards@roblox-rewards.com", evil3_body, "report", "phishing")
    emails.append(evil3)

    legit2_body = pygame.Surface((WIDTH * (1 - 0.2488 + 0.001), HEIGHT))
    legit2_text = body_font.render("Your application has been successfully submitted. You can view your submission details by logging into your account at fafsa.gov.", True, (0, 0, 0))
    legit2_body.fill("white")
    legit2_body.blit(legit2_text, (0, 0))

    legit2 = Email("FAFSA Application Successfully Submitted", "Federal Student Aid", "noreply@fafsa.gov", legit2_body, "reply", "legit domain")
    emails.append(legit2)

    evil4_body = pygame.Surface((WIDTH * (1 - 0.2488), HEIGHT))
    evil4_text = body_font.render("heyy i want to start a new life with u but my bank account is frozen rn. :( Send me $1,000 to help me fix the issue? I'll pay u back when we're together, promise!!", True, (0, 0, 0))
    evil4_body.fill("white")
    evil4_body.blit(evil4_text, (0, 0))

    evil4 = Email("Can't stop thinking about u", "Your Admirer", "babe@hotmail.com", evil4_body, "report", "scamming")
    emails.append(evil4)

    legit3_body = pygame.Surface((WIDTH * (1 - 0.2488 + 0.001), HEIGHT))
    legit3_text = body_font.render("Your recent order #9283 has shipped. Log in to track your package", True, (0, 0, 0))
    legit3_body.fill("white")
    legit3_body.blit(legit3_text, (0, 0))

    legit3 = Email("Your Order Has Shipped", "Amazon", "shipment-tracking@amazon.com", legit3_body, "reply", "legit domain & specific order")
    emails.append(legit3)

    evil5_body = pygame.Surface((WIDTH * (1 - 0.2488), HEIGHT))
    evil5_text = body_font.render("We've detected unusual activity on your Netflix account. Click here to verify your identity.", True, (0, 0, 0))
    evil5_body.fill("white")
    evil5_body.blit(evil5_text, (0, 0))

    evil5 = Email("You're Account is locked, urgent action required", "Netflix Support", "netflix-support@hotmail.com", evil5_body, "report", "scamming")
    emails.append(evil5)

    evil6_body = pygame.Surface((WIDTH * (1 - 0.2488), HEIGHT))
    evil6_text = body_font.render("We’ve detected unauthorized activity on your account. Click here to verify your identity.", True, (0, 0, 0))
    evil6_body.fill("white")
    evil6_body.blit(evil6_text, (0, 0))

    evil6 = Email("Your Bank Account Has Been Compromised", "Wells Fargo Support", "support@wellsfargo-secure.com", evil6_body, "report", "scamming")
    emails.append(evil6)

    evil7_body = pygame.Surface((WIDTH * (1 - 0.2488), HEIGHT))
    evil7_text = body_font.render("We noticed a new sign-in to your Google Account. Click here to check account activity.", True, (0, 0, 0))
    evil7_body.fill("white")
    evil7_body.blit(evil7_text, (0, 0))

    evil7 = Email("Security alert", "Google", "no-reply@accounts.goog1e.com", evil7_body, "report", "spelling error in domain")
    emails.append(evil7)

    legit4_body = pygame.Surface((WIDTH * (1 - 0.2488 + 0.001), HEIGHT))
    legit4_text = body_font.render("Welcome to LinkedIn! Start building your professional network by connecting with people you know. Log in now to get started", True, (0, 0, 0))
    legit4_body.fill("white")
    legit4_body.blit(legit3_text, (0, 0))

    legit4 = Email("Welcome to LinkedIn!", "LinkedIn", "welcome@linkedin.com", legit4_body, "reply", "legit domain & clear purpose")
    emails.append(legit4)

    return emails

