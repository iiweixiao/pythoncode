# import os
# if not os.path.exists('up_ids.txt'):
#     with open('up_ids.txt', 'w') as f:
#         up_id = '20165629:共青团中央'
#         f.write(up_id)
#
# up_ids = []
# with open('up_ids.txt', 'r') as f:
#     s = f.read()
#
# lst = s.splitlines()
#
# for item in lst:
#     if '：' in item:
#         item = item.replace('：', ':')
#     up_ids.append(item.split(':')[0])
# print(up_ids)