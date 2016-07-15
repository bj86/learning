from sys import argv
from os.path import exists
import uuid

script, from_file = argv

unique_filename = uuid.uuid4()

copyfrom = open(from_file)
data = copyfrom.read
out_file = open(unique_filename)
out_file.write(data)

copyto.close()
copyfrom.close()
