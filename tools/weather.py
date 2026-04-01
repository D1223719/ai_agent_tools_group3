import urllib.request
import urllib.parse
import json

def get_city_weather(city: str) -> str:
    """
    獲取指定城市的天氣資訊 (透過 wttr.in)。
    
    Args:
        city: 城市名稱，例如 "Taipei", "Tokyo", "London"。
    
    Returns:
        一段包含天氣資訊的字串。
    """
    print(f"\n[Tool Execution] Agent 調用了 'get_city_weather' 工具")
    print(f"[Tool Execution] 傳入參數: city='{city}'")
    print(f"[Tool Execution] 正在透過 wttr.in 獲取 {city} 的天氣...")

    # 使用 wttr.in 的 format=3 獲取單行天氣描述
    url = f"https://wttr.in/{urllib.parse.quote(city)}?format=3"
    req = urllib.request.Request(url, headers={'User-Agent': 'curl/7.81.0'})
    
    try:
        with urllib.request.urlopen(req) as response:
            weather_data = response.read().decode('utf-8').strip()
            print(f"[Tool Execution] 獲取成功！回傳結果: {weather_data}\n")
            return f"{city} 現在的天氣是: {weather_data}"
    except Exception as e:
        error_msg = f"無法獲取 {city} 的天氣資訊: {str(e)}"
        print(f"[Tool Execution] 發生錯誤: {error_msg}\n")
        return error_msg
