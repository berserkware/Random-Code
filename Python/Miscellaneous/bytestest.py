class ByteThingy():
    __bytes__ = b'this is a bytes version'

    @staticmethod
    def anAttribute():
        return 'anAttribute'

bt = ByteThingy()

print(bt.anAttribute)

print(bytes(bt))

print(bt.anAttribute)