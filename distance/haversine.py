from math import sin,asin,cos,radians,fabs,sqrt

# def haversine(lonA=float(input("please input lonA： ")), latA=float(input("please input latA： ")),
#               lonB=float(input("please input lonB： ")), latB=float(input("please input latB： "))):
#     """
#     Caculate the great circle distance between two points
#     on the earth
#     :param lonA: A longtitude
#     :param latA: A lattitude
#     :param lonB: B longtitude
#     :param latB: B lattitude
#     :return:  distance between two ponts
#     """
#     # 将十进制转换为弧度
#     lonA, latA, lonB, latB = map(radians, [lonA, latA, lonB, latB])
#
#     # haversine公式
#     dlon = lonB - lonA
#     dlat = latB - latA
#     a = sin(dlat/2)**2 + cos(latA) * cos(latB) * sin(dlon/2)**2
#     c = 2 * asin(sqrt(a))
#     r = 6371 # 地球半径，单位km
#     d = c * r * 1000
#     return d


def high(a, b, c):
    """
    求三角形的高度
    :param a: 边
    :param b: 底
    :param c: 边
    :return: 高度
    """

    # 根据海伦公式求高
    P = (a + b + c) / 2
    S = sqrt(P * (P - a) * (P - b) * (P - c))
    print("S",S)
    h = 2 * S / b
    if h is None:
        print("error")
# print("计算a边")
# a = haversine()
# print("计算b边")
# b = haversine()
# print("计算c边")
# c = haversine()
print(high(5, 6, 7))