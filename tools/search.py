from ddgs import DDGS

def search_weather_outfit(city: str) -> str:
    """
    透過 DuckDuckGo 搜尋指定城市的「一般性穿搭建議」或「旅遊文章」。
    
    注意：此工具主要尋找穿搭指南，**不保證能獲取即時的氣象資料**！
    如果使用者詢問「今天」、「現在」或「即時」的天氣穿搭，
    請務必「同時或先」呼叫 `get_city_weather` 工具取得目前精準天氣，
    再綜合本工具找到的穿搭建議來回答使用者。
    
    Args:
        city: 城市名稱，例如 "Taipei", "Tokyo", "London"。
    
    Returns:
        包含從網路搜尋到的穿搭建議字串。
    """
    query = f"{city} 天氣 穿搭"
    print(f"\n[Tool Execution] Agent 調用了 'search_weather_outfit' 工具")
    print(f"[Tool Execution] 傳入參數: city='{city}'")
    print(f"[Tool Execution] 正在透過 DuckDuckGo 搜尋: '{query}' ...")
    
    try:
        results = ""
        with DDGS() as ddgs:
            search_results = list(ddgs.text(query, max_results=3))
            
            if not search_results:
                return f"根據 '{query}' 找不到天氣與穿搭的相關資訊。"
            
            for index, res in enumerate(search_results):
                title = res.get('title', '無標題')
                body = res.get('body', '無內容')
                href = res.get('href', '')
                results += f"{index+1}. {title}\n   {body}\n   {href}\n\n"
        
        print(f"[Tool Execution] 搜尋成功！已取得相關建議。\n")
        return f"以下是關於 '{query}' 的搜尋結果（包含穿搭建議）:\n\n{results}"
        
    except Exception as e:
        error_msg = f"搜尋 {city} 的天氣穿搭時發生錯誤: {str(e)}"
        print(f"[Tool Execution] 發生錯誤: {error_msg}\n")
        return error_msg
