import setuptools

setuptools.setup(
    name='protvr',
    packages=setuptools.find_packages('protvr'),
    install_requires=[
        'flask',
    ],
    entry_points={
        'console_scripts': [
            'launch = protvr.launch:launch',
        ],
    },
)
