"""
    utils.py

    Supplementary routines that are used across FTSpecViewer, such as
    the datetime module.
"""

from datetime import datetime
from PyQt5.QtCore import QDate


def FTDateTime(datestring):
    # Takes the comment line from a QtFTM batch containing the date
    # and serializes a datetime object for use between QtFTM and the
    # Qt calendar widget
    datelist = datestring.split()[:-1]         # Skip the comment flag
    datestring = " ".join(datelist)            # Reform the datestring
    return datetime.strptime(datestring, "%a %b %e %H:%M:%S %Y")


def Py2QtDateTime(datetime_obj):
    # Takes a python datetime object and serializes a QDate object.
    return QDate.fromString(datetime_obj.strftime("%Y-%m-%d"))
