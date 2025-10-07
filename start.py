#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信AI训练数据工具包 - 主启动脚本
快速开始处理微信聊天记录
"""

import os
import sys
from pathlib import Path

def main():
    """主函数"""
    print("🚀 微信AI训练数据工具包")
    print("=" * 50)
    
    print("\n📋 可用操作:")
    print("1. 转换为GRPO格式")
    print("2. 分析数据质量")
    print("3. 拆分大文件")
    print("4. 批量处理")
    print("5. 运行完整流水线")
    print("0. 退出")
    
    while True:
        try:
            choice = input("\n请选择操作 (0-5): ").strip()
            
            if choice == "0":
                print("👋 再见！")
                break
            elif choice == "1":
                os.system("python scripts/1_convert_grpo_format.py")
            elif choice == "2":
                os.system("python scripts/2_analyze_grpo_data.py")
            elif choice == "3":
                os.system("python scripts/3_split_large_json.py")
            elif choice == "4":
                os.system("python scripts/4_batch_clean_splits.py")
            elif choice == "5":
                os.system("python scripts/5_run_pipeline.py")
            else:
                print("❌ 无效选择，请输入 0-5")
                
        except KeyboardInterrupt:
            print("\n\n👋 操作被中断，再见！")
            break

if __name__ == "__main__":
    main()