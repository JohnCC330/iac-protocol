from setuptools import setup, find_packages

setup(
    name='iac-protocol',
    version='0.1',
    license='BSD',
    author='Risto Stevcev',
    author_email='risto1@gmail.com',
    url='https://github.com/Risto-Stevcev/iac-protocol',
    long_description=open("README.rst","r").read(),
    packages=find_packages(),
    description="An protocol/interface that enables inter-application communication and scripting.",
    classifiers=[
        'Development Status :: 4 - Beta', 
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Home Automation',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)',
        'Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator',
        'Topic :: Software Development :: Interpreters',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Utilities',
        ], 
)
