#!/bin/bash

pyuic5 BatchViewer.ui -o ../python/qtbatch.py
pyuic5 BatchCreator.ui -o ../python/qtbatchcreator.py
pyuic5 ScanChooser.ui -o ../python/qtchooser.py
pyuic5 MainWindow.ui -o ../python/qtmain.py
pyuic5 Settings.ui -o ../python/qtsettings.py

pyrcc5 fonts.qrc -o ../python/fonts_rc.py
pyrcc5 icons.qrc -o ../python/icons_rc.py
