import streamlit as st
import pandas as pd


st.title("📍南宁美食探索")

map_data = {
    'latitude':[22.689314,22.772521,22.824100,22.838174,23.157285],
    'longitude':[108.363011,108.373943,108.341972,108.296089,108.280233]
}

st.map(pd.DataFrame(map_data))

import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(1000, 2) / [20, 50] + [39.9, 116.4],
    columns=['latitude', 'longitude'])
data = {
    '月份':['01月', '02月', '03月','04月','05月'],
    '🍽池又又融合小食堂':[200, 150, 180],
    '🍖雷记烧烤':[120, 160, 123],
    '🥢古记卷筒粉':[110, 100, 160],
    '🧆山东人家土菜馆':[120, 160, 123],
    '🥤泰吉吉':[120, 160, 123],
}

import streamlit as st
import pandas as pd

# 定义数据,以便创建数据框
data = {
    '月份':['01月', '02月', '03月'],
    '池又又融合小食堂':[200, 150, 180],
    '雷记烧烤':[120, 160, 123],
    '古记卷筒粉':[110, 100, 160],
    '山东人家土菜馆':[120, 160, 123],
    '泰吉吉':[120, 160, 123],
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3], name='序号')
# 将新索引应用到数据框上
df.index = index

st.header("🥧餐厅月评分数")
# 使用write()方法展示数据框
st.write(df)
st.header("条形图")


# 通过x指定月份所在这一列为条形图的x轴
st.bar_chart(df, x='月份')

# 修改df，用月份列作为df的索引，替换原有的索引
df.set_index('月份', inplace=True)

import streamlit as st
import pandas as pd

# 定义数据,以便创建数据框
data = {
    '月份':['01月（万元）', '02月（万元）', '03月（万元）'],
     '池又又融合小食堂':[8, 10, 10.5],
    '雷记烧烤':[10, 11, 12],
    '古记卷筒粉':[5, 4, 5.5],
    '山东人家土菜馆':[9, 13, 9.5],
    '泰吉吉':[7, 5, 8]
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3,], name='序号')
# 将新索引应用到数据框上
df.index = index

st.header("💰餐厅月销售额变化数据")
# 使用write()方法展示数据框
st.write(df)
st.header("数据折线图")


# 通过x指定月份所在这一列为折线图的x轴
st.line_chart(df, x='月份')


# 修改df，用月份列作为df的索引，替换原有的索引
df.set_index('月份', inplace=True)

import streamlit as st
import pandas as pd

# 定义数据,以便创建数据框
data = {
    '时间段':['8.0-10.0','11.0-13.0','14.0-16.0'],
     '池又又融合小食堂':[30, 80, 150],
    '雷记烧烤':[40, 40, 140],
    '古记卷筒粉':[100, 60, 50],
    '山东人家土菜馆':[40, 70, 150],
    '泰吉吉':[70, 50, 100]
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3,], name='序号')
# 将新索引应用到数据框上
df.index = index

st.header("🙆用餐高峰时段人流量数")
# 使用write()方法展示数据框
st.write(df)
st.header("面积图")


# 通过x指定月份所在这一列为面积图的x轴
st.area_chart(df, x='时间段')

# 修改df，用月份列作为df的索引，替换原有的索引
df.set_index('时间段', inplace=True)




# 餐厅数据
restaurants_data = {
    "餐厅": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "西冷牛排店"],
    "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐"],
    "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
    "人均消费(元)": [15, 20, 25, 35, 50],
    "latitude": [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
    "longitude": [108.222177, 108.353921, 108.266629, 108.378664, 108.245804]
}

