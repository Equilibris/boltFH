import BoltFH
import os
fileSys1 = BoltFH.FS(os.getcwd())

# os.chdir()

bfs = BoltFH.FS()

print(bfs.JSONFormating)

bfs.log(r'you\'re json here')

