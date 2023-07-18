from signal import Signal

if __name__ == "__main__":
    SAMPLE_RATE = int(input("Введите частоту дискретизации: "))
    DURATION = int(input("Введите продолжительность волн (мс): "))
    count = int(input("Введите кол-во волн: "))
    mysignal = Signal(SAMPLE_RATE, DURATION, count)
    mysignal.fourier_transform()
