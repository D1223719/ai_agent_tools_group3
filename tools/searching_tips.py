from duckduckgo_search import DDGS

def search_travel_tips(query: str, max_results: int = 8) -> str:
    """
    搜尋指定地點的熱門景點或旅遊注意事項。

    Args:
        query: 搜尋關鍵字，例如 "Tokyo 景點"、"Paris 注意事項"、"台北 必去景點"。
        max_results: 最多回傳幾筆搜尋結果，預設為 8。

    Returns:
        一段包含景點資訊或旅遊注意事項的字串摘要。
    """
    print(f"\n[Tool Execution] Agent 調用了 'search_travel_tips' 工具")
    print(f"[Tool Execution] 傳入參數: query='{query}', max_results={max_results}")
    print(f"[Tool Execution] 正在透過 DuckDuckGo 搜尋: {query} ...")

    try:
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=max_results):
                results.append(r)

        if not results:
            msg = f"找不到關於「{query}」的相關資訊，請嘗試其他關鍵字。"
            print(f"[Tool Execution] 無搜尋結果。\n")
            return msg

        # 整合搜尋結果成結構化字串
        output_lines = [f"以下是關於「{query}」的搜尋結果：\n"]
        for i, r in enumerate(results, start=1):
            title = r.get("title", "（無標題）")
            body  = r.get("body",  "（無內容摘要）")
            href  = r.get("href",  "")
            output_lines.append(f"{i}. 【{title}】")
            output_lines.append(f"   {body}")
            if href:
                output_lines.append(f"   來源: {href}")
            output_lines.append("")   # 空行分隔

        result_str = "\n".join(output_lines)
        print(f"[Tool Execution] 搜尋成功！共取得 {len(results)} 筆結果。\n")
        return result_str

    except Exception as e:
        error_msg = f"搜尋「{query}」時發生錯誤: {str(e)}"
        print(f"[Tool Execution] 發生錯誤: {error_msg}\n")
        return error_msg
