from setuptools import setup
setup(name='fightcadechat',
      version='0.9',
      description='Fightcade chatbot for fcreplay python code',
      url='http://github.com/glisignoli/fightcadechat',
      author='Gino Lisignoli',
      author_email='glisignoli@gmail.com',
      license='GPL3',
      packages=['fightcadechat'],
      entry_points = {
          'console_scripts': [
              'fightcadechat=fightcadechat.main:main',
          ]
      },
      install_requires = [
          'fcreplay'
      ],
      zip_safe=False)