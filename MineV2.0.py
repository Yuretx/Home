import os
import subprocess
import time
import win32api
import win32gui
import re
import pyautogui
import ctypes

clients = [^M
    {^M
        'name':"[XXX] MinecraftOnly",^M
        'login':'XXX'
        'passwrd': 'XXX',^M
    },^M
    {^M
        'name': "[XXX] MinecraftOnly",^M
        'login': 'XXX',^M
        'passwrd': 'XXX',^M
    },^M
    {^M
        'name':"[XXX] MinecraftOnly" ,^M
        'login': 'XXX',^M
        'passwrd': 'XXX',^M
    },^M
]^M
^M
ait = time.sleep


def pixel(x, y):
    hdc = ctypes.windll.user32.GetDC(0)
    color = ctypes.windll.gdi32.GetPixel(hdc, x, y)
    r = color % 256
    g = (color // 256) % 256
    b = color // (256 ** 2)
    ctypes.windll.user32.ReleaseDC(0, hdc)
    return (r, g, b)

def find_window_by_search_mine(pattern):
    hwnd = win32gui.FindWindow(None, pattern)
    return hwnd


def get_win_pos():
    abxy = pyautogui.size()
    # print(f'Разрешение монитора = : {abxy}')
    # print(f'Высота = {abxy.width}')
    # print(f'Ширина = {abxy.height}')
    x = abxy.width / 2
    y = abxy.height / 2
    x1 = 968 / 2
    y1 = 576 / 2
    win_x = x - x1
    win_y = y - y1
    return int(win_x), int(win_y)


def execute_client(client):
    win_x, win_y = get_win_pos()
    # запустить лаунчер
    hwd = find_window_by_search_mine('MinecraftOnly')
    if hwd == 0:
        subprocess.Popen('C:\\Users\\Yuretx\\Desktop\\MinecraftOnly.exe')
        # w8 запуска лаунчера
        print('Ждём 15 сек до запуска лаунчера')
        wait(7)
        hwd = find_window_by_search_mine('MinecraftOnly')
    else:
        win32gui.SetForegroundWindow(hwd)
        

    # разлогинить
    print(hwd)
    pyautogui.press("alt")
    wait(1)
    pyautogui.click(win_x+776, win_y+18)
    win32gui.SetForegroundWindow(hwd)
    wait(1)
    pyautogui.click(win_x+776, win_y+130)

    # логин
    wait(1)
    win32gui.SetForegroundWindow(hwd)
    pyautogui.click(win_x+496, win_y+238)
    win32gui.SetForegroundWindow(hwd)
    pyautogui.keyDown('ctrl')
    win32gui.SetForegroundWindow(hwd)
    pyautogui.press('a')
    win32gui.SetForegroundWindow(hwd)
    pyautogui.keyUp('ctrl')
    win32gui.SetForegroundWindow(hwd)
    pyautogui.typewrite(client['login'])

    # пароль
    wait(1)
    win32gui.SetForegroundWindow(hwd)
    pyautogui.click(win_x+496, win_y+270)
    win32gui.SetForegroundWindow(hwd)
    pyautogui.keyDown('ctrl')
    win32gui.SetForegroundWindow(hwd)
    pyautogui.press('a')
    win32gui.SetForegroundWindow(hwd)
    pyautogui.keyUp('ctrl')
    win32gui.SetForegroundWindow(hwd)
    pyautogui.typewrite(client['passwrd'])
    wait(2)

    # авторизация
    aaaa = True
    while aaaa:
        r, g, b = pixel(win_x+681, win_y+308)
        if not (r == 0xD4 and g == 0xD4 and b == 0xD4):
            aaaa = False
        else:
            win32gui.SetForegroundWindow(hwd)
            pyautogui.click(win_x+582, win_y+303)
        wait(3)

    # запуск
    win32gui.SetForegroundWindow(hwd)
    pyautogui.click(win_x+490, win_y+527)

    print(f'Ждём 20 сек до запуска клиента: {client['name']}')
    wait(20)


def main():
    print('Программа запущена')
    win_x, win_y = get_win_pos()
    # в цикле проверка клинтов
    while True:
        for client in clients:
            print(f'Обработка клиента: {client['name']}')
            hwd = find_window_by_search_mine(client['name'])
            if hwd > 0:
                print(f'Клиент запущен: {client['name']}')
                print(f'Устанавливаем фокус клиента: {client['name']}')
                print(hwd)
                try:
                    win32gui.SetForegroundWindow(hwd)
                except:
                    pass
                # проверить на рабочий скрипт
                pyautogui.FAILSAFE = False
                pyautogui.press("alt")
                win32gui.SetForegroundWindow(hwd)
                pyautogui.press('0')
                r, g, b = pixel(win_x+5, win_y+62)
                wait(1)
                print(r, g, b)
                if not (r == 255 and g == 12 and b == 00 ):
                    print('Скрипт не запущен')
                    print('Запуск скрипта')
                    try:
                        win32gui.SetForegroundWindow(hwd)
                    except:
                        pass
                    pyautogui.click(win_x+746, win_y+276)
                    wait(1)
                else:
                    pyautogui.press('0')
                    print('Скрипт запущен')
                # проверить на дисконнект
                print(' проверить на дисконнект')
                pyautogui.FAILSAFE = False
                pyautogui.press("alt")
                win32gui.SetForegroundWindow(hwd)
                wait(1)
                r, g, b = pixel(win_x+636, win_y+455)
                print(r, g, b)
                pyautogui.moveTo(win_x+636, win_y+455)
                wait(3)
                if (r == 115 and g == 115 and b == 115):
                    print('Обнаружен дисконнект, выход')
                    pyautogui.keyDown('alt')
                    pyautogui.press('F4')
                    pyautogui.keyUp('alt')
                    wait(5)
                    print('Повторный запуск')
                    execute_client(client)
                else:
                    print (r,g,b)
                    print ('Клиент запущен')
            else:
                # запускаем клиенты если нужно
                execute_client(client)
        print('Ждём 60 сек до некст тика')
        time.sleep(60)


if __name__ == '__main__':
    main()
