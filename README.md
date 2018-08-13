# ChromeDriver Tests

## Prerequisites

* Requires Samsung Internet v8.x which is pre-release at the time of writing.
* Requires ChromeDriver v2.36. [Try the download link here](https://chromedriver.storage.googleapis.com/index.html?path=2.36/).
* Connect the Android device over USB and ensure that USB debugging is enabled.
* Check that `adb devices` lists the device.
* Ensure that ChromeDriver is in your path (and that it resolves to the v2.36 binary): `chromedriver --version`.

## Running the tests

```
python samsung-internet-8-basic-test.py
```
