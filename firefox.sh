#!/bin/bash

export GECKO_DRIVER_VERSION='v0.24.0'
wget https://github.com/mozilla/geckodriver/releases/download/$GECKO_DRIVER_VERSION/geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz
tar -xvzf geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz
rm geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz
chmod +x geckodriver
sudo cp geckodriver /usr/local/bin/

cat <<EOF > script.py
#!/usr/bin/env python3
from selenium.webdriver import Firefox, FirefoxOptions, FirefoxProfile

ff_options = FirefoxOptions()
ff_options.headless = True

ff = Firefox(options=ff_options)
ff.quit()
EOF
chmod +x script.py