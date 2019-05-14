import serial
import time
import serial.tools.list_ports

ser = None


def get_ports():
    """Collect all ports n store to ports var"""
    ports = serial.tools.list_ports.comports()
    return ports


print(get_ports()[1])


def find_arduino(portsfound):
    """wil find Ardino port"""
    comPort = 'None'
    num_of_connection = len(portsfound)

    for i in range(0, num_of_connection):
        port = foundPorts[i]
        cnvt_str_port = str(port)

        if 'ttyACM' in cnvt_str_port:
            splitPort = cnvt_str_port.split(' ')
            comPort = (splitPort[0])

    return comPort


foundPorts = get_ports()
connectPort = find_arduino(foundPorts)


if connectPort != 'None':
    ser = serial.Serial(connectPort, 9600, timeout=1)
    print("Connected to Arduino in  : " + connectPort)
else:
    print("Connection Error- Cannot find Arduino in SYS port  ")
print('Connection process Finished ')


def getarduinodata():
    data = ser.readlines()
    return data

# def direct_write(senddata):
#
#     for i in senddata:
#         ser.write("{},".format().encode().split(','))
#         ser = serial.Serial(connectport, 9600, timeout=0.5)


class Sequence:
    # # port = input("Select port:")
    # ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0.5)
    # # time.sleep(2)
    # # # ser.write('u,v'.encode())
    # # # ser.flush()
    # # # print("Done")
    # ser = serial.Serial('COM6', 9600, timeout=0.5)

    def __init__(self, x_Pos, y_Pos, t_Tap, U_on, u_off):
        # self.reset = reset
        self.x_Pos = x_Pos
        self.y_Pos = y_Pos
        self.t_Tap = t_Tap
        self.U_on = U_on
        self.u_off = u_off

    def __repr__(self):
        return "{},{},{},{},{}".format(self.reset, self.x_Pos, self.y_Pos, self.t_Tap, self.U_on, self.u_off)

    def send_to_port(self):
        """To stream value to arduino"""
        time.sleep(2)
        # ser.write("R".encode())
        ser.flush()
        ser.write("{},{},{},{},{}".format(self.x_Pos, self.y_Pos, self.t_Tap, self.U_on, self.u_off).encode())
        # ser.flush()
        # while (1 == 1):
        #     mydata = ser.readline().lstrip()
        #     print(mydata.decode('utf-8'))
        #     value = str(mydata)

    # @classmethod
    # def send_to_port(cls):
    #     cls.ser = serial.Serial('COM6', 9600, timeout=0.5)
    #     time.sleep(2)
    #     cls.ser.flush()
    #     cls.ser.write("{},{},{},{},{}".format(cls).encode())
    #     cls.ser.flush()

    # def readline(self):
    #     return self.ser.readline()
    # #def bot_action(self):
    #     return "{},{},{}".format(self.x_Pos, self.y_Pos, self.t_Tap)
    def send_position(self):
        """To stream, X Y steps """
        return '{},{}'.format(self.x_Pos, self.y_Pos)

    def reset(self):
        ser.flush()
        return '{}'.format(self.reset)

    @staticmethod
    def checkbot():
        # ser.flush()
        time.sleep(2)
        ser.write("R".encode())
        return getarduinodata()

    @staticmethod
    def presspower():
        time.sleep(2)
        return ser.write("F".encode())

    @staticmethod
    def presspowerhold():
        time.sleep(2)
        return ser.write("Q".encode())


    @staticmethod
    def usbconect():
        time.sleep(2)
        ser.write("U".encode())
        # return ser.write("U".encode())
        return getarduinodata()
    @staticmethod
    def usbeject():
        time.sleep(2)
        return ser.write("u".encode())

    @staticmethod
    def directwrite(loop):
        time.sleep(2)
        # return "{},".format(loop).encode()
        ser.write(format(loop).encode())
        return getarduinodata()

    def direction(self):
        return "{},{},{}".format(self.x_Pos, self.y_Pos, self.t_Tap.encode())


seq1, seq2 = Sequence("X100", "y100", "T", "u", "v"), Sequence("X400", "y100", "T", "u", "v")


# print(seq2.bot_action())


# class BotAction(Sequence):
#     def __init__(self, x_Pos, y_Pos, t_Tap, U_on, u_off, Delay):
#         super().__init__(x_Pos, y_Pos, t_Tap, U_on, u_off)
#         self.Delay = Delay

#
# bot_actn1 = BotAction("X100", "Y100", "T", "U", "v", "S2000")
# Sequence.send_to_port(seq1)
# time.sleep(4)
# Sequence.send_to_port(seq2)

test1 = "F,R,F,S1000,y50,X10,T,X320,T,X65,T,X30,T,x100,y432,T,Y432,x422"
test = "F,S2000,F,T,y50,X10,T"
# for i in test.split(','):
#     time.sleep(2)
#     Sequence.directwrite(i)
# Sequence.directwrite(test)

Sequence.directwrite(test)
print(getarduinodata())