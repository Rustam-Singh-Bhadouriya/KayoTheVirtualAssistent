#all Modules Managment

import pyttsx3
from gtts import gTTS
# import google
from google import genai
from google.genai import types
import requests
from vosk import Model, KaldiRecognizer
import pyaudio
import webbrowser as wb
import pygame
import os
import wikipedia
import json
import  time

def downloadModules():
    os.system("pip install pyttsx3 gtts pygame google google.genai requests wikipedia vosk")
    print("Modules Install SuccessFully!")

