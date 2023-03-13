from setuptools import setup

install_requires = ['pefile','pyelftools']

setup(
    name ='code_splunker',
    version ='1.0.0',
    description ='Search for code caves in a binary',
    url = 'https://github.com/Ajstroze/code_splunker',
    author = 'Ajstroze',
    author_email = "ajstroze@gmail.com",
    packages = ['code_splunker'],
    install_requires = install_requires,
    license = 'GNU General Public License v3 or later (GPLv3+)',

    classifiers=[
        'Development Status :: 1',
        'Intended Audience :: Developers,reverse engineers, malware analysts, CTF competers',
        'Topic :: System',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.11.2',
    ],

    keywords = 'Codecave',

    entry_points={
        'console_scripts': [
            'code_splunker=code_splunker.main:main',
        ],
    },
)
