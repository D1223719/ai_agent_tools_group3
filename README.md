# AI agent 開發分組實作

> 課程：AI agent 開發 — Tool 與 Skill
> 主題： 旅遊前哨站

---

## Agent 功能總覽

> 這個 Agent 身兼「旅遊行前助理」，能夠主動詢問使用者的旅遊目的地與時間。不僅能即時查詢當地理氣象資訊，還可依據天氣給出防護穿搭建議，甚至能提供旅遊途中的人生格言與景點搜尋，最終產出一份精美的行前簡報！

| 使用者輸入   | Agent 行為                             | 負責組員 |
| ------------ | -------------------------------------- | -------- |
| （例：天氣） | 呼叫 `get_city_weather`，查詢即時天氣        |          |
| （例：穿搭） | 呼叫 `get_outfit_suggestion`，取得氣候穿搭建議  |          |
| （例：景點） | 呼叫 `search_travel_tips`，取得熱門景點與資訊 |          |
| （例：出發） | 執行 `trip_briefing` Skill，自動組合工具產出簡報 |          |

---

## 組員與分工

| 姓名 | 負責功能        | 檔案        | 使用的 API |
| ---- | --------------- | ----------- | ---------- |
|      | 天氣查詢工具    | `tools/weather.py` | `wttr.in` |
|      | 穿搭建議工具    | `tools/outfit_advisor.py` | — (本機判斷邏輯) |
|      | 景點搜尋工具    | `tools/searching_tips.py` | `DuckDuckGo API` |
|      | Skill 腳本整合  | `skills/trip_briefing.txt` | —         |
|      | Agent 與面板主程式 | `main.py` / `dashboard_with_skill.html` | `Gemini API` |

---

## 專案架構

```
├── tools/
│   ├── __init__.py
│   ├── weather.py         # 氣象查詢模組
│   ├── outfit_advisor.py  # 穿搭判斷模組
│   ├── search.py          # 網路搜尋模組
│   ├── searching_tips.py  # 景點旅遊搜尋模組
│   └── pdf_reader.py      # PDF文件讀取工具
├── skills/
│   └── trip_briefing.txt  # 旅遊行前助理 System Prompt
├── pdfs/                  # 當地 PDF 檔案存放區
├── dashboard_with_skill.html # 旅遊特化視覺互動儀表板
├── main.py                # 應用主程式入口
├── requirements.txt       # Python套件相依清單
└── README.md              # 系統專案說明文件
```

---

## 使用方式

```bash
# 1. 建立虛擬環境 (視作業系統而異)
python3 -m venv .venv
# 2. 啟動虛擬環境 (Windows 請執行 .venv\Scripts\activate)
source .venv/bin/activate
# 3. 安裝依賴套件
pip install -r requirements.txt
# 4. 配置環境變數 (在目錄建立 .env 檔案並寫入 GEMINI_API_KEY=你的金鑰)
# 5. 啟動 Agent
python main.py
```

---

## 執行結果

> 以下為使用者給定目的地後，系統自動依序調用天氣與穿搭工具產生的的結果：

```
======================================================
  Gemini 旅遊行前助理 (Travel Agent) 已啟動！
  告訴我您的目的地與時間，我將幫您準備行前簡報，預報天氣與建議穿搭！
  輸入 'exit' 或 'quit' 來結束對話。
======================================================

[可用技能列表]
 1. trip_briefing

請選擇要載入的技能編號 (直接按 Enter 鍵跳過，不載入技能): 1
-> 成功載入技能: trip_briefing.txt


你: 我下禮拜要去東京玩三天兩夜

[Tool Execution] Agent 調用了 'get_city_weather' 工具
[Tool Execution] 傳入參數: city='Tokyo'
[Tool Execution] 正在透過 wttr.in 獲取 Tokyo 的天氣...
[Tool Execution] 獲取成功！回傳結果: Tokyo 現在的天氣是: ⛅️ +18°C

[Tool Execution] Agent 調用了 'get_outfit_suggestion' 工具
[Tool Execution] 傳入參數: weather_condition='Cloudy', temp_celsius=18
[Tool Execution] 獲取成功！回傳結果:
【穿搭建議】
氣候偏涼。建議穿著長袖上衣，搭配薄外套或針織衫，採洋蔥式穿搭。

Agent: 🌍 【目的地資訊】
東京三天兩夜行程即將開始，祝您有個美好愉快的旅途！

🌤️ 【當地天氣狀況】
為您查詢到東京天氣可能為多雲 (Cloudy)，氣溫大約在 18°C 左右。偏向微涼不出太陽的氣候。

🎒 【穿搭建議指南】
根據當地氣候，現在氣候偏涼。建議您穿著長袖上衣，搭配薄外套或針織衫，採洋蔥式穿搭。即使白天稍熱也很容易脫卸喔。

💡 【行前溫馨提醒】
18°C 稍微有些涼意，早晚溫差可能較大，出門在外務必攜帶保暖小外套。另外，可以隨機查詢好玩的景點做雙重規劃！祝您日本之旅滿載而歸！
```

