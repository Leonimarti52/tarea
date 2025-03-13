from setuptools import find_packages, setup

package_name = 'eje2'

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
    maintainer='leoni',
    maintainer_email='leonimarti52@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pub1 = eje2.pub1:main',
            'pub2 = eje2.pub2:main',
            'pub3 = eje2.pub3:main',
            'sub_pub = eje2.sub_pub:main',
            'sub = eje2.sub:main',
        ],
    },
)
