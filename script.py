#!/usr/bin/env python3
from selenium.webdriver import Firefox, FirefoxOptions, FirefoxProfile

ff_options = FirefoxOptions()
ff_options.headless = True

ff = Firefox(options=ff_options)
ff.quit()
