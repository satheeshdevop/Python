d1 = { 'a' : 10, 'b' : 20}
d2 = { 'c' : 40, 'd' : 50 }

# update () method
d1.update(d2)

# dictionary unpacking 
md = {**d1, **d2}

print(f" Merging two dictionaries using update method               : {d1}")
print(f" Merging two dictionaries using dictionary unpacking method : {md}")