from setuptools import setup, find_packages

setup(
    name='trinetraservices',
    version='0.1',
    author='Ishwor Subedi',
    author_email='ishworr.subedi@gmail.com',
    description='A brief description of your package',
    long_description=open('alpr/README.md').read(),
    url='https://github.com/ishworrsubedii/anpr_speed-estimation_violation-detection',
    packages=find_packages(),
    package_data={
        'servicess.alpr': [
            'src/**/*',
            'usage/**/*',
            'README.md',
        ],
        'servicess.speed': [
            'src/**/*',
            'usage/**/*',
            'README.md',
        ],
        'servicess.trafficlight': [
            'src/**/*',
            'usages/**/*',
            'README.md',
        ],

    },
)
