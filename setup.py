from setuptools import setup

setup(name='package.testing',
      entry_points={
          'console_scripts': [
              'run-tests = project.scripts:runtests',
              'run-suite = project.scripts:runsuite'
          ]
      },
      install_requires=['nose'],
      packages=['project']
)
