import os
from fcntl import ioctl


class Accellerometer():
    """Class abstracting the MMA7455L Accellerometer"""

    def __init__(self, int_pin):
        self.adress = 0x1D

        self.i2c = os.open("/dev/i2c-2", os.O_RDWR)
        ioctl(self.i2c, 0x703, self.adress)

    def get_x(self):
        os.write(self.i2c, 0x00)
        data = os.read(self.i2c, 2)
        print(data)


if __name__ == '__main__':
    a = Accellerometer()
    a.get_x()
