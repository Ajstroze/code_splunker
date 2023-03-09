from code_splunker.cave import Cave
import pefile

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
                    #TODO: Verify correct permissions
                    if section_flags & section.IMAGE_SCN_MEM_READ:
                        cave.permissions = 'READ'
                    else:
                        cave.permissions = "WRITE"
                    print('[*] A cave has been found!')
                    print(cave)
                    print("   ")
                    count = 0
                else:
                    count = 0


def splunk_elf(file,size):
    pass

def splunk(file,size):
    type = file[-3:]
    if type == "exe":
        splunk_exe(file,size)
    elif type == 'elf':
        splunk_elf(file,size)
    else:
        raise TypeError('File type must be either exe or elf, other file types not currently supported')
