from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = int(power)


    def run(self):
        print(f'{self.name}, на нас напали!')
        batt_days = 0
        enemyes = 100
        while enemyes > 0:
            enemyes -= self.power
            batt_days += 1
            print(f'{self.name} сражается {batt_days} день(дня)..., осталось {enemyes} воинов.')
            sleep(1)
        print(f'{self.name} одержал победу спустя {batt_days} дней(дня)!')


threads = []

first_knight = Knight('Sir Lancelot', 10)
first_knight.start()
second_knight = Knight("Sir Galahad", 20)
second_knight.start()

threads.append(first_knight)
threads.append(second_knight)

for thread in threads:
    thread.join()

print(f'Все битвы окончены!')

