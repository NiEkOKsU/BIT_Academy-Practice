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
        self.__s = None

    def left(self, val = 1):
        st = self.get_status()
        self.set_status(st)
        battery = self.get_battery()
        if val > 0 and st == robotStatus.ALIVE and battery >= 0:
            map = self.get_map()
            x, y = self.get_x(), self.get_y()
            self.__T[x][y] = 'T'
            if y - val < 0:
                y -= 1
                flag = 1
                while battery >= 0 and y > 0:
                    if map[x][y] == 'T':
                        y -= 1
                        battery -= 1
                    elif map[x][y] == 'B':
                        battery += BATTERY_VAL - 1
                        map[x][y] = 'T'
                        self.__T[x][y] = 'T'
                        y -= 1
                    elif map[x][y] == 'W':
                        flag = 0
                        self.set_battery(battery)
                        self.set_y(y)
                        self.set_status(robotStatus.WATER)
                        break
                    elif map[x][y] == 'G':
                        flag = 0
                        self.set_battery(battery)
                        self.set_y(y + 1)
                        self.set_status(robotStatus.CRASH)
                        break
                if flag == 1:
                    if battery < 0:
                        self.set_battery(0)
                        self.set_y(y + 1)
                        self.set_status(robotStatus.DEAD)
                    elif battery == 0 and y == 0:
                        if map[x][y] != 'B':
                            self.set_battery(0)
                            self.set_y(0)
                            self.set_status(robotStatus.DEAD)
                        else:
                            self.set_battery(BATTERY_VAL)
                            map[x][y] = 'T'
                            self.__T[x][y] = 'T'
                            self.set_y(0)
                            self.set_status(robotStatus.CRASH)
                    else:
                        self.set_battery(battery - 1)
                        self.set_y(0)
                        self.set_status(robotStatus.CRASH)
            else:
                for i in range(y - 1, y - val-1, -1):
                    battery -= 1
                    if battery < 0:
                        self.set_status(robotStatus.DEAD)
                        self.set_battery(0)
                        self.set_y(i+1)
                        break
                    elif map[x][i] != 'T':
                        if map[x][i] == 'B':
                            battery += BATTERY_VAL
                            map[x][i] = 'T'
                            self.__T[x][i] = 'T'
                        elif map[x][i] == 'W':
                            self.set_status(robotStatus.WATER)
                            self.set_battery(battery)
                            self.set_y(i)
                            break
                        elif map[x][i] == 'G':
                            self.set_status(robotStatus.CRASH)
                            self.set_battery(battery)
                            self.set_y(i + 1)
                            break
                if battery == 0 and self.get_status() == robotStatus.ALIVE:
                    if map[x][y - val-1] != 'B':
                        self.set_status(robotStatus.DEAD)
                        self.set_y(y - val)
                        self.set_battery(battery)
                    else:
                        self.set_y(y - val)
                        self.set_battery(battery)
                elif self.get_status() == robotStatus.ALIVE:
                    self.set_y(y - val)
                    self.set_battery(battery)
        return self

    def right(self, val = 1):
        st = self.get_status()
        battery = self.get_battery()
        self.set_status(st)
        if val > 0 and st == robotStatus.ALIVE and battery >= 0:
            map = self.get_map()
            x, y = self.get_x(), self.get_y()
            self.__T[x][y] = 'T'
            len_map_y = len(map[x])
            if y + val > len_map_y - 1:
                y += 1
                flag = 1
                while battery >= 0 and y < len_map_y - 1:
                    if map[x][y] == 'T':
                        y += 1
                        battery -= 1
                    elif map[x][y] == 'B':
                        battery += BATTERY_VAL - 1
                        map[x][y] = 'T'
                        self.__T[x][y] = 'T'
                        y += 1
                    elif map[x][y] == 'W':
                        flag = 0
                        self.set_battery(battery)
                        self.set_y(y)
                        self.set_status(robotStatus.WATER)
                        break
                    elif map[x][y] == 'G':
                        flag = 0
                        self.set_battery(battery)
                        self.set_y(y - 1)
                        self.set_status(robotStatus.CRASH)
                        break
                if flag == 1:
                    if battery < 0:
                        self.set_battery(0)
                        self.set_y(y - 1)
                        self.set_status(robotStatus.DEAD)
                    elif battery == 0 and y == len_map_y - 1:
                        if map[x][y] != 'B':
                            self.set_battery(0)
                            self.set_y(y)
                            self.set_status(robotStatus.DEAD)
                        else:
                            self.set_battery(BATTERY_VAL)
                            map[x][y] = 'T'
                            self.__T[x][y] = 'T'
                            self.set_y(y)
                            self.set_status(robotStatus.CRASH)
                    else:
                        self.set_battery(battery - 1)
                        self.set_y(len_map_y - 1)
                        self.set_status(robotStatus.CRASH)
            else:
                for i in range(y + 1, y + val + 1):
                    battery -= 1
                    if battery < 0:
                        self.set_status(robotStatus.DEAD)
                        self.set_battery(0)
                        self.set_y(i - 1)
                        break
                    elif map[x][i] != 'T':
                        if map[x][i] == 'B':
                            battery += BATTERY_VAL
                            self.__T[x][i] = 'T'
                            map[x][i] = 'T'
                        elif map[x][i] == 'W':
                            self.set_status(robotStatus.WATER)
                            self.set_battery(battery)
                            self.set_y(i)
                            break
                        elif map[x][i] == 'G':
                            self.set_status(robotStatus.CRASH)
                            self.set_battery(battery)
                            self.set_y(i - 1)
                            break
                if battery == 0 and self.get_status() == robotStatus.ALIVE:
                    if map[x][y + val + 1] != 'B':
                        self.set_status(robotStatus.DEAD)
                        self.set_y(y + val)
                        self.set_battery(battery)
                    else:
                        self.set_y(y + val)
                        self.set_battery(battery)
                elif self.get_status() == robotStatus.ALIVE:
                    self.set_y(y + val)
                    self.set_battery(battery)
        return self

    def up(self, val = 1):
        st = self.get_status()
        self.set_status(st)
        battery = self.get_battery()
        if val > 0 and st == robotStatus.ALIVE and battery >= 0:
            map = self.get_map()
            x, y = self.get_x(), self.get_y()
            self.__T[x][y] = 'T'
            if x - val < 0:
                x -= 1
                flag = 1
                while battery >= 0 and x > 0:
                    if map[x][y] == 'T':
                        x -= 1
                        battery -= 1
                    elif map[x][y] == 'B':
                        battery += BATTERY_VAL - 1
                        map[x][y] = 'T'
                        self.__T[x][y] = 'T'
                        x -= 1
                    elif map[x][y] == 'W':
                        flag = 0
                        self.set_battery(battery)
                        self.set_x(x)
                        self.set_status(robotStatus.WATER)
                        break
                    elif map[x][y] == 'G':
                        flag = 0
                        self.set_battery(battery)
                        self.set_x(x - 1)
                        self.set_status(robotStatus.CRASH)
                        break
                if flag == 1:
                    if battery < 0:
                        self.set_battery(0)
                        self.set_x(x + 1)
                        self.set_status(robotStatus.DEAD)
                    elif battery == 0 and x == 0:
                        if map[x][y] != 'B':
                            self.set_battery(0)
                            self.set_x(0)
                            self.set_status(robotStatus.DEAD)
                        else:
                            self.set_battery(BATTERY_VAL)
                            map[x][y] = 'T'
                            self.__T[x][y] = 'T'
                            self.set_x(0)
                            self.set_status(robotStatus.CRASH)
                    else:
                        self.set_battery(battery - 1)
                        self.set_x(0)
                        self.set_status(robotStatus.CRASH)
            else:
                for i in range(x - 1, x - val - 1, -1):
                    battery -= 1
                    if battery < 0:
                        self.set_status(robotStatus.DEAD)
                        self.set_battery(0)
                        self.set_x(i + 1)
                        break
                    elif map[i][y] != 'T':
                        if map[i][y] == 'B':
                            battery += BATTERY_VAL
                            map[i][y] = 'T'
                            self.__T[i][y] = 'T'
                        elif map[i][y] == 'W':
                            self.set_status(robotStatus.WATER)
                            self.set_x(i)
                            self.set_battery(battery)
                            break
                        elif map[i][y] == 'G':
                            self.set_status(robotStatus.CRASH)
                            self.set_battery(battery)
                            self.set_x(i + 1)
                            break
                if battery == 0 and self.get_status() == robotStatus.ALIVE:
                    if map[x - val - 1][y] != 'B':
                        self.set_status(robotStatus.DEAD)
                        self.set_x(x - val)
                        self.set_battery(battery)
                    else:
                        self.set_x(x - val)
                        self.set_battery(battery)
                elif self.get_status() == robotStatus.ALIVE:
                    self.set_x(x - val)
                    self.set_battery(battery)
        return self
        
    def down(self, val = 1):
        st = self.get_status()
        self.set_status(st)
        battery = self.get_battery()
        if val > 0 and st == robotStatus.ALIVE and battery >= 0:
            map = self.get_map()
            x, y = self.get_x(), self.get_y()
            self.__T[x][y] = 'T'
            len_map_x = len(map)
            if x + val > len_map_x - 1:
                x += 1
                flag = 1
                while battery >= 0 and x < len_map_x - 1:
                    if map[x][y] == 'T':
                        x += 1
                        battery -= 1
                    elif map[x][y] == 'B':
                        battery += BATTERY_VAL - 1
                        map[x][y] = 'T'
                        self.__T[x][y] = 'T'
                        x += 1
                    elif map[x][y] == 'W':
                        flag = 0
                        self.set_battery(battery)
                        self.set_x(x)
                        self.set_status(robotStatus.WATER)
                        break
                    elif map[x][y] == 'G':
                        flag = 0
                        self.set_battery(battery)
                        self.set_x(x - 1)
                        self.set_status(robotStatus.CRASH)
                        break
                if flag == 1:
                    if battery < 0:
                        self.set_battery(0)
                        self.set_x(x - 1)
                        self.set_status(robotStatus.DEAD)
                    elif battery == 0:
                        if map[x][y] != 'B':
                            self.set_battery(0)
                            self.set_x(len_map_x - 1)
                            self.set_status(robotStatus.DEAD)
                        else:
                            self.set_battery(BATTERY_VAL)
                            map[x][y] = 'T'
                            self.__T[x][y] = 'T'
                            self.set_x(len_map_x - 1)
                            self.set_status(robotStatus.CRASH)
                    else:
                        self.set_battery(battery - 1)
                        self.set_x(len_map_x - 1)
                        self.set_status(robotStatus.CRASH)
            else:
                for i in range(x + 1, x + val + 1):
                    battery -= 1
                    if battery < 0:
                        self.set_status(robotStatus.DEAD)
                        self.set_battery(0)
                        self.set_x(i - 1)
                        break
                    elif map[i][y] != 'T':
                        if map[i][y] == 'B':
                            battery += BATTERY_VAL
                            map[i][y] = 'T'
                            self.__T[i][y] = 'T'
                        elif map[i][y] == 'W':
                            self.set_status(robotStatus.WATER)
                            self.set_x(i)
                            self.set_battery(battery)
                            break
                        elif map[i][y] == 'G':
                            self.set_status(robotStatus.CRASH)
                            self.set_x(i - 1)
                            self.set_battery(battery)
                            break
                if battery == 0 and self.get_status() == robotStatus.ALIVE:
                    if map[x + val+1][y] != 'B':
                        self.set_status(robotStatus.DEAD)
                        self.set_x(x + val)
                        self.set_battery(battery)
                    else:
                        self.set_x(x + val)
                        self.set_battery(battery)
                elif self.get_status() == robotStatus.ALIVE:
                    self.set_x(x + val)
                    self.set_battery(battery)
        return self


    def set_battery(self, bat):
        self.__b = bat
    def set_status(self, stat):
        self.__s = stat
    def set_x(self, x):
        self.__x = x
    def set_y(self, y):
        self.__y = y


    def get_status(self):
        if self.__s == None:
            if self.get_battery == 0:
                return robotStatus.DEAD

            T, x, y = self.__T, self.get_x(), self.get_y()

            if T[x][y] == 'T':
                return robotStatus.ALIVE
            elif T[x][y] == 'W':
                return robotStatus.WATER
            elif T[x][y] == 'B':
                self.__T[x][y] = 'T'
                T[x][y] = 'T'
                self.set_battery(self.get_battery() + BATTERY_VAL)
                return robotStatus.ALIVE
            return robotStatus.CRASH
        return self.__s

    def get_battery(self):
        return self.__b

    def get_map(self):
        status = self.get_status()
        x, y = self.get_x(), self.get_y()
        T = self.__T

        if status == robotStatus.ALIVE:
            T[x][y] = 'R'
            return T
        T[x][y] = 'X'
        return T

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
