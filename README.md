# 微信AI训练数据工具包 (WeChat AI Training Data Toolkit)

一个强大的微信聊天记录处理工具包，专门用于将微信导出的聊天记录转换为AI模型训练数据格式。

## ✨ 功能特性

- 🔄 **多格式支持**: 支持GRPO、千问、ChatML等多种AI训练数据格式
- 🧹 **智能清洗**: 自动清理时间戳、发送者标识等冗余信息
- 📊 **数据分析**: 提供详细的数据质量分析和训练时长预估
- 🚀 **批量处理**: 支持大文件自动拆分和批量处理
- 📋 **一键流水线**: 提供完整的数据处理流水线

## 🛠️ 安装使用

### 环境要求

- Python 3.7+
- 依赖包：见 `requirements.txt`

### 快速开始

1. **克隆项目**
```bash
git clone https://github.com/yourusername/wechat-ai-training-data-toolkit.git
cd wechat-ai-training-data-toolkit
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **准备数据**
将微信导出的聊天记录JSON文件放入 `data/` 目录

4. **运行处理流水线**
```bash
python scripts/5_run_pipeline.py
```

## 📖 使用指南

### 核心脚本说明

| 脚本 | 功能 | 使用场景 |
|------|------|----------|
| `1_convert_grpo_format.py` | 转换为GRPO格式 | 强化学习训练数据 |
| `2_analyze_grpo_data.py` | 数据质量分析 | 训练前数据评估 |
| `3_split_large_json.py` | 大文件拆分 | 处理超大聊天记录 |
| `4_batch_clean_splits.py` | 批量清洗 | 批量处理拆分文件 |
| `5_run_pipeline.py` | 一键流水线 | 完整数据处理流程 |

### 配置文件

修改 `scripts/config.py` 来自定义处理参数：

```python
# 数据文件路径
INPUT_FILE = "data/message.json"
OUTPUT_DIR = "data/output"

# 处理参数
MAX_FILE_SIZE_MB = 100
BATCH_SIZE = 1000
```

### 数据格式

#### 输入格式（微信导出）
```json
{
  "messages": [
    {
      "talker": "用户名",
      "content": "消息内容",
      "timestamp": "2024-01-01 10:00:00"
    }
  ]
}
```

#### 输出格式（GRPO）
```json
{
  "problem": "用户问题",
  "solution": "AI回答",
  "messages": [
    {"role": "user", "content": "用户消息"},
    {"role": "assistant", "content": "AI回复"}
  ]
}
```

## 📊 数据统计

处理完成后会生成详细的数据报告：
- 总样本数量
- 消息分布统计
- 训练时长预估
- 数据质量评分

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 发起Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

- 感谢所有贡献者
- 基于微信聊天记录导出格式
- 适配主流AI训练框架

## 📞 联系方式

如有问题或建议，请通过以下方式联系：

- 提交 [Issue](https://github.com/yourusername/wechat-ai-training-data-toolkit/issues)
- 发起 [Discussion](https://github.com/yourusername/wechat-ai-training-data-toolkit/discussions)

---

⭐ 如果这个项目对您有帮助，请给个Star支持一下！