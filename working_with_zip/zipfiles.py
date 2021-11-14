import zipfile
import zlib
with open('archive.zip') as workfile:
    print(zipfile.is_zipfile(workfile))


with zipfile.ZipFile('newarchive.zip', 'w') as workfile:
    workfile.write('sometext.txt', compress_type=zipfile.ZIP_DEFLATED, compresslevel=5)
    workfile.write('somefile', compress_type=zipfile.ZIP_DEFLATED, compresslevel=5)
    workfile.write('anotherfile', compress_type=zipfile.ZIP_DEFLATED, compresslevel=5)
    files = workfile.namelist()
    print(files)
    for file in files:
        print(workfile.read(name=file))
        workfile.extract(file, 'extracted')
