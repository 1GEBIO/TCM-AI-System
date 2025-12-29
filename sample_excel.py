import pandas as pd
import random

# 1. 定义模拟数据
herbs = [
    '石菖蒲', '全蝎', '蜈蚣', '天麻', '川芎', '僵蚕', '柴胡', '当归', '白芍', '茯苓',
    '甘草', '半夏', '胆南星', '郁金', '远志', '酸枣仁', '龙骨', '牡蛎', '钩藤', '地龙'
]

categories = ['开窍药', '息风止痉药', '活血化瘀药', '补气药', '清热药', '化痰药', '安神药']
origins = ['安徽', '河南', '湖北', '云南', '四川', '甘肃', '内蒙古', '浙江', '山西']
four_qi = ['温', '平', '寒', '凉', '热']
five_flavors = ['辛', '苦', '甘', '酸', '咸']
meridians = ['心经', '肝经', '脾经', '肺经', '肾经']
dynasties = ['汉代', '唐代', '宋代', '金元', '明代', '清代']

# 2. 构建数据集
data = []
for herb in herbs:
    data.append({
        '中药': herb,
        '频次': random.randint(100, 1500),
        '类别': random.choice(categories),
        '产地': random.choice(origins),
        '四气': random.choice(four_qi),
        '五味': random.choice(five_flavors),
        '归经': random.choice(meridians),
        '剂量': random.randint(3, 15),
        '巅峰朝代': random.choice(dynasties),
        'MW': random.randint(150, 500),      # 分子量
        'LogP': round(random.uniform(1, 5), 2), # 脂水分配系数
        'OB': round(random.uniform(20, 80), 2)  # 生物利用度
    })

# 3. 创建 DataFrame 并保存
df = pd.DataFrame(data)

# 保存为 Excel
file_name = 'sample_tcm.xlsx'
df.to_excel(file_name, index=False)

print(f"✅ 成功生成示例数据：{file_name}")
print(f"包含列名：{list(df.columns)}")