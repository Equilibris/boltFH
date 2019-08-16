from threading import Thread
from random import randint
import json
import os
from hashlib import md5

class FS():

    @staticmethod
    def copy(FSObj1, FSObj2): pass

    def __init__(self, path=os.getcwd()):
        def recersiveTreverse(path=os.getcwd(),count = 2):
            ISD = {
                'files' : [],
                'folders' : [],
                'temp' : {}
            } # ISD stands for internal scope dict

            os.chdir(path)
            for i in os.listdir():
                try:
                    os.chdir(path+'\\'+i)
                    ISD['folders'].append(os.getcwd())
                    os.chdir(path)
                except Exception as e:
                    ISD['files'].append(File(os.getcwd(),i))
                    # ISD['files'].append(i)

            for folder in ISD['folders']:
                ISD['temp'][folder]=recersiveTreverse(folder)
            ISD['folders']=[]

            ISD['folders'] = ISD['temp']
            ISD.pop('temp')

            return(ISD)

        if path != None:
            self.fileSystem = recersiveTreverse(path=path)
        
        else:
            self.fileSystem = {}

    @property
    def JSONFormating(self):
        def recersiveTreverse(dictObj):
            ISD = {
                'files' : [],
                'folders' : {}
            } # ISD stands for internal scope dict

            for key,value in dictObj.items():
                if key == 'files':
                    for i in value:
                        ISD['files'].append(str(i))

                else:
                    for deepKey,deepValue in value.items():
                        ISD['folders'][deepKey] = recersiveTreverse(deepValue)

                # try:
                #     os.chdir(path+'\\'+i)
                #     ISD['folders'].append(os.getcwd())
                #     os.chdir(path)
                # except Exception as e:
                #     ISD['files'].append(File(os.getcwd(),i))
                #     # ISD['files'].append(i)

            # for folder in ISD['folders']:
            #     ISD['temp'][folder]=recersiveTreverse(folder)
            # ISD['folders']=[]

            # ISD['folders'] = ISD['temp']
            # ISD.pop('temp')

            return(ISD)

        # return recersiveTreverse(self.fileSystem)

        return (json.dumps(recersiveTreverse(self.fileSystem), indent=4))

    def __str__(self):
        return self.JSONFormating

    def log(self, fName):
        with open(fName,'w') as f:
            f.write(str(self.JSONFormating))


class File():
    @classmethod
    def xpbc(cls, fileObj1, fileObj2, x=3, repetisions=5): # xpbc stands for x point based comparason
        
        minVar = min(len(fileObj1),len(fileObj2))

        fC1 = fileObj1.contents[::(x%minVar-2)+1]
        fC2 = fileObj2.contents[::(x%minVar-2)+1]

        if fC1 == fC2:
            if repetisions > 0:
                if cls.xpbc(fileObj1, fileObj2, x=randint(3, minVar//3),repetisions=repetisions-1):
                    return True

                else:
                    return False

            else:
                return True

        else:
            return False

    @classmethod
    def lnbc(cls, fileObj1, fileObj2):  # lnbc stands for lenght based comparason
        if len(fileObj1) == len(fileObj2):
            return True

        else:
            return False

    @classmethod
    def szbc(cls, fileObj1, fileObj2):  # szbc stands for size based comparason
        if fileObj1.size == fileObj2.size:
            return True

        else:
            return False

    @classmethod
    def habc(cls, fileObj1, fileObj2):  # habc stands for hash based comparason
        if fileObj1.hash == fileObj2.hash:
            return True

        else:
            return False

    def __init__(self,path, name):
        self.name = name
        self.path = path
        self.size = os.stat(path).st_size 

    def __len__(self):
        return len(self.contents)

    __int__ = __len__

    def __repr__(self):
        return f'{self.__class__.__qualname__}({self.path},{self.name})'

    @property
    def contents(self):
        return open(self.path,'r').read()

    @property
    def hash(self):
        return md5(self.contents.encode()).hexdigest()