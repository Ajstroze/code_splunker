def splunk_exe(file,size):
    pass

def splunk_elf(file,size):
    pass

def parse_type(file):
    return type

def splunk(file,size):
    type = parse_type(file)
    if type == 'exe':
        splunk_exe(file,size)
    elif type == 'elf':
        splunk_elf(file,size)
    else:
        raise TypeError('File type must be either exe or elf, other fiel types not currently supported')
    
