from setuptools import setup

setup(
    name='jarbas_utils',
    version='0.5.2',
    packages=['jarbas_utils',
              'jarbas_utils.sound',
              'jarbas_utils.mark1',
              'jarbas_utils.skills',
              'jarbas_utils.lang'],
    url='https://github.com/OpenJarbas/jarbas_utils',
    install_requires=["pronouncing",
                      "googletrans",
                      "pyalsaaudio==0.8.2",
                      "mycroft-messagebus-client",
                      "colour",
                      "timezonefinder>=4.2.0",
                      "geopy>=1.21.0",
                      "geocoder>=1.38.1"],
    license='MIT',
    author='jarbasAI',
    author_email='jarbasai@mailfence.com',
    description='collection of simple utilities for use across the mycroft ecosystem'
)
