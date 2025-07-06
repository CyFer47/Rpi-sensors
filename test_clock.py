import time
import board
import busio
import adafruit_ds3231

# Setup I2C and RTC
i2c = busio.I2C(board.SCL, board.SDA)
rtc = adafruit_ds3231.DS3231(i2c)

try:
    while True:
        now = rtc.datetime
        print("RTC Time: {:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
            now.tm_year, now.tm_mon, now.tm_mday,
            now.tm_hour, now.tm_min, now.tm_sec
        ))
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped.")
