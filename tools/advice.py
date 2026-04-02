import urllib.request
import json

def get_travel_advice() -> str:
    """
    取得一則出發前的人生建議（旅行格言）。
    此工具會從 Advice Slip API (https://api.adviceslip.com/advice) 取得隨機的一句話。
    
    Returns:
        一段包含隨機人生建議或旅行格言的字串。
    """
    print(f"\n[Tool Execution] Agent 調用了 'get_travel_advice' 工具")
    print(f"[Tool Execution] 正在獲取隨機的人生意義與旅行格言...")

    url = "https://api.adviceslip.com/advice"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            advice = data['slip']['advice']
            print(f"[Tool Execution] 獲取成功！回傳結果: {advice}\n")
            return f"給您的隨機旅行建議與格言是: {advice}"
    except Exception as e:
        error_msg = f"無法獲取建議: {str(e)}"
        print(f"[Tool Execution] 發生錯誤: {error_msg}\n")
        return error_msg
