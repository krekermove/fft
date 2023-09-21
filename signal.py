import numpy as np
from matplotlib import pyplot as plt    # Библиотека отвечающая за вывод графиков
from scipy.fft import rfft, rfftfreq    # Библиотека с помощью которой происходит преобразование Фурье
import math


class Signal:                                   # Класс описывающий все действия связанные с волнами
    def __init__(self, sample_rate, duration):
        self.SAMPLE_RATE = sample_rate          # Частота дискритизации (Гц)
        self.DURATION = duration / 1000         # Продолжительность волн
        self.freq = []                          # Массив в котором хранятся все частоты волн которые введет пользователь
        self.altitude = []                      # Массив в котором хранятся все амплитуды волн которые введет пользователь
        self.phase = []                         # Массив в котором хранятся все фазы волн которые введет пользователь
        self.k = 0                              # Индекс волны
        self.flag = False
        self.x = np.arange                      # Массив в котором будут хранится координаты по оси x
        self.max_signal = 0                     # Макс значение сигнала
        self.skv_signal = 0                     # Среднеквадратичное значение сигнала
        self.max_spectrum = 0                   # Макс значение спектра
        self.sr_spectrum = 0                    # Среднее значение спектра

    def generate_sine_wave(self):               # Функция которая генерирует волны
        x = np.arange(0, self.DURATION, 1/self.SAMPLE_RATE) # Массив координат x
        # 2pi для преобразования в радианы
        y = self.altitude[self.k] * np.sin(2 * np.pi * x * self.freq[self.k] + self.phase[self.k]) # Массив координат y
        return x, y

    def fourier_transform(self):                # Функция которая выполняет преобразование Фурье и выводит графики
        self.x, mixed_tone = self.generate_sine_wave() #----------------------------------
        for i in range(1, 5):                          #
            self.k += 1                                #    Генерация 5ти волн с теми параметрами
            x, signal = self.generate_sine_wave()      #    которые ввел пользователь
            mixed_tone += signal                       #----------------------------------
        self.max_signal = max(mixed_tone)              # Определяем максимальное значение сигнала
        tmp = 0
        for i in mixed_tone:                             #--------------------------------
            tmp += i**2                                  # Определяем среднеквадратич значение сигнала
        self.skv_signal = math.sqrt(tmp/len(mixed_tone)) #--------------------------------
        plt.plot(self.x * 1000, mixed_tone)             #---------------------------------
        plt.xlabel('Время (мс)')                        #
        plt.ylabel('Амплитуда (Дб)')                    #   Создание и вывод первого графика
        plt.title('Сигнал')                             #   с получившимся сигналом из 5ти волн
        plt.show()                                      #---------------------------------

        n = int(self.SAMPLE_RATE * self.DURATION)       #---------------------------------
        yf = rfft(mixed_tone, norm="forward")           #
        yf *= 2                                         #
        xf = rfftfreq(n, 1 / self.SAMPLE_RATE)          #
        self.max_spectrum = max(np.abs(yf))             #   Подсчет максимального значения спектра
        tmp = 0                                         #
        for i in np.abs(yf):                            #
            tmp += i                                    #
        self.sr_spectrum = tmp/5                        #   Подсчет среднего значения спектра
        plt.plot(xf, np.abs(yf))                        #
        plt.xlabel('Частота (Гц)')                      #   Создание и вывод второго графика
        plt.ylabel('Амплитуда (Дб)')                    #   с получившимся спектром Фурье
        plt.title('Спектр Фурье')                       #
        plt.show()                                      #----------------------------------