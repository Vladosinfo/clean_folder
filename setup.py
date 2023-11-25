from setuptools import setup

setup(name='cleat-folder',
      version='1.0.0',
      description='Structure and reorganize the order in the repository',
      url='https://github.com/Vladosinfo/clean_folder',
      author='Vladyslav',
      author_email='vladosinfo@gmail.com',
      license='MIT',
      entry_points={'clean-folder': ['helloworld = clean_folder.clean:main']}
)