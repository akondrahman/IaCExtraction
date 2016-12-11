'''
Akond, Dec 11, 2016, holder for dicts
'''

excludeDictForWikimedia = {  '/Users/akond/PUPP_REPOS/wikimedia-downloads/puppet':  [16, 18, 19, 6, 10, 15, 14, 1, 17],
                    '/Users/akond/PUPP_REPOS/wikimedia-downloads/vagrant':  [21, 17, 183, 15, 143, 135, 267, 141, 168, 265, 159, 130, 10, 278, 173, 280, 181, 176, 140, 275, 124, 154, 240, 151, 190, 261, 264, 251, 121, 266, 239,
                                                                             161, 274, 284, 248, 269, 114, 268, 136, 259, 137, 182, 26, 289, 11, 107, 13, 153, 118, 241, 252, 288, 152, 155, 286, 191, 254, 116, 122, 101, 217, 120,
                                                                             169, 250, 258, 25, 123, 262, 253, 110, 157, 247, 171, 184, 270, 27, 260, 139, 142, 188, 119, 103, 256, 177, 117, 283, 179, 145, 263, 131, 138, 287, 16,
                                                                             242, 105, 112, 160, 156, 12, 276, 178, 282, 149, 100, 109, 281, 24, 111, 174, 185, 218, 272, 144, 187, 279, 249, 255, 245, 285, 106, 164, 172, 18, 162,
                                                                             244, 115, 108, 23, 158, 175, 166, 148, 180, 271,
                                                                             243, 163, 146, 126, 186, 257, 238, 165, 273, 150, 167, 246, 113, 127, 102, 170, 128, 277, 220, 125, 147, 219, 14, 104, 129, 28, 189],
                    '/Users/akond/PUPP_REPOS/wikimedia-downloads/cdh':  [42, 27, 47, 3, 50, 26, 45, 46, 59, 2, 38, 56, 4, 34, 90, 33, 96, 122, 92, 104, 67, 98, 18, 76, 116, 6, 16, 78, 51, 24, 77, 115, 36, 60,
                                                                         29, 43, 64, 87, 28, 34, 84, 72, 12, 71, 19, 89, 119, 57, 120, 11, 41, 8, 100, 80, 48, 111, 13, 17, 99, 101, 52, 60, 44, 79, 75, 85, 68, 54,
                                                                         97, 109, 35, 9, 63, 27, 37, 83, 117, 61, 110, 31, 74, 1,
                                                                         82, 66, 107, 81, 32, 69, 93, 10, 7, 55, 86, 40, 103, 73, 102, 94, 65, 58, 14, 30, 49, 62, 70, 95, 88, 108, 118, 39, 113, 15, 53, 91],
                    '/Users/akond/PUPP_REPOS/wikimedia-downloads/cdh4':  [52, 4, 54, 8, 50, 51, 49, 53, 6, 9, 7, 5],
                    '/Users/akond/PUPP_REPOS/wikimedia-downloads/translatewiki':  [100, 103, 102, 113, 85, 108, 10, 112, 106, 92, 50, 47, 53, 109, 71, 111, 56, 48, 2, 86, 81, 32, 28, 84, 31, 45, 110, 36, 78, 29, 80,
                                                                                   54, 43, 107, 8, 89, 26, 35, 74, 82, 44, 3, 37, 88, 79, 25, 77, 4, 6, 49, 91, 76, 104, 75, 42, 55, 27, 105, 41, 51, 83, 33, 39, 46, 72, 101,
                                                                                   90, 40, 73, 58, 38, 115, 57, 34, 116, 87, 114, 24, 30, 52],
                    '/Users/akond/PUPP_REPOS/wikimedia-downloads/kafka':  [11, 13, 18, 10, 12, 1, 14, 16, 17, 15, 19]
                  }



