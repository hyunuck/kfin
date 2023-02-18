from setuptools import setup, find_packages

setup(name='kfin',
      version='0.0.3',
      description='Open API wrapper library for Korea financial organizations',
      author='Hyunuck Kim',
      author_email='gusdnr@gmail.com',
      url='https://github.com/hyunuck/kfin',
      license='MIT License',
      python_requires='>=3',
      packages=find_packages(exclude=['docs', 'tests*']),
      install_requires=[
          "httpx==0.23.3"
      ],
      )
