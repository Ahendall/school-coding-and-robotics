import simpleaudio as sa
import time

"""
Audio functions & vars
use var.play() to immideatly continue the code while the audio is playing
use var.play().wait_done() to  wait until audio is finished.
"""


def DarthPlagueis():
    # Not Background Audio, Use wait_done()
    sa.stop_all()
    dpw = "./audio_source/DPW.wav"
    dpw_obj = sa.WaveObject.from_wave_file(dpw)
    dpw_obj.play().wait_done()


def DontTryIt():
    # Not background audio, use wait_done()
    sa.stop_all()
    dti = "./audio_source/DontTryIt.wav"
    dti_obj = sa.WaveObject.from_wave_file(dti)
    dti_obj.play().wait_done()


def MainTheme():
    # background audio, do not use wait_done()
    sa.stop_all()
    swt = "./audio_source/StarWarsTheme.wav"
    swt_obj = sa.WaveObject.from_wave_file(swt)
    swt_obj.play()


def Betrayal():
    # background audio, do not use wait_done()
    sa.stop_all()
    abt = "./audio_source/AnakinBetrayal.wav"
    abt_obj = sa.WaveObject.from_wave_file(abt)
    abt_obj.play()


def Cantina():
    # background audio, do not use wait_done()
    sa.stop_all()
    cm = "./audio_source/CantinaMusic.wav"
    cm_obj = sa.WaveObject.from_wave_file(cm)
    cm_obj.play()


def Deeds():
    # background audio, do not use wait_done()
    sa.stop_all()
    ddd = "./audio_source/DarkDeeds.wav"
    ddd_obj = sa.WaveObject.from_wave_file(ddd)
    ddd_obj.play()


def ImpMarch():
    # background audio, do not use wait_done()
    sa.stop_all()
    march = "./audio_source/ImperialMarch.wav"
    march_obj = sa.WaveObject.from_wave_file(march)
    march_obj.play()


def Immolation():
    # Not background Audio, use wait_done()
    sa.stop_all()
    chosen = "./audio_source/ChosenOne.wav"
    chosen_obj = sa.WaveObject.from_wave_file(chosen)
    chosen_obj.play().wait_done()
