import os
import subprocess
import time
import win32api
import win32gui
import re
import pyautogui
import ctypes

clients = [
    {
        'name':"[XXX] MinecraftOnly",
        'login':'XXX'
        'passwrd': 'XXX',
    },
    {
        'name': "[XXX] MinecraftOnly",
        'login': 'XXX',
        'passwrd': 'XXX',
    },
    {
        'name':"[XXX] MinecraftOnly" ,
        'login': 'XXX',
        'passwrd': 'XXX',
    },
]

wait = time.sleep


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
    hwd = find_window_by_search_mine('MinecraftOnly Launcher')
    if hwd == 0:
        subprocess.Popen('C:\\Users\\Yuretx\\Desktop\\MinecraftOnly.exe')
        # w8 запуска лаунчера
        print('Ждём 15 сек до запуска лаунчера')
        wait(7)
        hwd = find_window_by_search_mine('MinecraftOnly Launcher')
    else:
        try:
            win32gui.SetForegroundWindow(hwd)
        except:
            pass

    # разлогинить
    print(hwd)
    pyautogui.press("alt")
    try:
            win32gui.SetForegroundWindow(hwd)
    except:
            pass
    pyautogui.click(win_x+776, win_y+18)
    try:
            win32gui.SetForegroundWindow(hwd)
    except:
            pass
    pyautogui.click(win_x+776, win_y+130)

    # логин
    win32gui.SetForegroundWindow(hwd)
    pyautogui.click(897, 500)
    win32gui.SetForegroundWindow(hwd)
    pyautogui.keyDown('ctrl')
    win32gui.SetForegroundWindow(hwd)
    pyautogui.press('a')
    win32gui.SetForegroundWindow(hwd)
    pyautogui.keyUp('ctrl')
    win32gui.SetForegroundWindow(hwd)
    pyautogui.typewrite(client['login'])

    # пароль
    win32gui.SetForegroundWindow(hwd)
    pyautogui.click(884, 531)
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
        r, g, b = pixel(776,505 )
        if not (r == 0xD4 and g == 0xD4 and b == 0xD4):
            aaaa = False
        else:
            win32gui.SetForegroundWindow(hwd)
            pyautogui.click(1056, 562)
        wait(3)

    # запуск
    win32gui.SetForegroundWindow(hwd)
    pyautogui.click(981, 777)

    print(f'Ждём 20 сек до запуска клиента: {client['name']}')
    wait(20)


def main():
    print('Программа запущена')
    # в цикле проверка клинтов
    while True:
        for client in clients:
            print(f'Обработка клиента: {client['name']}')
            hwd = find_window_by_search_mine(client['name'])
            if hwd > 0:
                print(f'Клиент запущен: {client['name']}')
                print(f'Устанавливаес фокус клиента: {client['name']}')
                print(hwd)
                try:
                    win32gui.SetForegroundWindow(hwd)
                except:
                    pass
                # проверить на рабочий скрипт
                pyautogui.FAILSAFE = False
                pyautogui.press("alt")
                try:
                    win32gui.SetForegroundWindow(hwd)
                except:
                    pass
                wait(1)
                pyautogui.press('0')
                r, g, b = pixel(478, 306)
                print(r, g, b)
                pyautogui.moveTo(478, 306)
                wait(3)
                if not (r == 12 and g == 12 and b == 12 ):
                    print('Скрипт не запущен')
                    print('Запуск скрипта')
                    try:
                        win32gui.SetForegroundWindow(hwd)
                    except:
                        pass
                    pyautogui.click(1219, 523)
                    pyautogui.press('0')
                else:
                    print('Скрипт запущен')
                # проверить на дисконнект
                pyautogui.FAILSAFE = False
                pyautogui.press("alt")
                try:
                    win32gui.SetForegroundWindow(hwd)
                except:
                    pass
                wait(1)
                r, g, b = pixel(1232,603)
                print(r,g,b)
                pyautogui.moveTo(1130,708)
                wait(3)
                if (r == 38 and g == 27 and b == 19):
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
        print('Ждём 5 мин до некст тика')
        time.sleep(300)


if __name__ == '__main__':
    main()
