Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
cars = ['toyota','honda','benz']
cars.append('byd')
print(cars)
['toyota', 'honda', 'benz', 'byd']
cars.remove('honda')
print(cars)
['toyota', 'benz', 'byd']
cars.insert(0,'tesla')
print(cars)
['tesla', 'toyota', 'benz', 'byd']
print(cars[0])
tesla
print(cars[1])
toyota
for c in cars:
    print(c)

    
tesla
toyota
benz
byd

print(*cars)
tesla toyota benz byd
for i,c in enumerate(cars):
    print(i,c)
... 
...     
0 tesla
1 toyota
2 benz
3 byd
>>> for i,c in enumerate(cars):
...     print(i+1,c)
... 
...     
1 tesla
2 toyota
3 benz
4 byd
>>> for i,c in enumerate(cars, start=0):
...     print('ลำดับ {} {}'.format(i,c))
... 
...     
ลำดับ 0 tesla
ลำดับ 1 toyota
ลำดับ 2 benz
ลำดับ 3 byd
>>> for i,c in enumerate(cars, start=1):
...     print('ลำดับ {} {}'.format(i,c))
... 
...     
ลำดับ 1 tesla
ลำดับ 2 toyota
ลำดับ 3 benz
ลำดับ 4 byd
>>> 
>>> cars[1]='isuzu'
>>> print(cars)
['tesla', 'isuzu', 'benz', 'byd']
>>> del cars[0]
>>> print(cars)
['isuzu', 'benz', 'byd']
>>> len(cars)
3

ord('A')
ord('ก')
