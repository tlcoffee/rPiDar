from setuptools import setup

setup(
    name='rPiDar',
    version='0.0.1',
    url='https://github.com/tlcoffee/rpidar',
    author='Travis Northrup',
    author_email='travis.northrup@pm.me',
    packages=['openpylivox'],
    description='Python Controller for Lidar Sensor on RaspberryPi',
    install_requires=['numpy >= 1.15.4', 'crcmod >= 1.7.0'],
    python_requires='>=3.5',
)
