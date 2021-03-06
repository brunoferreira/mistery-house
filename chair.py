import pygame
import constants
from utils import Utils
import os
from objects import InteractiveObjetcs


class Chair(InteractiveObjetcs):
    """
        Classe que define os parametros básicos das cadeiras do código
    """
    def __init__(self, x, y, position_mode, scale = None):
        super().__init__(self.chair_image, x, y, position_mode, scale)


    def after_interaction(self):
        pass


    def define_mask(self):
        mask_width = self.width*1.2
        mask_height = self.height*1.2
        mask = pygame.mask.Mask((mask_width, mask_height), False)
        rect_width = 0.8*mask_width
        rect_height = 0.8*mask_height
        position = ((mask_width - rect_width)/2, (mask_height - rect_height)/2)
        rect = pygame.mask.Mask((rect_width, rect_height), True)
        mask.draw(rect, position)
        return mask


class DecorationArmChairLateral(Chair):
    """
        Classe que define uma cadeira na posição lateral que estão nas salas
    """
    def __init__(self, x, y, position_mode):
        self.chair_image = os.path.join(constants.IMAGES_DIR, 'red armchair right.png')
        super().__init__(x, y, position_mode, (90, 115))

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

        message = "Uma poltrona vermelha."

        options = {'centralized'}
        parameters = {'message': message, 'font_size': 20,
            'width': 0.72*constants.WIDTH, 'height': 0.1*constants.HEIGHT,
        }
        Utils().print_message(options, parameters)


class DecorationArmChairFront(Chair):
    """
        Classe que define uma cadeira na posição frontal que estão nas salas
    """
    def __init__(self, x, y, position_mode):
        self.chair_image = os.path.join(constants.IMAGES_DIR, 'purple armchair front.png')
        super().__init__(x, y, position_mode, (90, 115))

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

        message = "Quer descansar um pouco?"

        options = {'centralized'}
        parameters = {'message': message, 'font_size': 20,
            'width': 0.72*constants.WIDTH, 'height': 0.1*constants.HEIGHT,
        }
        Utils().print_message(options, parameters)