# coding: utf-8

import pyglet
import pygame
import time
import threading

SONG = r'../../res/out.mp3'


def playWithPyglet():
    def stop():
        time.sleep(song.duration + 1)
        pyglet.app.exit()

    song = pyglet.media.load(SONG)
    song.play()
    # 启用子线程，在音乐播放完毕后终止此进程
    th = threading.Thread(target=stop)
    th.start()

    pyglet.app.run()


def playWithPygame():
    pygame.mixer.init()
    pygame.mixer.music.load(SONG)

    clock = pygame.time.Clock()

    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(60)
    pygame.quit()

if __name__ == '__main__':
    playWithPyglet()
    # playWithPygame()
