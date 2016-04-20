'''
Created on 2016. 4. 19.

@author: David
'''
from PIL import Image
from PIL.ExifTags import TAGS
import os
from os.path import abspath
from werkzeug import secure_filename

target_dir = os.path.normpath('C:/Users/David/git/Python_Project/Flask_Application/static/uploads')
#print target_dir

path = '/'.join(abspath("static/uploads").split('\\'))

for f in os.listdir('./static/uploads'):
    if f.endswith(('.JPG', 'jpg')):
        print f
        
        i = Image.open(target_dir+'\\' +f)
        
        exif = dict((TAGS[k], v) for k, v in i._getexif().items() if k in TAGS)
        
        if exif['Orientation'] != 1:
            i = i.rotate(90, expand=True)

        i.thumbnail((1000,1000), Image.ANTIALIAS)
        
        fn, text = os.path.splitext(f) # tuple
        
        destiny = os.path.normpath(path+'/png')
        print os.path.isdir(destiny)
         
        if os.path.isdir(destiny):
            i.save(destiny + '/{}.png'.format(fn))
        else:
            os.makedirs(destiny)
            i.save(destiny + '/{}.png'.format(fn))