import os
import sys
import platform
import getpass
import configparser
from pathlib import Path


def name():
    return "Automatizator"


def version():
    return 1.0


def color_blue():
    return "#4b699b"


def color_green():
    return "#556B2F"


def color_yellow():
    return "#8e7746"


def color_red():
    return "#8e4646"


def preference_dir():
    user = getpass.getuser()
    dir_pref = {"Darwin": "/Users/" + user + "/Library/Application Support/" + name(),
                "Windows": "C:/Users/" + user + "/AppData/Local/" + name(),
                "Linux": "/home/" + user + "/.local/share/" + name()}[platform.system()]
    return dir_pref


def preference_path():
    dir_pref = preference_dir()
    if not os.path.isdir(dir_pref):
        os.makedirs(dir_pref)
    config = configparser.ConfigParser()
    file_pref = dir_pref + "/preferences.ini"
    if not os.path.isfile(file_pref):
        config.add_section("LOCALE")
        config.set("LOCALE", "language", "en")
        config.set("LOCALE", "recent1", "")
        config.set("LOCALE", "recent2", "")
        config.set("LOCALE", "recent3", "")
        config.set("LOCALE", "recent4", "")
        config.set("LOCALE", "recent5", "")
        config.set("LOCALE", "recent6", "")
        with open(file_pref, "w") as configfile:  # Save prefs
            config.write(configfile)
    return file_pref


def get_preferences():
    file_pref = preference_path()
    config = configparser.ConfigParser()
    config.read(file_pref)
    return config


def get_language():
    lang = get_preferences()["LOCALE"]["language"]
    return lang


def get_recent():
    recent = [get_preferences()["LOCALE"]["recent1"],
              get_preferences()["LOCALE"]["recent2"],
              get_preferences()["LOCALE"]["recent3"],
              get_preferences()["LOCALE"]["recent4"],
              get_preferences()["LOCALE"]["recent5"],
              get_preferences()["LOCALE"]["recent6"]]
    return recent


def get_dictionary():
    config = configparser.ConfigParser()
    lang = get_language()
    file_lang = app_path() + "/language/" + lang + ".ini"
    config.read(file_lang)
    return config[lang.upper()]


def app_path():
    return str(Path(__file__).parent.parent.parent).replace("\\", "/")


def soft_name():
    if "maya" in sys.modules:
        return "maya"
    if "hou" in sys.modules:
        return "houdini"


def default_actions():
    actions = {
        "info": {
            "version": version()},
        "action": {
            "main_actions":
                [{"enable": True,  # Enable/disable action
                  "name": "",  # Script name for convenience
                  "soft": "",  # If the software is specified, then the action will be visible only in it.
                  "run": "allways",  # Under what conditions will the action work?
                  "override": False,  # This is the same action, only it replaces or complements the parent.
                  # conditions. This is useful if you have a pipeline and in a certain series
                  # you need to adjust the parent action.
                  # "blend": "instead",
                  # Parameter for child actions. Specifies whether the action will replace or
                  # augment the parent action.
                  "type": None,  # Mode action: set attribute or custom script
                  # "enable_build": True,  # Enable build step or leave only checker?
                  # "build_script": "",  # For only type script. The script itself with the return.
                  # "enable_check": True,  # Enable checker step or leave only builder?
                  # "check": ""  # For only type script. The script itself with the return.
                  }]},
        "button": {
            "main_buttons": [{"name": "Button name",  # The name that will be displayed on the button itself.
                              # Button showed and worked only Checker mode.
                              "soft": "",  # If the software is specified, then the action will be visible only in it.
                              "script": ""  # The command that will be displayed when the button is clicked.
                              # The button will be pressed automatically if all actions receive successful statuses.
                              }]
        },
        "output": {
            "output_actions": {
                "actions": "main_actions",
                "buttons": "main_buttons"
            }
        }}
    return actions

