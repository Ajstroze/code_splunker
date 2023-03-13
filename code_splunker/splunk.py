from code_splunker.cave import Cave
import pefile
from elftools.elf.elffile import ELFFile

# Iterate through the exe, locate each code cave and create an object for each cave
def splunk_exe(file,size):
    pe = pefile.PE(file)
    if pe.OPTIONAL_HEADER.DllCharacteristics & pe.OPTIONAL_HEADER.IMAGE_DLLCHARACTERISTICS_DYNAMIC_BASE:
        print("[*] ASLR is enabled, virtual address may vary in run time")
    print(f"[*] Splunking for code cave with at least {size} bytes")
    image_base = pe.OPTIONAL_HEADER.ImageBase
    for section in pe.sections:
        pos = 0
        count = 0
        data = section.get_data()
        for byte in data:
            pos += 1
            if byte == 0x00:
                count += 1
            else:
                if count > size:
                    cave = Cave()
                    cave.section = section.Name.decode()
                    cave.cave_size = count
                    cave.cave_begin = hex(image_base + section.VirtualAddress + pos - count - 1)
                    cave.cave_end = hex(image_base + section.VirtualAddress + pos - 1)
                    cave.vaddress = hex(section.VirtualAddress)
                    section_flags = section.Characteristics
                    # Get the sections permissions
                    if section_flags &  0x40000000:
                        cave.permissions += "READ "
                    elif section_flags & 0x80000000:
                        cave.permissions += "WRITE "
                    elif section_flags & 0x20000000:
                        cave.permissions += "EXECUTE"
                    else:
                        cave.permissions = "NONE"
                    print('[*] A cave has been found!')
                    print(cave)
                    print("   ")
                    count = 0
                else:
                    count = 0

# Iterate through the elf file and create an object for each code cave
def splunk_elf(file,size):
    with open(file,'rb') as f:
        elf = ELFFILE(f)
    if elf.header.e_type == 'ET_DYN':
        print("[*] ASLR is enabled, virtual address may vary in run time")
    print(f"[*] Splunking for code cave with at least {size} bytes")
    for section in elf.iter_sections():
        pos = 0
        count = 0
        data = section.data()
        for byte in data:
            pos += 1
            if byte == 0x00:
                count += 1
            else:
                if count > size:
                    cave = Cave()
                    cave.section = section.name.decode()
                    cave.cave_size = count
                    cave.cave_begin = hex(section.header.sh_addr + pos - count - 1)
                    cave.cave_end = hex(section.header.sh_addr + pos - 1)
                    cave.vaddress = hex(section.header.sh_addr)
                    section_flags = section.header.sh_flags
                    # Get the sections permissions
                    if section_flags & 0x01:
                        cave.permissions += "WRITE "
                    if section_flags & 0x02:
                        cave.permissions += "ALLOC "
                    if section_flags & 0x04:
                        cave.permissions += "EXECUTE"
                    if section_flags == 0:
                        cave.permissions = "NONE"
                    print('[*] A cave has been found!')
                    print(cave)
                    print("   ")
                    count = 0
                else:
                    count = 0

# Parse tge file type and begin the codecave search process
def splunk(file,size):
    type = file[-3:]
    if type == "exe":
        splunk_exe(file,size)
    elif type == 'elf':
        splunk_elf(file,size)
    else:
        raise TypeError('File type must be either exe or elf, other file types not currently supported')
