class Cave:
    def __init__ (self):
        self.section = ''
        self.cave_begin = 0
        self.cave_end = 0
        self.vaddress = 0
        self.permissions = None

    def __str__(self):
        return '\n'.join(['Section name:             {name}',
                          'Cave begin:               {cave_begin}',
                          'Cave end:                 {cave_end}',
                          'Virtual address:          {vaddress}',
                          'Section permissions:      {permissions}']).format(**self.__dict__)
