class robotStatus:
    ALIVE = 0
    DEAD  = 1
    CRASH = 2
    WATER = 3

BATTERY_VAL = 10
class robot:
    # mapa, x, y, bateria
    def __init__(self, T, x, y, b):
        self.__T = T
        self.__x = x
        self.__y = y
        self.__b = b

    def left(self, val = 1):
        return self
    def right(self, val = 1):
        return self
    def up(self, val = 1):
        return self
    def down(self, val = 1):
        return self

    def get_status(self):
        if self.get_battery == 0:
            return robotStatus.DEAD

        T, x, y = self.__T, self.get_x(), self.get_y()

        if T[x][y] == 'T':
            return robotStatus.ALIVE
        elif T[x][y] == 'W':
            return robotStatus.WATER
        return robotStatus.CRASH

    def get_battery(self):
        return self.__b

    def get_map(self):
        status = self.get_status()
        x, y = self.get_x(), self.get_y()
        T = self.__T

        if status == robotStatus.ALIVE:
            T[x][y] = 'R'
            return T
        T[x][y] = 'x'
        return T

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
