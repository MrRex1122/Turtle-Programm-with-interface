
from PyQt6 import uic, QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
import turtle
from turtle import *
import random
import sys
from random import choice
import PyQt6.QtCore, PyQt6.QtGui, PyQt6.QtWidgets



class Ui_CSIT040Project(object):
    def setupUi(self, CSIT040Project):
        CSIT040Project.setObjectName("CSIT040Project")
        CSIT040Project.resize(444, 312)
        CSIT040Project.setSizeGripEnabled(False)
        self.Preset_1 = QtWidgets.QPushButton(CSIT040Project)
        self.Preset_1.setGeometry(QtCore.QRect(20, 20, 131, 61))
        self.Preset_1.setMouseTracking(False)
        self.Preset_1.setDefault(False)
        self.Preset_1.setFlat(False)
        self.Preset_1.setObjectName("Preset_1")
        self.Preset_3 = QtWidgets.QPushButton(CSIT040Project)
        self.Preset_3.setGeometry(QtCore.QRect(20, 140, 131, 61))
        self.Preset_3.setObjectName("Preset_3")
        self.Preset_2 = QtWidgets.QPushButton(CSIT040Project)
        self.Preset_2.setGeometry(QtCore.QRect(20, 80, 131, 61))
        self.Preset_2.setObjectName("Preset_2")
        self.Random = QtWidgets.QPushButton(CSIT040Project)
        self.Random.setGeometry(QtCore.QRect(20, 200, 131, 61))
        self.Random.setObjectName("Random")
        self.Start_button = QtWidgets.QPushButton(CSIT040Project)
        self.Start_button.setGeometry(QtCore.QRect(230, 230, 171, 51))
        self.Start_button.setObjectName("Start_button")
        self.RGB_button = QtWidgets.QCheckBox(CSIT040Project)
        self.RGB_button.setGeometry(QtCore.QRect(220, 200, 41, 16))
        self.RGB_button.setObjectName("RGB_button")
        self.Red_box = QtWidgets.QSpinBox(CSIT040Project)
        self.Red_box.setGeometry(QtCore.QRect(171, 140, 51, 22))
        self.Red_box.setMaximum(255)
        self.Red_box.setObjectName("Red_box")
        self.Green_box = QtWidgets.QSpinBox(CSIT040Project)
        self.Green_box.setGeometry(QtCore.QRect(220, 140, 51, 22))
        self.Green_box.setMaximum(255)
        self.Green_box.setObjectName("Green_box")
        self.Blue_box = QtWidgets.QSpinBox(CSIT040Project)
        self.Blue_box.setGeometry(QtCore.QRect(270, 140, 51, 22))
        self.Blue_box.setMaximum(255)
        self.Blue_box.setObjectName("Blue_box")
        self.RGB_text = QtWidgets.QTextBrowser(CSIT040Project)
        self.RGB_text.setGeometry(QtCore.QRect(170, 100, 141, 31))
        self.RGB_text.setObjectName("RGB_text")
        self.OR = QtWidgets.QTextBrowser(CSIT040Project)
        self.OR.setGeometry(QtCore.QRect(200, 170, 81, 21))
        self.OR.setObjectName("OR")
        self.Speed_text = QtWidgets.QTextBrowser(CSIT040Project)
        self.Speed_text.setGeometry(QtCore.QRect(380, 100, 51, 31))
        self.Speed_text.setObjectName("Speed_text")
        self.Rotation_text = QtWidgets.QTextBrowser(CSIT040Project)
        self.Rotation_text.setGeometry(QtCore.QRect(330, 100, 51, 31))
        self.Rotation_text.setObjectName("Rotation_text")
        self.Speed_box = QtWidgets.QSpinBox(CSIT040Project)
        self.Speed_box.setGeometry(QtCore.QRect(380, 140, 51, 22))
        self.Speed_box.setMaximum(1000)
        self.Speed_box.setObjectName("Speed_box")
        self.Rotation_box = QtWidgets.QSpinBox(CSIT040Project)
        self.Rotation_box.setGeometry(QtCore.QRect(330, 140, 51, 22))
        self.Rotation_box.setMaximum(360)
        self.Rotation_box.setObjectName("Rotation_box")
        self.RGB_text_2 = QtWidgets.QTextBrowser(CSIT040Project)
        self.RGB_text_2.setGeometry(QtCore.QRect(170, 20, 261, 31))
        self.RGB_text_2.setObjectName("RGB_text_2")
        self.RGB_text_3 = QtWidgets.QTextBrowser(CSIT040Project)
        self.RGB_text_3.setGeometry(QtCore.QRect(170, 60, 261, 31))
        self.RGB_text_3.setObjectName("RGB_text_3")
        self.toolButton = QtWidgets.QToolButton(CSIT040Project)
        self.toolButton.setGeometry(QtCore.QRect(410, 0, 21, 16))
        self.toolButton.setObjectName("toolButton")
        self.retranslateUi(CSIT040Project)
        QtCore.QMetaObject.connectSlotsByName(CSIT040Project)
        self.add_applications()


    def retranslateUi(self, CSIT040Project):
        _translate = QtCore.QCoreApplication.translate
        CSIT040Project.setWindowTitle(_translate("CSIT040Project", "CSIT040Project"))
        self.Preset_1.setText(_translate("CSIT040Project", "Preset 1"))
        self.Preset_3.setText(_translate("CSIT040Project", "Preset 3"))
        self.Preset_2.setText(_translate("CSIT040Project", "Preset 2"))
        self.Random.setText(_translate("CSIT040Project", "Random"))
        self.Start_button.setText(_translate("CSIT040Project", "Start"))
        self.RGB_button.setText(_translate("CSIT040Project", "RGB"))
        self.RGB_text.setHtml(_translate("CSIT040Project", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Red;     Green;     Blue</span></p></body></html>"))
        self.OR.setHtml(_translate("CSIT040Project", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">OR</p></body></html>"))
        self.Speed_text.setHtml(_translate("CSIT040Project", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Speed</p></body></html>"))
        self.Rotation_text.setHtml(_translate("CSIT040Project", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Rotation</p></body></html>"))
        self.RGB_text_2.setHtml(_translate("CSIT040Project", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Python Turtle Art Program v.1</span></p></body></html>"))
        self.RGB_text_3.setHtml(_translate("CSIT040Project", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Enter your variant or use preset</span></p></body></html>"))
        self.toolButton.setText(_translate("CSIT040Project", "..."))

    def on_button_clicked(self):
        print("Clicked")

    def rgb_spiral(self):
        RGB = self.RGB_button.isChecked()
        Red, Green, Blue = self.Red_box.value(), self.Green_box.value(), self.Blue_box.value()
        drawing_speed = self.Speed_box.value()
        rotation = self.Rotation_box.value()

        turtle.title("RGB Spliral")
        turtle.TurtleScreen._RUNNING = True
        speed(drawing_speed)
        bgcolor("black")
        r, g, b = Red, Green, Blue

        for i in range(255 * 2):

            colormode(255)
            if RGB == True:
                if i < 255 // 3 and g < 250:
                    g += 5
                elif i < 255 * 2 // 3 and r > 5:
                    r -= 5
                elif i < 255 and b < 250:
                    b += 5
                elif i < 255 * 4 // 3 and g > 5:
                    g -= 5
                elif i < 255 * 5 // 3 and r < 250:
                    r += 5
                elif b > 5:
                    b -= 5
            fd(60 + i)
            rt(rotation)
            pencolor(r, g, b)

    def random_spiral(self, drawing_speed, rotation, RGB, Red, Green, Blue):
        turtle.title("RGB Spliral")
        turtle.TurtleScreen._RUNNING = True
        speed(drawing_speed)
        bgcolor("black")
        r, g, b = Red, Green, Blue

        for i in range(255 * 2):

            colormode(255)
            if RGB == True:
                if i < 255 // 3 and g < 250:
                    g += 5
                elif i < 255 * 2 // 3 and r > 5:
                    r -= 5
                elif i < 255 and b < 250:
                    b += 5
                elif i < 255 * 4 // 3 and g > 5:
                    g -= 5
                elif i < 255 * 5 // 3 and r < 250:
                    r += 5
                elif b > 5:
                    b -= 5
            fd(60 + i)
            rt(rotation)
            pencolor(r, g, b)




    def example_1(self):
        import turtle
        import colorsys


        bgcolor("black")
        t = turtle.Turtle()
        turtle.Screen().bgcolor("black")
        t.speed(100)
        n = 36
        h = 0
        for i in range(460):
            c = colorsys.hsv_to_rgb(h, 1, 0.9)
            h += 1 / n
            t.color(c)
            t.left(145)
            for i in range(5):
                t.forward(300)
                t.left(150)
        turtle.done()

    def example_2(self):
        squary = turtle.Turtle()
        squary.speed(10)

        for i in range(500):  # this "for" loop will repeat these functions 500 times
            squary.forward(i)
            squary.left(91)

    def example_3(self):
        wn = turtle.Screen()
        wn.bgcolor("black")
        astroid = turtle.Turtle()
        astroid.speed(0)
        triad = turtle.Turtle()
        triad.speed(0)
        triad.up()
        triad.goto(-120, 120)
        triad.down()
        squad = turtle.Turtle()
        squad.speed(0)
        squad.up()
        squad.goto(120, 120)
        squad.down()
        pentago = turtle.Turtle()
        pentago.speed(0)
        pentago.up()
        pentago.goto(-120, -120)
        pentago.down()
        octago = turtle.Turtle()
        octago.speed(0)
        octago.up()
        octago.goto(120, -120)
        octago.down()
        colors = ["red", "gold", "blue", "green", "white", "cyan", "pink"]

        for i in range(50):
            triad.color(random.choice(colors))
            triad.forward(i * 3)
            triad.left(120)

        for i in range(50):
            squad.color(random.choice(colors))
            squad.forward(i * 2)
            squad.left(90)

        for i in range(50):
            pentago.color(random.choice(colors))
            pentago.forward(i * 2)
            pentago.left(72)

        for i in range(75):
            octago.color(random.choice(colors))
            octago.forward(i)
            octago.left(60)

        for i in range(50):
            astroid.color(random.choice(colors))
            astroid.forward(i * 3)
            astroid.left(144)

        triad.up()
        triad.goto(-110, 200)
        triad.down()
        triad.write("Triad")
        triad.hideturtle()

        squad.up()
        squad.goto(120, 180)
        squad.down()
        squad.write("Squad")
        squad.hideturtle()

        pentago.up()
        pentago.goto(-140, -20)
        pentago.write("Pentago")
        pentago.hideturtle()

        octago.up()
        octago.goto(120, -40)
        octago.down()
        octago.write("Hex")
        octago.hideturtle()

        astroid.up()
        astroid.goto(0, 60)
        astroid.down()
        astroid.write("Astroid")
        astroid.hideturtle()

        turtle.done()


    def random_values(self):
        drawing_speed = random.randrange(1, 1001)
        rotation = random.randrange(1, 361)
        Red = random.randrange(1, 256)
        Green = random.randrange(1, 256)
        Blue = random.randrange(1, 256)
        RGB = random.choice([True, False])
        self.random_spiral(drawing_speed, rotation, RGB, Red, Green, Blue)

    def add_applications(self):
        self.Preset_1.clicked.connect(self.example_1)
        self.Start_button.clicked.connect(self.rgb_spiral)
        self.Preset_2.clicked.connect(self.example_2)
        self.Preset_3.clicked.connect(self.example_3)
        self.Random.clicked.connect(self.random_values)



def application():
    app = QApplication(sys.argv)
    window = QDialog()
    ui = Ui_CSIT040Project()
    ui.setupUi(window)
    window.show()
    app.exec()





if __name__ == '__main__':
    application()
