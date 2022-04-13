import pygame
import constants
from utils import Utils
import os
from objects import InteractiveObjetcs

class Paper(InteractiveObjetcs):

    def __init__(self, x, y, position_mode):
        self.paper_image_path = os.path.join(constants.IMAGES_DIR, 'paper.png')
        super().__init__(self.paper_image_path, x, y, position_mode, (45, 55))



    def after_interaction(self):
        pass


    def define_mask(self):
        mask_width = self.width
        mask_height = self.height
        mask = pygame.mask.Mask((mask_width, mask_height), False)
        rect_width = 0.8*mask_width
        rect_height = 0.8*mask_height
        position = ((mask_width - rect_width)/2, (mask_height - rect_width)/2)
        rect = pygame.mask.Mask((rect_width, rect_height), True)
        mask.draw(rect, position)
        return mask        


class Paper1(Paper):

    def interaction(self, player):
        self.print_pop_up()

        in_pop_up = True
        while in_pop_up:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #TODO
                    pass
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        in_pop_up = False
                    elif event.key == pygame.K_ESCAPE:
                        in_pop_up = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_e:
                        player.stop_acting()


    def print_pop_up(self):
        width = 0.9*constants.WIDTH
        x_pop_up = 0.5*constants.WIDTH

        message1 = "Bem vindo a Mistery House!"
        message2 = "Você não se lembra como veio parar aqui, mas não se preocupe, tudo será explicado no tempo"
        message3 = "certo. A única coisa que posso te dizer nesse momento é que, por muitas vezes, a vida"
        message4 = "parece ser apenas preto no branco, mas, na verdade, ela não é. Tudo não é sempre 0 ou 1."

        options = {'centralized', 'text_offset'}
        parameters = {'message': message1, 'font_size': 16,
            'width': width, 'height': 0.24*constants.HEIGHT,
            'x_text': 0.5*width, 'y_text': 0.2*0.24*constants.HEIGHT
        }
        Utils().print_message(options, parameters)

        options = {}
        parameters = {'message': message2, 'font_size': 16,
            'width': width, 'height': 0.04*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.48*constants.HEIGHT
        }
        Utils().print_message(options, parameters)
        
        parameters = {'message': message3, 'font_size': 16,
            'width': width, 'height': 0.04*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.52*constants.HEIGHT
        }
        Utils().print_message(options, parameters)

        parameters = {'message': message4, 'font_size': 16,
            'width': width, 'height': 0.04*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.56*constants.HEIGHT
        }
        Utils().print_message(options, parameters)


class Paper2(Paper):

    def interaction(self, player):
        self.print_pop_up()

        in_pop_up = True
        while in_pop_up:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #TODO
                    pass
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        in_pop_up = False
                    elif event.key == pygame.K_ESCAPE:
                        in_pop_up = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_e:
                        player.stop_acting()


    def print_pop_up(self):

        message = "Nada por aqui."
        options = {'centralized'}
        parameters = {'message': message, 'font_size': 20,
            'width': 0.3*constants.WIDTH, 'height': 0.2*constants.HEIGHT
        }
        Utils().print_message(options, parameters)