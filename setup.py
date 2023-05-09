from distutils.core import setup
import os

setup(
        name = 'HikNetExtractor',
        version = '1.0.10',
        license = 'GNU General Public License v3 (GPLv3)',
        url = 'https://github.com/surfzoid/HikNetExtractor',
        description = 'Provides functionality to extract periodically record event from Hikvion camera or NVR.',
        long_description = 'Provides functionality to extract periodically record event from Hikvion camera or NVR with ISAPI and HTTPDigestAuth enable. Add this script to an schedule task and you will keep records during the number of day you put in the config.',
        platforms = ['Linux, Windows, Mac'],
        author = 'Surfzoid',
        author_email = 'surfzoid@gmail.com',
        maintainer = 'Surfzoid',
        maintainer_email = 'surfzoid@gmail.com',
        )
