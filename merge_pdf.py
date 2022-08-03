import os
import sys
import re
from PyPDF2 import PdfFileMerger
directory = os.getcwd().replace('\\', '/')
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)
source_dir = (directory+ "/")
# print("dlkg"+source_dir)
new = sorted_alphanumeric(os.listdir(source_dir))
merger = PdfFileMerger()
new

for item in new:
    if item.endswith('pdf'):
        print(item)
        merger.append(source_dir + item)

merger.write(source_dir + 'finish.pdf')       
merger.close()

print (" Done Nhe")