from setuptools import setup

setup(name='capitain_corpus_reader',
      version='0.1',
      description='A Python-NLTK-like corpus reader for XML texts that comply with the CapiTainS guidelines',
      url='',
      author='Francesco Mambrini',
      author_email='',
      license='CC BY SA',
      packages=['capitain_corpus_reader'],
      install_requires=[
          'nltk',
          'MyCapytain'
      ],
      include_package_data=True,
      tests_require=["pytest"],
      zip_safe=False)
