import os

import sklearn

sklearn_version = sklearn.__version__

print(sklearn_version)
print('==================================')

for s in os.environ['PATH'].split(';'):
    print(s)

print('==================================')

for s in os.environ['PATH'].split(';'):
    print(s)
