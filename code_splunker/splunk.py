import code_splunker.cave
import pefile

def splunk_exe(file,size):
    pass

def splunk_elf(file,size):
    pass

# def parse_type(file):
#     type = file[-4:]
#     return type

def splunk(file,size):
    type = file[-3:]
    if type == 'exe':
        splunk_exe(file,size)
    elif type == 'elf':
        splunk_elf(file,size)
    else:
        raise TypeError('File type must be either exe or elf, other fiel types not currently supported')
