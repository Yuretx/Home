import win32gui
import time
import pyautogui
import telebot

bot = telebot.TeleBot("token")
wait = time.sleep


#def send_message():
    #@bot.message_handler(commands=['start'])
    #def start_function(message):
            #chat_id = -4210462204 # Сюда помещаем id пользователя кому будет отправлено сообщение
            #bot.send_message(chat_id, 'Зайди, там новое задание \nhttps://t.me/notcoin_bot')
    #bot.polling(none_stop=True)

def start():
    chat_id = "@raveinthegrave2"
    bot.send_message(chat_id, 'Зайди, там новое задание \nhttps://t.me/notcoin_bot')

def search_not_window():
    hwnd = win32gui.FindWindow(None, "TelegramDesktop")
    return hwnd

def chooice_window():
    while True:
        hwd = search_not_window()
        win32gui.SetForegroundWindow(hwd)
        pyautogui.moveTo(853,683)
        r, g, b = pyautogui.pixel(824,603)
        print(r, g, b,"первый")
        if not (r == 28, g == 28, b == 30):
            win32gui.SetForegroundWindow(hwd)
            wait(5)
            print(r, g, b, 'vtoroy')
        else:
            start()
            print(r, g, b,'tretiy')
            wait(10)


if __name__ == '__main__':
    chooice_window()
