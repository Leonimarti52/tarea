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
    maintainer_email='leoni@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'nodo1 = eje2.nodo1:main',
            'nodo2 = eje2.nodo2:main',
            'sub = eje2.sub:main',
        ],
    },
)
