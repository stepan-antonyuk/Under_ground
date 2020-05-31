import pygame

from editmode import Editor
# from station import Station
from world import World

world = World(lineList=[], stationList=[])

FPS = 60
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode()  # (flags=pygame.FULLSCREEN)
done = False
color = (0, 0, 0)
was_pressed = False
station_editor = False
counter = 0
time = 0
button_pressed = False
line_editor = False
stations_connected = 0
drawing_line = False
initial_station = None
dragging = False

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


def draw_station_screen(stations):
    for station in stations:
        station.draw_station(screen)


def on_station(stations):
    return pressed_station(stations) is not None


def pressed_station(stations):
    for station in stations:
        if station.on_station(pygame.mouse.get_pos()):
            return station
    return None


editor = Editor(screen, world)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    screen.fill((255, 255, 255))

    editor.on_pressed(pygame.key.get_pressed())
    editor.mode.before()
    if pygame.mouse.get_pressed()[0]:
        editor.mode.on_left_pressed()
    else:
        editor.mode.on_left_released()

    # pygame.draw.rect(screen, red, (100, 880, 100, 100), 2)
    # pygame.draw.rect(screen, green, (300, 880, 100, 100), 2)
    # pygame.draw.rect(screen, blue, (500, 880, 100, 100), 2)

    # pressed = pygame.key.get_pressed()
    #
    # if pressed[pygame.K_s] and not button_pressed:
    #     line_editor = False
    #     button_pressed = True
    #     if station_editor and time == 0:
    #         station_editor = False
    #         time += 1
    #     elif not station_editor and time == 0:
    #         station_editor = True
    #         time += 1
    # elif pressed[pygame.K_l] and not button_pressed:
    #     station_editor = False
    #     button_pressed = True
    #     if line_editor and time == 0:
    #         line_editor = False
    #         time += 1
    #     elif not line_editor and time == 0:
    #         line_editor = True
    #         time += 1
    # else:
    #     button_pressed = False
    #     time = 0
    #
    # if station_editor:
    #     print("station editor mode on")
    #     if pygame.mouse.get_pressed()[0]:
    #         if not was_pressed:
    #             print("made new station")
    #             was_pressed = True
    #             world.stationList.append(Station(pygame.mouse.get_pos()))
    #             counter += 1
    #             print(counter)
    #             print(world.stationList[-1])
    #         else:
    #             print("moving station")
    #             world.stationList[counter - 1].change_pos(pygame.mouse.get_pos())
    #     else:
    #         if was_pressed:
    #             print("placing station")
    #             world.stationList[counter - 1].change_pos(pygame.mouse.get_pos())
    #             was_pressed = False
    #     # elif pygame.mouse.get_pressed()[0] and was_pressed:
    #     #     print("moving station")
    #     #     world.stationList[counter - 1].change_pos(pygame.mouse.get_pos())
    # elif line_editor:
    #     print("line editor mod on")
    #     if pygame.mouse.get_pressed()[0]:
    #         if on_station(world.stationList) and not drawing_line:
    #             print("on station")
    #             drawing_line = True
    #             initial_station = pressed_station(world.stationList)
    #         elif drawing_line:
    #             print("drawing line")
    #             initial_station.draw_line_from_station(pygame.mouse.get_pos(), screen)
    #             if on_station(world.stationList) and initial_station != pressed_station(world.stationList):
    #                 print("found second station")
    #     else:
    #         if drawing_line and on_station(world.stationList) and initial_station != pressed_station(world.stationList):
    #             print("connecting stations")
    #             world.connecting_station_line(initial_station.station_pos(), pressed_station(world.stationList).station_pos())
    #             drawing_line = False
    #         else:
    #             print("none")
    #             drawing_line = False
    # else:
    #     print("move editor")
    #     if pygame.mouse.get_pressed()[0]:
    #         if on_station(world.stationList) and not dragging:
    #             print("found station, start dragging")
    #             dragging = True
    #             initial_station = pressed_station(world.stationList)
    #         elif dragging:
    #             print("dragging")
    #             world.change_line_pos(pygame.mouse.get_pos(), initial_station.station_pos())
    #             initial_station.change_pos(pygame.mouse.get_pos())
    #     else:
    #         print("waiting for command")
    #         dragging = False

    world.draw_lines(screen)
    draw_station_screen(world.stationList)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
