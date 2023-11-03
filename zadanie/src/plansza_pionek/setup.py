from setuptools import find_packages, setup

package_name = 'plansza_pionek'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dodo',
    maintainer_email='dominikkorwek@interia.pl',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "plansza_pionek =plansza_pionek.plansza_i_pionek:main",
            "ruch = plansza_pionek.ruch:main"
        ],
    },
)
