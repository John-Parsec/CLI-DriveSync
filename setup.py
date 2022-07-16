from setuptools import setup
setup(
    name = 'cli-drivesync',
    version = '0.1.0',
    description='CLI em python para sincronização de pastas locais com o Google Driver',
    author='João "John Parsec" Manoel',
    license='MIT',
    install_requires=[
        'icecream'
    ],
    entry_points = {
        'console_scripts': [
            'ds = src.__main__:main'
        ]
    })