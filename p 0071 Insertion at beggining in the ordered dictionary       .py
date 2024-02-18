from collections import OrderedDict
satheesh = OrderedDict([('s', 3), ('t', 6), ('v', 9)])
tech     = ('p', 1)
dev      = OrderedDict([tech])
dev.update(satheesh)

print(f" Updated Ordered Dictionary :{dev}")