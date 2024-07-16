import board
import time
import sqlite3
import sys

import adafruit_dht


def main():
    db_file = sys.argv[1]
    location = sys.argv[2]
    print(db_file)
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    insert_stmt = "insert into temperature(temperature, humdity, location) values(?, ?, ?);"

    dhtDevice = adafruit_dht.DHT22(board.D27)
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity

        cur.execute(insert_stmt, (temperature_f, humidity, location))

        print(f"{temperature_f} F Humidity {humidity}%")
        con.commit()
    finally:
        dhtDevice.exit()


if __name__ == '__main__':
    rc = main()
    sys.exit(rc)
