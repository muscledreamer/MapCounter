# -*- coding: utf-8 -*-
# @Email: jqian_bo@163.com
# @Author: JingQian Bo
# @Create Time: 2019/11/19-3:35 PM

import requests

with open("bj.txt", "r") as f:
    data = f.read()

_point_list = [tuple(i.split(",")) for i in data.split(";")]

point_list = []
data = data.split(";")
for i in range(len(data)):
    _tuple = tuple(float(_) for _ in data[i].split(","))
    point_list.append(_tuple)
print(point_list)

# api = "http://api.map.baidu.com/place/v2/search?query=天安门&region=北京&output=json&ak=DzeLvY1PsV9Gs6Dft0xbXh7rhfH6Qum4&page_num=1"
# r = requests.get(api).json()
mid_lat = 39.916537  # 纬度
mid_lng = 116.403784  # 经度

# cos纬度=0.26
add_lat = 1 * 1 / 111 * 0.26  # 纬度
add_lng = 1 * 1 / 111  # 经度


# 矩形测量
def jx():
    min_lat_range = 39.26
    max_lat_range = 41.03
    min_lng_range = 115.25
    max_lng_range = 117.30

    add_lat_lng = add_lat * add_lng

    total_range = (max_lat_range - min_lat_range) * (max_lng_range - min_lng_range)

    count = total_range / add_lat_lng
    return count





print(count)