---

## 各功能說明

### 天氣查詢模組（負責：）

- **Tool 名稱**：`get_city_weather`
- **使用 API**：`wttr.in`
- **輸入**：字串 `city` (目的地名稱)
- **輸出範例**：`Tokyo 現在的天氣是: ⛅️ +18°C`

```python
{
    "name": "get_city_weather",
    "description": "獲取指定城市的天氣資訊 (透過 wttr.in)",
    "parameters": { 
        "city": "string"
    }
}
```

### 穿搭建議模組（負責：）

- **Tool 名稱**：`get_outfit_suggestion`
- **使用 API**：無 (依據輸入參數於本地撰寫條件式產出建議)
- **輸入**：字串 `weather_condition` (天氣狀況), 數值 `temp_celsius` (攝氏溫度)
- **輸出範例**：`天氣寒冷。建議穿著厚毛衣、發熱衣，並搭配防風保暖的大衣或外套。有降雪可能，請穿著具備防滑功能的鞋子，並確保衣物防水。`

### 景點搜尋模組（負責：）

- **Tool 名稱**：`search_travel_tips`
- **使用 API**：`DuckDuckGo API` (`duckduckgo-search` 套件)
- **輸入**：字串 `query` (搜尋關鍵字), 數值 `max_results` (最多結果數，預設 8)
- **輸出範例**：
```text
以下是關於「Tokyo 景點」的搜尋結果：

1. 【2024 東京 10 大必去景點推薦】
   包含東京鐵塔、淺草寺雷門、晴空塔與秋葉原等熱門區域的旅遊攻略...
   來源: https://example.com/tokyo-guide
```

### Skill：旅遊行前簡報（負責：）

- **組合了哪些 Tool**：主要是 `get_city_weather` 與 `get_outfit_suggestion` (AI 也會視情況搭配搜尋工具)
- **執行順序**：

```
Step 1: 詢問使用者並理解輸入 → 取得 旅遊目的地與時間長度
Step 2: 自動呼叫 get_city_weather → 取得 該目的地的氣候預報
Step 3: 將取得的天氣與溫度送給 get_outfit_suggestion → 取得 個人化的防寒防雨裝備指南
Step 4: 組合上述取得的所有輸出與既有的 System Prompt 性格 → 產生 一份圖文並茂的行前簡報
```

---

## 心得

### 遇到最難的問題

> (請於此填入各組員遭遇的難關，例如：原本的儀表板是單一 Chatbox 設計，面對多重工具模組時會導致版面壅擠及混亂；為此運用了「切換式前端設計」結合 Local Storage 搭配 JSON 來儲存，順利將多個頻道的對話進行隔離。)

### Tool 和 Skill 的差別

> (請於此填入：Tool 像是一個單一的「手腳」，幫 Agent 查詢或處理非常特定範圍的事項（例如給定城市抓取溫度）；而 Skill 就像給 Agent 注入了「靈魂與腳本」，它透過 System Prompt 定義了人設、思考邏輯與工作SOP，讓 Agent 大腦知道「什麼時候該去調用哪個 Tool」，並統整結果回報給使用者。)

### 如果再加一個功能

> (請於此填入：我希望能再加入例如『機票航班查詢 Tool』或是『Google Maps 熱門餐廳 Tool』，這樣配合這套行前簡報系統，不但有天氣與穿搭，連最重要的「食」與「行」都可以靠 Agent 全自動解決！)
