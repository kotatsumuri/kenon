import requests
import os
url_ok = "https://maker.ifttt.com/trigger/Temperatur_ok/with/key/" + os.environ["IFTTT_KEY"]
url_ng = "https://maker.ifttt.com/trigger/Temperatur_ng/with/key/" + os.environ["IFTTT_KEY"]


def ifttt_ok(temperatur):
    payload = {"value1": str(temperatur)}
    response = requests.post(url_ok, data=payload)
    print(response)


def ifttt_ng():
    response = requests.post(url_ng)
    print(response)


if __name__ == "__main__":
    ifttt_ok(36.1)
    ifttt_ng()

