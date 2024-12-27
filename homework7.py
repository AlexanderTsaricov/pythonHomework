import shutil
import zipfile
from pathlib import Path
from zipfile import ZipFile
import datetime


def renameFiles (catalog, filesExtension, numb_digits, newName='', numletters=[0,3]):
    catalogObj = Path(catalog)
    if (catalogObj.is_dir()):
        listFilesInCatalog = []
        for file in catalogObj.iterdir():
            listFilesInCatalog.append(file)
        print(listFilesInCatalog)
        renameListFiles = []
        for file in listFilesInCatalog:
            extensionList = file.name.split('.')
            extension = ''
            if len(extensionList) > 1:
                extension = extensionList[1]
            if (extension == filesExtension):
                renameListFiles.append(file)
        numbersForName = 10 ** (numb_digits - 1)
        for file in renameListFiles:
            partFileName = file.name[numletters[0]:numletters[1]]
            file.rename(f'{catalog}/{partFileName}{newName}_{numbersForName}.{filesExtension}')
            numbersForName+=1

def makeArchiveCatalog (catalog, pathArchive):
    catalogObj = Path(catalog)
    Path.mkdir(pathArchive)
    if (catalogObj.is_dir()):
        for file in catalogObj.iterdir():
            with ZipFile(f'{pathArchive}/{catalog}.zip', 'a') as myzip:
                myzip.write(f'{catalog}/{file.name}')

def deleteOldFile(catalog, countDays):
    catalogObj = Path(catalog)
    today = datetime.datetime.today()
    if (catalogObj.is_dir()):
        for file in catalogObj.iterdir():
            timeMake = file.stat().st_mtime
            readable_time = datetime.datetime.fromtimestamp(timeMake)
            if ((today - readable_time).days >= countDays):
                if (file.is_dir()):
                    shutil.rmtree(f'{catalog}/{file.name}')
                file.unlink()

def findFilesByExtension(catalog, extension):
    catalogObj = Path(catalog)
    if (catalogObj.is_dir()):
        for file in catalogObj.iterdir():
            if file.is_dir():
                findFilesByExtension(f'{catalog}/{file.name}', extension)
            fileName = file.name
            if (len(fileName.split('.'))>1):
                if(fileName.split('.')[1] == extension):
                    print(fileName)

findFilesByExtension('testDir', 'txt')