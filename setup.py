from setuptools import setup, find_namespace_packages

setup(name='clean-folder', 
      version='1.0.0',
      description='Structure and reorganize the order in the repository',
      url='https://github.com/Vladosinfo/clean_folder',
      author='Vladyslav',
      author_email='vladosinfo@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
      )