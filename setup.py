setup(
        name='project2',
        version='1.0',
        author='Tolulope Okeowo',
        authour_email='tookeowo@ou.edu',
        packages=find_packages(exclude=('tests', 'docs')),
        setup_requires=['pytest-runner'],
        tests_require=['pytest']
)
