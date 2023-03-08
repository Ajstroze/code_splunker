from setuptools import setup, find_packages

setup(
    name ='Code-Splunker',
    version ='1.0.0',
    description ='Search for code caves in a binary',
    long_description = long_description,
    url = 'https://github.com/Ajstroze/Code-Splunker',
    author = 'Ajstroze',
    author_email = "ajstroze@gmail.com",
    license = 'GNU General Public License v3 or later (GPLv3+)',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: System',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2.7',
    ],

    keywords = 'Codecave',

    packages = find_packages(exclude=['contrib','docs','tests']),

    install_requires=[],

    extras_require={},

    entry_points={
        'console_scripts': [
            'code-splunker=code-splunker.main:main',
      ],
    },
)
