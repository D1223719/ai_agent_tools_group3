def get_outfit_suggestion(weather_condition: str, temp_celsius: int) -> str:
    """
    根據天氣狀況與氣溫給出穿搭建議。
    
    Args:
        weather_condition: 天氣狀況描述 (例如: "Sunny", "Rain", "Cloudy")
        temp_celsius: 預計氣溫 (攝氏)
        
    Returns:
        一段建議的穿搭字串。
    """
    print(f"\n[Tool Execution] Agent 調用了 'get_outfit_suggestion' 工具")
    print(f"[Tool Execution] 傳入參數: weather_condition='{weather_condition}', temp_celsius={temp_celsius}")

    suggestion = "【穿搭建議】\n"
    
    # 根據溫度給出基本穿搭建議
    if temp_celsius >= 28:
        suggestion += "此溫度非常炎熱。建議穿著輕薄透氣的短袖、短褲，並注意防曬與補充水分。\n"
    elif 20 <= temp_celsius < 28:
        suggestion += "氣候舒適微熱。建議穿著短袖或薄長袖，可搭配休閒長褲或裙裝。\n"
    elif 12 <= temp_celsius < 20:
        suggestion += "氣候偏涼。建議穿著長袖上衣，搭配薄外套或針織衫，採洋蔥式穿搭。\n"
    elif 5 <= temp_celsius < 12:
        suggestion += "天氣寒冷。建議穿著厚毛衣、發熱衣，並搭配防風保暖的大衣或外套。\n"
    else:
        suggestion += "天氣非常寒冷。強烈建議穿著羽絨衣、發熱衣物，並準備毛帽、手套與圍巾等禦寒配件。\n"
        
    # 根據天氣狀況給出額外建議
    weather_lower = weather_condition.lower()
    if "rain" in weather_lower or "drizzle" in weather_lower or "shower" in weather_lower or "雨" in weather_lower:
        suggestion += "有下雨可能，請記得攜帶雨具（雨傘或雨具），建議穿著防水鞋履。\n"
    elif "sun" in weather_lower or "clear" in weather_lower or "晴" in weather_lower:
        suggestion += "天氣晴朗，建議準備墨鏡與防曬用品以保護皮膚。\n"
    elif "snow" in weather_lower or "雪" in weather_lower:
        suggestion += "有降雪可能，請穿著具備防滑功能的鞋子，並確保衣物防水。\n"
        
    print(f"[Tool Execution] 獲取成功！回傳結果:\n{suggestion}\n")
    return suggestion
