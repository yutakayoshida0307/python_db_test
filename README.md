
# python_DB_test

## 実行方法

### DBの起動
```
docker compose up
```

### パッケージのインストール
初回のみ
```
brew install uv
```

各プロジェクトを開く

例
```
cd python_raw_sql_test
```

以下コマンドを実行

```
uv sync
```

### 各プロジェクトで単体テストを実行

#### VSCode

各プロジェクトをVSCodeで開く

例

```
code ./python_raw_sql_test
```

テストを実行する


