from qgis.core import QgsFeature, QgsPoint, QgsGeometry, QgsProject, QgsField, QgsVectorLayer
from PyQt5.QtWidgets import QApplication, QFileDialog, QFormLayout, QLabel, QLineEdit, QWidget, QDialog, QPushButton, QVBoxLayout, QTextBrowser, QGroupBox, QGridLayout, QCheckBox, QAction
from PyQt5.QtCore import QVariant, QRect, Qt
from PyQt5.QtGui import *
import pandas as pd 
from datetime import datetime as dt
import os
from qgis.utils import iface, Qgis
from qgis.core import QgsWkbTypes

''' Append PATH in QGIS settings to import local script
or 

import sys
sys.path.append(<path to survey file folder>)
'''

from survey_script import ScriptWindow



window = ScriptWindow()








def survey():
    window.show()
    iface.messageBar().pushMessage('Survey Script Loaded')

action = QAction('Survey')
action.triggered.connect(survey)
#action.setIcon(QIcon(icon))
iface.addToolBarIcon(action)

