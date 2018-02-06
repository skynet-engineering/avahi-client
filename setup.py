import setuptools


setuptools.setup(
    name='avahi-client',
    packages=['avahi'],
    version='1.0.2',
    description='Library for service publication and discovery using Avahi',
    author='Kevin Lin',
    author_email='kevin@skynet.engineering',
    url='https://code.skynet.engineering/diffusion/AVAHI',
    install_requires=[
        'netifaces==0.10.6',
    ],
    keywords=[],
    classifiers=[],
)
