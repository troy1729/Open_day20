from __future__ import print_function
import requests
import os
from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver
from django.shortcuts import render
import subprocess
import sys
from subprocess import run,PIPE
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import librosa
import librosa.display
import numpy as np
from playsound import playsound
import glob
import winsound



def button(request):
    return render(request,'t&t.html')
def external(request):
    files = glob.glob('media/*.wav')
    for f in files:
        os.remove(f)
    file = glob.glob('media/*.mp3')
    for f in file:
        os.remove(f)
    aud=request.FILES['file']
    print("audio is ",aud)
    fs=FileSystemStorage()
    filename=fs.save(aud.name,aud)
    fileurl=fs.open(filename)
    templateurl=fs.url(filename)
    print("file raw url",filename)
    print("file full url", fileurl)
    print("template url",templateurl)
    print("dodo")
    print("dodo")
    return render(request, 't&t.html')
def org(request):
    for wave_file in glob.glob("media/*.wav"):
        y, sr = librosa.load(wave_file, sr=None)
        librosa.output.write_wav('new/i.wav',y, sr)
        winsound.PlaySound('new/i.wav', winsound.SND_FILENAME)
    return render(request, 't&t.html') 
def pitch(request):
    for wave_file in glob.glob("media/*.wav"):
        y, sr = librosa.load(wave_file, sr=None)
        sr1 = int(sr*2)
        librosa.output.write_wav('new/a.wav',y, sr1)
        winsound.PlaySound('new/a.wav', winsound.SND_FILENAME)
    return render(request, 't&t.html') 
def pitc(request):
    for wave_file in glob.glob("media/*.wav"):
        y, sr = librosa.load(wave_file, sr=None)
        sr1 = int(sr/1.3)
        librosa.output.write_wav('new/b.wav',y, sr1)
        winsound.PlaySound('new/b.wav', winsound.SND_FILENAME)
    return render(request, 't&t.html')
def rev(request):
    for wave_file in glob.glob("media/*.wav"):
        y, sr = librosa.load(wave_file, sr=None)
        y1 = [0]*len(y)
        for i in range(len(y)):
            y1[i] = y[len(y)-i-1]
        y2 = np.asarray(y1)
        librosa.output.write_wav('new/c.wav',y2, sr)
        winsound.PlaySound('new/c.wav', winsound.SND_FILENAME)
    return render(request, 't&t.html')
def hp(request):
    for wave_file in glob.glob("media/*.wav"):
        y, sr = librosa.load(wave_file, sr=None)
        y_third = librosa.effects.pitch_shift(y, sr, n_steps=6)
        librosa.output.write_wav('new/d.wav',y_third, sr)
        winsound.PlaySound('new/d.wav', winsound.SND_FILENAME)
    return render(request, 't&t.html')
def lp(request):
    for wave_file in glob.glob("media/*.wav"):
        y, sr = librosa.load(wave_file, sr=None)
        y_for = librosa.effects.pitch_shift(y, sr, n_steps=-6)
        librosa.output.write_wav('new/e.wav',y_for, sr)
        winsound.PlaySound('new/e.wav', winsound.SND_FILENAME)
    return render(request, 't&t.html')
def we(request):
    for wave_file in glob.glob("media/*.wav"):
        y, sr = librosa.load(wave_file, sr=None)
        N = 10000
        y1 = np.pad(y, (N, 0), 'constant')
        y_third = librosa.effects.pitch_shift(y, sr, n_steps=6)
        N = 10000
        y_third = np.pad(y, (0, N), 'constant')
        y3=y_third+y1
        librosa.output.write_wav('new/f.wav',y3, sr)
        winsound.PlaySound('new/f.wav', winsound.SND_FILENAME)
    return render(request, 't&t.html')
def ry(request):
    for wave_file in glob.glob("media/*.wav"):
        y, sr = librosa.load(wave_file, sr=None)
        dura= librosa.get_duration(y=y, sr=sr)
        tt = np.linspace(0, dura, dura * sr, False)
        note = np.sin( (2 * np.pi)*(300 * tt))
        N=0
        note = np.pad(y, (0, N), 'constant')
        y3=y*note
        librosa.output.write_wav('new/g.wav',y3, sr)
        winsound.PlaySound('new/g.wav', winsound.SND_FILENAME)
    return render(request, 't&t.html')
def mip(request):
    for wave_file in glob.glob("media/*.wav"):
        y, sr = librosa.load(wave_file, sr=None)
        (a,b,c,d,e,f)=np.split(y,6)
        b = librosa.effects.pitch_shift(b, sr, n_steps=-6)
        c = librosa.effects.pitch_shift(c, sr, n_steps=6)
        d = librosa.effects.pitch_shift(d, sr, n_steps=-3)
        e = librosa.effects.pitch_shift(e, sr, n_steps=3)
        vs = np.append(a,b)
        vs = np.append(vs,c)
        vs = np.append(vs,d)
        vs = np.append(vs,e)
        vs = np.append(vs,f)
        librosa.output.write_wav('new/h.wav',vs, sr)
        winsound.PlaySound('new/h.wav', winsound.SND_FILENAME)
    return render(request, 't&t.html')
    
        
    