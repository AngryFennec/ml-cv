# -*- coding: utf-8 -*-
from setuptools import setup

packages = ["yolo_demo", "yolo_demo.core"]

package_data = {
    "": ["*"],
    "yolo_demo": [
        "data/*",
        "core/*",
        "data/classes/*",
        "data/classes/voc.names",
        "saved_model/*",
    ],
}

install_requires = [
    "Pillow>=9.0.1,<10.0.0",
    "easydict>=1.9,<2.0",
    "numpy>=1.22.3,<2.0.0",
    "opencv-python>=4.5.5,<5.0.0",
    "tensorflow==2.8.0",
]

entry_points = {
    "console_scripts": [
        "yolo_demo=yolo_demo.demo:start",
    ]
}

setup_kwargs = {
    "name": "yolo_demo",
    "version": "0.12.0",
    "description": "",
    "long_description": None,
    "author": "Angry Fennec",
    "author_email": "shellfix@gmail.com",
    "maintainer": None,
    "maintainer_email": None,
    "url": None,
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "python_requires": ">=3.9,<3.11",
    "entry_points": entry_points,
}


setup(**setup_kwargs)
