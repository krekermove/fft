import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import rfft, rfftfreq

class Signal():
    def __init__(self, sample_rate, duration, count):
        self.SAMPLE_RATE = sample_rate  # Гц
        self.DURATION = duration / 1000  # Секунды
        self.k = 0  # Индекс волны
        self.flag = False
        self.count = count # Кол-во волн
        self.x = np.arange


    def generate_sine_wave(self, freq):
        x = np.arange(0, self.DURATION, 1/self.SAMPLE_RATE)
        # 2pi для преобразования в радианы
        y = float(input(f"Введите амплитуду для волны {self.k}: ")) * np.sin(2 * np.pi * x * freq + float(input(f"Введите фазу для волны {self.k}: ")))
        return x, y

    def input_freq(self):
        self.k += 1
        a = int(input(f"Введите частоту для волны {self.k}: "))
        return a

    def fourier_transform(self):
        if self.count > 0:
            self.x, mixed_tone = self.generate_sine_wave(self.input_freq())
        else:
            print("Кол-во сигналов должно быть больше 0")

        if self.count > 1:
            for i in range(0, self.count - 1):
                x, signal = self.generate_sine_wave(self.input_freq())
                mixed_tone += signal
            self.flag = True
            plt.plot(self.x * 1000, mixed_tone)
            plt.xlabel('Время (мс)')
            plt.ylabel('Амплитуда')
            plt.title('Сигнал')
            plt.show()
        elif self.count > 0:
            self.flag = True
            plt.plot(self.x * 1000, mixed_tone)
            plt.xlabel('Время (мс)')
            plt.ylabel('Амплитуда')
            plt.title('Сигнал')
            plt.show()

        if self.flag:
            n = int(self.SAMPLE_RATE * self.DURATION)
            yf = rfft(mixed_tone)
            xf = rfftfreq(n, 1 / self.SAMPLE_RATE)
            plt.plot(xf, np.abs(yf))
            plt.xlabel('Частота (Гц)')
            plt.ylabel('Амплитуда')
            plt.title('Спектр Фурье')
            plt.show()