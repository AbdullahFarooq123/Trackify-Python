import ctypes
import json
import os
import sys

from PyQt5 import QtWidgets

import user_screen
from Login import Ui_Form
from trackify_app import views
from user_screen import Ui_MainWindow

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trackify_database.settings")


# from trackify_app import views


def show_user_window(username: str, remember_me=True):
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(username)
    MainWindow.closeEvent = lambda event: user_screen.closeEvent(ui, event, remember_me=remember_me)
    ui.setupUi(MainWindow)
    MainWindow.show()
    return app.exec_()


def show_login():
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    app.exec_()
    return ui


ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
try:
    with open('current_user.json', 'r') as current_user:
        current_user_credentials = json.load(current_user)
        current_user_username = current_user_credentials['username']
        current_user_password = current_user_credentials['password']
        returned_value = views.sign_in(current_user_username,current_user_password)
        if returned_value is not False:
            show_user_window(username=current_user_username)
        else:
            raise KeyError
except (FileNotFoundError, KeyError):
    login = show_login()
    if login.did_signin:
        sys.exit(show_user_window(remember_me=login.remember_me, username=login.username))
