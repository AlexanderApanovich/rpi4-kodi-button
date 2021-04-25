import subprocess
import time
import RPi.GPIO as GPIO

gpio_pin = 17

allProcessesCommand = "pgrep -f kodi".split()
runKodiCommand = "nohup kodi &".split()
closeKodiCommand = "kodi-send --host=192.168.100.17 --action='Quit'".split()

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def getKodiIsRunning():
    try:
        pids = subprocess.check_output(allProcessesCommand).split()
        pids = map(int, pids)
        return len(pids) > 0
    except Exception:
        return False


def runKodi():
    try:
        subprocess.check_output(runKodiCommand)
    except Exception:
        pass


def closeKodi():
    try:
        command = closeKodiCommand
        subprocess.check_output(command.split())
    except Exception:
        pass


def update():
    kodiIsRunning = getKodiIsRunning()
    if kodiIsRunning:
        pass
        # TODO: issue #1 Black screen on kodi close 
        # closeKodi()
    else:
        runKodi()


def init():
    while True:
        time.sleep(0.2)
        if GPIO.input(gpio_pin) == False:
            update()


init()
