"""
Watch SFTP and do stuff to a dir of files once it no longer has them open
"""
from setuptools import find_packages, setup

dependencies = ['click', 'psutil', 'pathlib', 'colorama']

setup(
    name='sftpwatcher',
    version='0.1.0',
    url='https://github.com/mykelalvis/sftp-watcher',
    license='BSD',
    author='Mykel Alvis',
    author_email='mykel.alvis@gmail.com',
    description='Watch SFTP and do stuff to a dir of files once it no longer has them open',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'sftpwatcher = sftpwatcher.cli:main',
            's3mover = s3mover.cli:main',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Operators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
