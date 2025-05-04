"""Third part/option of the assignment.

Communication line using UART interface
User can choose from 3 modes
- Transmitter - transmits data entered via console
- Node - receives data on one interface and sends it out through second
- Receiver - prints received data to the console
"""
from machine import UART, Pin
from cyprich_uloha2.utils import decider


class Communicator:
    """Manages the communication."""

    def __init__(self):
        """Create instance of the class."""
        mode: int = decider(
            "Choose mode in which you want to operate",
            "Transmitter",
            "Node",
            "Receiver")
        functions = [self.transmitter, self.node, self.receiver]
        functions[mode - 1]()

    @staticmethod
    def transmitter():
        """Transmit data entered via console."""
        uart = UART(1, tx=Pin(4), rx=Pin(5))
        while True:
            try:
                user = input("Write your message [ctrl+c for exit]: ")
                uart.write(bytes(user, "UTF-8"))
            except KeyboardInterrupt:
                break

    @staticmethod
    def node():
        """Receive data on one interface and send it to other."""
        uart1 = UART(1, tx=Pin(4), rx=Pin(5))
        uart2 = UART(2, tx=Pin(6), rx=Pin(7))

        print("\t[Press ctrl+c to exit]")
        while True:
            try:
                recv = uart1.readline()
                if recv:
                    uart2.write(bytes(recv.decode(), "UTF-8"))
            except KeyboardInterrupt:
                break

    @staticmethod
    def receiver():
        """Print received data."""
        uart = UART(1, tx=Pin(4), rx=Pin(5))
        print("\t[Press ctrl+c to exit]")
        while True:
            try:
                recv = uart.readline()
                if recv:
                    print(recv.decode())
            except KeyboardInterrupt:
                break


def main():
    """Run the third part of the assigment."""
    Communicator()


if __name__ == '__main__':
    main()