excludeDictForMozilla = {  '/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet':  [1219, 1207, 1124, 1442, 1222, 1105, 1109, 1177, 114, 1074, 1314, 1047, 1008, 1020, 1040, 1122, 1096, 1039, 1052, 1234, 1176, 1051, 1100, 1009, 1155, 1173, 1042, 11, 105,
                                                                                        1224, 1085, 1127, 1209, 1230, 1066, 1043, 109, 1058, 1143, 1239, 1190, 1082, 110, 1099, 1163, 1150, 1195, 1094, 1129, 1025, 1080, 1027, 1142, 1022, 1002, 1800, 1203, 1035, 1053, 1228, 1130, 1023,
                                                                                        1065, 1077, 1316, 1003, 1237, 1182, 1005, 1054, 1178, 1462, 1141, 1181, 1179, 102, 1147, 1167, 1193, 1060, 1154, 1024, 1062, 1132, 1001, 1232, 1045, 1208, 1171, 1124, 1070, 1108, 1165, 1078, 103, 1235,
                                                                                        1006, 1146, 107, 1091, 1144, 1231, 1238, 1175, 1118, 1199, 1136, 10, 1083, 1007, 1135, 1103, 1164, 111, 1048, 1174, 1067, 1101, 1233, 1087, 1218, 1092, 1004, 1032, 1037, 1192, 1076, 1111, 1079, 1093,
                                                                                        1172, 1160, 1113, 1119, 1128, 1149, 1112, 1197, 1046, 1029, 1061, 1055, 1180, 1157, 1194, 1188, 1152, 1097, 1148, 1071, 1158, 1028, 1106, 1212, 1121, 1036, 175, 1090, 1200, 1229, 1115, 1123, 1217, 1117,
                                                                                        1120, 1213, 1186, 1161, 1225, 113, 1210, 1785, 1072, 1110, 1185, 1137, 1095, 1057, 1455, 1529, 1000, 1059, 112, 1151, 1166, 1198, 1205, 1140, 1206, 1184, 1139, 1098, 1088, 1221, 1075, 1159, 1138, 1031,
                                                                                        1050, 1041, 1021, 1196, 1170, 1223, 1168, 1131, 1793, 1073, 1201, 1034, 1236, 1044, 1169, 1068, 1791, 1204, 1211, 1133, 1049, 1240, 1818, 1214, 1030, 1102, 1056, 1216, 1226, 1107, 1227, 1589, 1134, 1162,
                                                                                        1202, 1187, 1116, 104, 106, 1064, 1153, 1220, 1081, 1104, 1215, 1069, 108, 1033, 1038, 1114, 1183, 1063, 1780, 1086, 1145, 1241, 1026, 1156, 1191, 1084, 1126, 1712, 1513, 160, 1526, 1762, 1755, 1540,
                                                                                        1125, 1745, 1480, 1747, 1685, 1487, 1723, 1592, 1767, 1794, 1859, 1681, 1586, 1512, 182, 1641, 179, 1711, 1781, 1853, 1474, 1682, 1625, 1766, 1498, 1486, 163, 174, 1479, 1691, 1748, 1765, 1736, 1644,
                                                                                        1741, 1735, 1583, 1524, 1708, 1775, 1497, 1525, 1740, 1515, 1575, 1684, 1756, 1491, 1493, 1523, 1483, 17, 1778, 1464, 1508, 1716, 1709, 16, 1510, 1744, 1764, 181, 1820, 128, 1773, 180, 1693, 156,
                                                                                        1473, 1609, 1718, 1519, 1857, 178, 1761, 1854, 1753, 1653, 1511, 1463, 1799, 1743, 1484, 1506, 1760, 1485, 1738, 1779, 1522, 1469, 1783, 1754, 1520, 1784, 1730, 1591, 1710, 1732, 1759, 1729, 1751, 176,
                                                                                        1494, 1750, 184, 1721, 1768, 1772, 1722, 1481, 1724, 1752, 1467, 161, 1466, 1719, 1683, 1518, 1608, 1492, 1834, 157, 1504, 1731, 127, 1858, 1720, 1499, 1797, 1477, 1472, 1509, 1478, 1528, 1482, 1742,
                                                                                        183, 1514, 1739, 1490, 159, 1769, 1856, 1585, 1737, 1680, 1582, 1687, 1489, 1521, 1770, 1495, 1507, 162, 1763, 173, 1617, 1733, 1782, 1516, 1696, 1662, 1748, 1471, 1725, 1860, 1686, 1488, 1734, 1475,
                                                                                        170, 1496, 1465, 1707, 1468, 1855, 1757, 1623, 1517, 1588, 1726, 177, 1746, 1476, 1527, 183, 1505, 1758, 1771, 1581, 1470],
                    '/Users/akond/PUPP_REPOS/mozilla-releng-downloads/relabs-puppet':  [172, 1330, 1617, 1565, 1005, 21, 228, 231, 1004, 1618, 1064, 239, 219, 1532, 1629, 1607, 1030, 1597, 235, 214, 15, 257, 1592, 182, 224, 1612, 20, 1197, 233, 1604, 223,
                                                                                        1019, 1170, 1520, 1405, 25, 222, 259, 250, 1035, 1209, 260, 1527, 1622, 193, 1366, 1609, 241, 194, 1118, 1055, 1598, 261, 1443, 1065, 103, 1631, 1414, 1061, 1200, 1056, 1185, 1380, 1383,
                                                                                        1051, 1363, 1157, 1179, 1029, 1210, 226, 1558, 206, 1442, 1043, 1573, 1103, 1447, 1094, 1326, 176, 1052, 1218, 1359, 1071, 120, 1023, 131, 1107, 1078, 1457, 1583, 1092, 1369, 1599, 1298,
                                                                                        1418, 1108, 163, 1580, 247, 1342, 199, 1116, 1539, 240, 1095, 1519, 1038, 1333, 1075, 1091, 1396, 170, 1444, 1594, 1158, 1105, 171, 1311, 238, 1372, 173, 253, 220, 1097, 1371, 1187, 1562,
                                                                                        200, 1354, 1020, 1003, 1393, 256, 117, 1079, 1424, 178, 1338, 1037, 1634, 138, 1437, 1365, 1076, 1389, 1575, 1102, 1395, 1225, 1224, 1398, 1188, 1222, 1082, 1352, 1217, 180, 1470, 1025, 1343,
                                                                                        216, 1626, 175, 1454, 1190, 1115, 1616, 1615, 1309, 1526, 1571, 1081, 1390, 1348, 1018, 1305, 1155, 1112, 1168, 1543, 19, 1590, 1633, 217, 1553, 1584, 1327, 1402, 245, 1572, 1171, 109, 1635, 1360,
                                                                                        1377, 1152, 225, 107, 1228, 1481, 1073, 186, 1153, 1059, 1322, 1391, 1084, 1302, 1379, 1422, 1117, 1062, 1109, 246, 218, 106, 1324, 189, 1206, 258, 1034, 1567, 1203, 1397, 1072, 1015, 1046, 1538,
                                                                                        165, 184, 1451, 1032, 1226, 1297, 1482, 1178, 1426, 1357, 1048, 1089, 1165, 1086, 1435, 1201, 1163, 1576, 132, 1467, 1012, 141, 1174, 1613, 1415, 1106, 1361, 197, 101, 1314, 1175, 1336, 1060, 1364,
                                                                                        1550, 1328, 11, 1160, 1347, 1307, 1427, 215, 1350, 1219, 1589, 1310, 1469, 1439, 1063, 1016, 12, 1582, 1540, 1194, 1196, 221, 1608, 1349, 236, 1387, 1014, 1318, 1417, 1528, 249, 212, 1161, 1040, 1049,
                                                                                        1367, 1525, 24, 1300, 1167, 1177, 111, 153, 1042, 1358, 140, 1204, 230, 1205, 196, 213, 1570, 1620, 1172, 162, 1033, 1011, 204, 1058, 1547, 135, 1031, 1413, 1028, 255, 1593, 1301, 1075, 1345, 1351,
                                                                                        1574, 1159, 1440, 1090, 181, 1193, 1408, 17, 1588, 1150, 1591, 1551, 210, 1578, 1164, 263, 1632, 1603, 1026, 1320, 1602, 155, 229, 1614, 1430, 1548, 1385, 1119, 1433, 1531, 152, 1601, 227, 115, 1450,
                                                                                        1198, 1453, 177, 1610, 1621, 1429, 1541, 1346, 1041, 237, 1355, 146, 1093, 1335, 108, 22, 1002, 13, 1186, 1211, 1564, 1176, 1001, 1456, 1421, 1088, 1331, 1227, 156, 1039, 1533, 234, 1008, 1080, 1445,
                                                                                        1024, 1207, 1624, 205, 1386, 1441, 1432, 1191, 1013, 191, 1195, 1428, 254, 1312, 1544, 1098, 1007, 202, 133, 154, 1554, 195, 1208, 1057, 1319, 1381, 207, 1537, 1036, 1340, 1536, 1344, 139, 1017, 262,
                                                                                        164, 168, 1623, 1586, 1521, 211, 1045, 1458, 1523, 1561, 1221, 1431, 169, 100, 1401, 251, 1524, 105, 1329, 1630, 203, 1410, 1304, 1627, 1053, 1455, 1425, 1202, 252, 1452, 140, 1409, 114, 1182, 157,
                                                                                        1306, 1337, 1047, 1110, 1600, 1535, 1448, 1111, 1220, 144, 1313, 1368, 1534, 1436, 1183, 1636, 1378, 209, 166, 1180, 1411, 1412, 1216, 1560, 1303, 1587, 1009, 1606, 1518, 1559, 1530, 1148, 1483,
                                                                                        1563, 1529, 1215, 183, 1637, 1568, 1638, 1050, 121, 1419, 1070, 1213, 1581, 1569, 1446, 232, 1542, 201, 1353, 1184, 1151, 1438, 1223, 1370, 1404, 1407, 142, 1373, 118, 1099, 119, 1114, 1027,
                                                                                        1423, 187, 16, 1619, 116, 1394, 1400, 1083, 1010, 1595, 1388, 1449, 1169, 1214, 143, 1545, 190, 243, 179, 1392, 1362, 1154, 1339, 188, 1468, 1577, 1557, 1325, 1069, 248, 104, 1085, 1066, 129,
                                                                                        1156, 1321, 208, 1121, 1375, 1434, 1021, 1403, 1181, 1334, 1374, 1628, 1212, 192, 1382, 110, 1162, 1315, 1054, 1317, 1376, 1356, 1323, 1579, 134, 1552, 1100, 1316, 1596, 1399, 151, 161, 1384,
                                                                                        1192, 1605, 137, 1416, 1006, 1341, 1189, 1625, 1104, 1074, 185, 1420, 1120, 1406, 1546, 1044, 136, 1166, 1566, 1332, 1549, 1000, 1585, 167, 1522,
                                                                                        1299, 18, 1611, 1113, 103, 1556, 159, 1022, 130, 158, 174, 1199, 1087, 1173, 244, 1077, 23, 1067, 198, 160, 1096, 1101, 1555, 10]
                  }
