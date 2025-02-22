from setuptools import setup, find_packages

setup(
    name="webgen",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pynput",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "webgen=webgen:main",
        ],
    },
)
