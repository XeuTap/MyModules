import sys
from mypkg.mymod import test
test('myclient.py')
print(sys.__dict__)
import mypkg.mymod as mod
mod.test('myclient.py')
print(sys.__dict__)