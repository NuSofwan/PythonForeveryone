from decimal import Decimal
def land(width,long,price=999888):
    cal=width*long
    cal_wa=cal/4
    print('ที่ดินผืนนี้กว้าง: {} เมตร  ยาว: {}  เมตร'.format(width,long))
    print('ที่ดินผืนนี้มีพื้นที่: {} ตารางเมตร'.format(cal))
    print('ที่ดินผืนนี้มีพื้นที่: {} ตารางวา'.format(cal_wa))
    calprice = cal_wa * price
    return 'ที่ดินผืนนี้ราคา: {:,} บาท'.format(calprice)
res=land(5,15)
print(res)


