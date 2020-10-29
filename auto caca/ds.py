import pyglet
import time


player = pyglet.media.Player()
source = pyglet.media.load('error.mp3')
player.queue(source)
player.play();
#print("play sound+");
time.sleep(1);
#print("delete sound+")
player.delete();
exit();
