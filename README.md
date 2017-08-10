# FTSpecViewer

## A PyQt5 application written for microwave spectroscopy analysis

---

## Introduction

 FTSpecViewer was written to assist in the interactive and exploratory analysis
 of microwave spectra. While there are many proprietary programs that are capable
  of performing the similar analyses (such as Origin and Igor) there are few that
  are specialized; filtering and fitting, for example, can be routinely done with
  these programs, however support for techniques such as double resonance and overlaying
  catalog spectra are not as well accounted for.

FTSpecViewer was written to be open source -- hence the choice of Qt and Python.
Please feel free to make any modifications and contributions to the code. For now,
I've tried to minimize the number of additional packages required for the sake of
 portability, but we will see how far the program develops.

Usage is pretty straightforward - load an experimental spectrum, look for peaks,
get quantitative values, etc.

The theming was done using Qt stylesheets - the colors were chosen/inspired by
 "Mathemagiker", created by Benedict Leicht.

http://www.awwwards.com/best-websites/mathemagiker/

## Features

- Loading and reading general ASCII spectra (tab delimited) and support for additional
 file types, such as SPFIT/SPCAT.

- Signal processing routines, such as window functions and various filters.

- Overlay catalog spectra to assist with assignment.

## To-do

- Point-and-click peaks, and corresponding fits to extract spectroscopic parameters
 (harmonic progressions)

- Multidimensional spectral analysis; time evolution of chirped-pulse spectra

## Running FTSpecViewer

The program can be run via command line by calling `python app.py`, which is a script
 in the `python/` folder that drives the application.
