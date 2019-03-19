from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    long_desc = f.read()

setup(
    name='py-telegram-bot',
    version='0.2.post2',
    description='Telegram Bots API wrapper.',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    url='https://vk.com/nix13',
    author='Nix13',
    author_email='nix1304@gmail.com',
    install_requires=['requests', 'pysocks'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