excludeDictForOpenstack = {
                       '/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-tripleo
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-openstack-integration
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/packstack
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-plugin-ci
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-monasca
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-plugin-cisco-aci
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-library
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-cinder
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-plugin-manila
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-rally
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-pacemaker
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-manila
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-plugin-opendaylight
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-plugin-contrail
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-plugin-nsx-t
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-swift
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-vitrage
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-watcher
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-nova
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-octavia
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-barbican
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-designate
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-plugin-lma-collector
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-ceph
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-glance
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-plugin-ironic
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-ironic
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-oslo
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-plugin-onos
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-magnum
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-ceilometer
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-congress
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-zaqar
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-openstack-cookiecutter
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-plugin-plumgrid
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-heat': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-plugin-lma-infrastructure-alerting': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-gnocchi': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-plugin-bigswitch': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-neutron': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-aodh': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-mistral': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-ec2api': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-keystone': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-plugin-external-zabbix': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-midonet': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/solar-resources': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-plugin-midonet': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-plugin-murano': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-plugin-mellanox': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-plugin-scaleio': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-trove': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-plugin-6wind-virtual-accelerator': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-plugin-influxdb-grafana': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-sahara': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-murano': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-plugin-datera-cinder': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-plugin-elasticsearch-kibana': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-plugin-purestorage-cinder': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/fuel-plugin-ceilometer-redis': [-999999]
'/Users/akond/PUPP_REPOS/mozilla-releng-downloads/puppet-qdr': [-999999]

                  }
