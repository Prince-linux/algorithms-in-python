# A simple python program that adds space to any word after the full stop.
# Author: Prince Oppong Boamah
# Date: 18th January 2023

word = "Learn Python - Take our Python class for free! This python course for beginners consists of 10 classes, slowly and progressively introducing Python skills through explanations, example walk-through and code challenges.We know that the best way to learn Python is to start practising.In this fourth module we focus on learning the basic underpinning skills used throughout this course, string manipulation."

new_word = word.replace(".", ". ")
print(new_word)