from setuptools import setup

setup(
    name='jarbas_utils',
    version='0.6.5',
    packages=['jarbas_utils',
              'jarbas_utils.sound',
              'jarbas_utils.mark1',
              'jarbas_utils.skills',
              'jarbas_utils.lang'],
    url='https://github.com/OpenJarbas/jarbas_utils',
    install_requires=["pronouncing",
                      "googletrans",
                      "mycroft-messagebus-client",
                      "inflection",
                      "colour", "pexpect"],
    license='Apache',
    author='jarbasAI',
    author_email='jarbasai@mailfence.com',
    description='collection of simple utilities for use across the mycroft ecosystem'
)
