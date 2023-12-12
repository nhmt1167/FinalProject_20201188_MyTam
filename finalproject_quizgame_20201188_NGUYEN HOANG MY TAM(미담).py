import pygame
import sys
import random
import time
from answers_dict import answers_dict


pygame.init()


WIDTH, HEIGHT = 800, 600
FPS = 30
WHITE = (255, 255, 255)
FONT = pygame.font.Font(None, 36)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Celeb Quiz")

# image size
images = {key: pygame.transform.scale(pygame.image.load(answers_dict[key][-1]), (400, 400)) for key in answers_dict.keys()}

#random shuffle
questions = list(images.keys())
random.shuffle(questions)

# Main game loop
score = 0
current_question_index = 0

# start page
starting_page = True

#for countdown
countdown_duration = 5  # seconds for countdown
start_time = 0

#sound
pygame.mixer.init()
end_sound = pygame.mixer.Sound("tteng(cut).mp3")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        
        if event.type == pygame.MOUSEBUTTONDOWN and starting_page:
            starting_page = False
            start_time = time.time()  #start timer

    # Display starting page
    if starting_page:
        screen.fill(WHITE)
        start_text = FONT.render("Click to Start", True, (0, 0, 0))
        text_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(start_text, text_rect)
        pygame.display.flip()
        continue

    
    while current_question_index < len(questions):
        current_question = questions[current_question_index]
        correct_answers = answers_dict[current_question]

        # Reset timer every ques
        start_time = time.time()

        #Center img
        screen.fill(WHITE)
        image_rect = images[current_question].get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(images[current_question], image_rect)

        #Ask Ques
        prompt_text = FONT.render("Type the name of the celebrity:", True, (0, 0, 0))
        screen.blit(prompt_text, (WIDTH // 2 - 200, HEIGHT - 100))

        #Show score
        score_text = FONT.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (WIDTH - 200, 20))

        pygame.display.flip()
        

        #get input
        input_text = ""
        input_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 50, 200, 36)
        typing = True

        while typing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_RETURN:
                        typing = False
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

            #calc for time countdown
            current_time = time.time()
            remaining_time = max(0, countdown_duration - (current_time - start_time))

            screen.fill(WHITE)
            screen.blit(images[current_question], image_rect)
            pygame.draw.rect(screen, (0, 0, 0), input_rect, 2)
            text_surface = FONT.render(input_text, True, (0, 0, 0))
            screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            screen.blit(score_text, (WIDTH - 200, 20))

            #show countdown
            countdown_text = FONT.render(str(int(remaining_time) + 1), True, (255, 0, 0))
            screen.blit(countdown_text, (20, 20))

            pygame.display.flip()

            #if countdown is already 0
            if remaining_time <= 0:
                typing = False

        
        if input_text.lower() in [answer.lower() for answer in correct_answers]:
            score += 1
        else:
            #end game if wrong
            break

        current_question_index += 1

    #display end screen
    screen.fill(WHITE)
    screen.fill(WHITE)
    end_text = FONT.render("TTENG! Click to Start again", True, (0, 0, 0))
    score_text = FONT.render(f"Your score: {score}", True, (0, 0, 0))

    #center text
    end_text_rect = end_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    score_text_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10))

    #show text
    screen.blit(end_text, end_text_rect)
    screen.blit(score_text, score_text_rect)

    pygame.display.flip()

    # play sound
    end_sound.play()
    
    # close window
    waiting_for_exit = True
    while waiting_for_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                waiting_for_exit = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                waiting_for_exit = False
                current_question_index = 0
                score = 0
                starting_page = True
                start_time = 0 