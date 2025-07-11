import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D4)

while True:
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity

        print(f"Temp: {temperature_c:.1f}°C  Humidity: {humidity:.1f}%")

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(3.0)
