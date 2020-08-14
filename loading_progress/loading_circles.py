from dearpygui.dearpygui import *
import time
from math import sin, cos
pi = 3.141592
set_main_window_size(800, 640)  # Set window size


def count(sender, data):  # Define the async function to be executed.
    i = 0
    while i < data:
        i = i + 1
        time.sleep(0.1)


def longAsyncReturn(sender, data): 
    set_render_callback("") # Remove the set_render callback 
    hide_item("drawing") # and hide drawing
    add_text("And there we go")
    add_text("The async process ended and this screen was shown.", bullet=True)
    add_text("Load whatever you wanted in the app here", bullet=True)
    add_button("Some button", callback="some_callback")

def iter_loading(center_x, center_y, size, circles_radius, radii):
    '''
    center_x - X coordinate of center of loading circle
    center_Y - Y coordinate of center of loading circle
    size - Diameter of loading circle
    circles_radius = radius of smaller circles that constituite the loading circle
    radii - List of radiuses of all 12 circles
    '''
    # sin(pi/6) = 0.5
    # sin(pi/3) = 0.86602540378
    # cos(pi/6) = 0.86602540378
    # cos(pi/3) = 0.5

    draw_circle(
        "drawing", [
            center_x, center_y + size / 2], radii[0], [
            255, 255, 255, 255], 20, 5, fill=[
                255, 255, 255, 255], tag="circle#1")
    draw_circle(
        "drawing", [
            center_x + sin(pi/6) * size / 2, center_y + cos(pi/6) * size / 2], radii[1], [
                255, 255, 255, 255], 20, 5, fill=[
                    255, 255, 255, 255], tag="circle#2")
    draw_circle(
        "drawing", [
            center_x + sin(pi/3) * size / 2, center_y + cos(pi/3) * size / 2], radii[2], [
                255, 255, 255, 255], 20, 5, fill=[
                    255, 255, 255, 255], tag="circle#3")

    draw_circle(
        "drawing", [
            center_x + size / 2, center_y], radii[3], [
            255, 255, 255, 255], 20, 5, fill=[
                255, 255, 255, 255], tag="circle#4")

    draw_circle(
        "drawing", [
            center_x + sin(pi/3) * size / 2, center_y - cos(pi/3) * size / 2], radii[4], [
                255, 255, 255, 255], 20, 5, fill=[
                    255, 255, 255, 255], tag="circle#5")

    draw_circle(
        "drawing", [
            center_x + sin(pi/6) * size / 2, center_y - cos(pi/6) * size / 2], radii[5], [
                255, 255, 255, 255], 20, 5, fill=[
                    255, 255, 255, 255], tag="circle#6")

    draw_circle(
        "drawing", [
            center_x, center_y - size / 2], radii[6], [
            255, 255, 255, 255], 20, 5, fill=[
                255, 255, 255, 255], tag="circle#7")

    draw_circle(
        "drawing", [
            center_x - sin(pi/6) * size / 2, center_y - cos(pi/6) * size / 2], radii[7], [
                255, 255, 255, 255], 20, 5, fill=[
                    255, 255, 255, 255], tag="circle#8")

    draw_circle(
        "drawing", [
            center_x - sin(pi/3) * size / 2, center_y - cos(pi/3) * size / 2], radii[8], [
                255, 255, 255, 255], 20, 5, fill=[
                    255, 255, 255, 255], tag="circle#9")

    draw_circle(
        "drawing", [
            center_x - size / 2, center_y], radii[9], [
            255, 255, 255, 255], 20, 5, fill=[
                255, 255, 255, 255], tag="circle#10")

    draw_circle(
        "drawing", [
            center_x - sin(pi/3) * size / 2, center_y + cos(pi/3) * size / 2], radii[10], [
                255, 255, 255, 255], 20, 5, fill=[
                    255, 255, 255, 255], tag="circle#11")

    draw_circle(
        "drawing", [
            center_x - sin(pi/6) * size / 2, center_y + cos(pi/6) * size / 2], radii[11], [
                255, 255, 255, 255], 20, 5, fill=[
                    255, 255, 255, 255], tag="circle#12")

    radii = radii[-1:] + radii[:-1] #Right shift radiuses so the loading seems as it is rotating
    return radii


run_async_function("count", 100, return_handler="longAsyncReturn")
set_render_callback("loading")
add_drawing("drawing", width=800, height=640) # Add drawing
circles_radius = 10  # Radius of small circles
radii = [2 * circles_radius] + [circles_radius] * 11 #Initialize list of radii.


def loading(sender, data):
    # This function is constantly called until aysnc return handler triggers
    # because of set_render_callback("loading")
    global radii
    global circles_radius

    center_x, center_y, size = [400, 320, 200]
    radii = iter_loading(center_x, center_y, size, circles_radius, radii)
    time.sleep(0.1)

start_dearpygui()
