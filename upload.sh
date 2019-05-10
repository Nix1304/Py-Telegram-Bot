#!/usr/bin/env bash
rm -Rf build
rm -Rf dist
rm -Rf py_telegram_bot.egg-info

python3 setup.py sdist bdist_wheel
twine upload dist/*