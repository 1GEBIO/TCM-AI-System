from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI(title="TCM-LMH API Core")

# 定义数据模型
class DiagnosisRequest(BaseModel):
    symptoms: list[str]

# 1. 模拟数据库中的真实药材
REAL_HERB_DB = {
    "石菖蒲": {"产地": "安徽", "归经": "心经", "功效": "开窍豁痰"},
    "全蝎": {"产地": "河南", "归经": "肝经", "功效": "息风止痉"}
}

# 接口 A：获取全量药物列表 (替代原来的 process_data)
@app.get("/herbs/list")
def get_all_herbs():
    # 在真实场景中，这里会查询 MySQL/Neo4j
    return {"data": list(REAL_HERB_DB.keys()), "count": len(REAL_HERB_DB)}

# 接口 B：AI 智能诊断 (替代原来的随机推荐)
@app.post("/clinic/diagnose")
def ai_diagnose(req: DiagnosisRequest):
    # 这里接入真正的 DeepSeek / GPT 接口
    print(f"接收到症状: {req.symptoms}")
    
    # 模拟 AI 推理过程
    if "喉间痰鸣" in req.symptoms:
        return {
            "formula": "定痫丸加减",
            "composition": ["石菖蒲", "胆南星", "半夏"],
            "confidence": 0.92
        }
    else:
        return {
            "formula": "通用基础方",
            "composition": ["甘草", "茯苓"],
            "confidence": 0.5
        }

# 启动命令: uvicorn backend:app --reload