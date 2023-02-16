from setuptools import setup, find_packages

setup(name='Eu4ng-test',  # 패키지 명
      version='0.1.0',
      description='Open API wrapper library for Korean financial organizations',
      author='Hyunuck Kim',
      author_email='gusdnr@gmail.com',
      url='https://github.com/hyunuck',
      license='BSD License',
      python_requires='>=3',
      install_requires=[
          "httpx==^0.23.3"
      ],
      )
