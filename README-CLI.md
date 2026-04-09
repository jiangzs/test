# 斐波那契 CLI 工具

一个用于计算斐波那契数列的命令行工具，专为教学演示设计。

## 功能特性

- 📊 计算第 n 个斐波那契数
- 📋 显示前 n 项斐波那契序列（表格格式）
- 🎓 交互式学习模式
- 👶 新手引导模式
- ❌ 友好的错误提示

## 安装

```bash
# 安装依赖
pip install -r requirements-cli.txt
```

## 使用方法

### 基础计算

```bash
# 计算第 10 个斐波那契数
python -m cli.main 10

# 或者使用模块方式
python src/cli/main.py 10
```

### 序列显示

```bash
# 显示前 5 项序列
python -m cli.main sequence 5
python src/cli/main.py seq 5
```

### 交互模式

```bash
# 进入交互模式
python -m cli.main -i
python src/cli/main.py interact
```

### 新手引导

```bash
# 启动新手引导
python -m cli.main --guide
python src/cli/main.py guide
```

### 帮助信息

```bash
python -m cli.main --help
```

## 运行测试

```bash
pytest tests/ -v
```

## 项目结构

```
src/cli/
├── __init__.py      # 模块初始化
├── main.py          # Typer 主入口
├── commands.py      # 命令实现
├── interactive.py   # 交互模式
└── formatters.py    # 输出格式化
tests/
├── test_cli.py
├── test_interactive.py
└── test_formatters.py
```
