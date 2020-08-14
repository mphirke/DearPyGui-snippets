from dearpygui.dearpygui import *
import time
from math import sqrt, sin, cos
pi = 3.141592
set_main_window_size(800, 640)  # Set window size

progress_count = 0
last_progress = 0

def count(sender, data):  # Define the async function to be executed.
    global progress_count
    i = 0
    while i < data:
        i = i + 1
        progress_count = i/data*100.0
        time.sleep(0.1)


def longAsyncReturn(sender, data): 
    set_render_callback("") # Remove the set_render callback 
    hide_item("drawing") # and hide drawing
    add_text("And there we go")
    add_text("The async process ended and this screen was shown.", bullet=True)
    add_text("Load whatever you wanted in the app here", bullet=True)
    add_button("Some button", callback="some_callback")


center_x, center_y = [400,320]
size=150

sin30 = sin(pi/6)
sin60 = sin(pi/3)
cos30 = cos(pi/6)
cos60 = cos(pi/3)

def iter_arcs(progress):
    if progress < 50:
        theta = pi/2 * progress/25.00
        x1, y1 = [center_x, center_y+size/2]
        x4, y4 = [center_x+sin(theta)*size/2, center_y+cos(theta)*size/2]
    if progress==50:
        theta = pi/2
        x1, y1 = [center_x, center_y-size/2]
        x4, y4 = [center_x+sin(theta)*size/2, center_y+cos(theta)*size/2]
    elif progress >= 50:
        theta = pi/2 * (progress-50)/25.00
        x1, y1 = [center_x, center_y-size/2]
        x4, y4 = [center_x-sin(theta)*size/2, center_y-cos(theta)*size/2]
    
    # Reference - https://stackoverflow.com/a/44829356/9155948
    ax = x1 - center_x
    ay = y1 - center_y
    bx = x4 - center_x
    by = y4 - center_y
    q1 = ax * ax + ay * ay
    q2 = q1 + ax * bx + ay * by
    k2 = 4/3 * (sqrt(2 * q1 * q2) - q2) / (ax * by - ay * bx)

    x2 = center_x + ax - k2 * ay
    y2 = center_y + ay + k2 * ax
    x3 = center_x + bx + k2 * by
    y3 = center_y + by - k2 * bx

    draw_bezier_curve("drawing", [x1,y1], [x2,y2], [x3,y3], [x4,y4], [255,255,255,255], 5, 10, tag="arc#"+str(progress_count))
    draw_text("drawing", [center_x-18,center_y+12], str(round(progress_count))+ " %", size=24, tag="Progress_text")
    return progress

run_async_function("count", 200, return_handler="longAsyncReturn")
set_render_callback("loading")
add_drawing("drawing", width=800, height=640) # Add drawing


def loading(sender, data):
    global progress_count
    global last_progress
    if progress_count > last_progress:
        last_progress = iter_arcs(progress_count)
    time.sleep(0.05)

start_dearpygui()
