import os
import glob
import google.generativeai as genai
from tools import get_city_weather, read_pdf_content, read_code_files, search_weather_outfit
from dotenv import load_dotenv

def load_skill_prompt() -> str:
    """讓使用者選擇並載入 skills 目錄下的技能 (System Prompt)"""
    skills_dir = "skills"
    if not os.path.exists(skills_dir):
        return ""
        
    txt_files = glob.glob(os.path.join(skills_dir, "*.txt"))
    if not txt_files:
        return ""
        
    print("\n[可用技能列表]")
    for i, file in enumerate(txt_files):
        skill_name = os.path.splitext(os.path.basename(file))[0]
        print(f" {i+1}. {skill_name}")
        
    choice = input("\n請選擇要載入的技能編號 (直接按 Enter 鍵跳過，不載入技能): ")
    if choice.isdigit() and 1 <= int(choice) <= len(txt_files):
        try:
            with open(txt_files[int(choice)-1], 'r', encoding='utf-8') as f:
                skill_content = f.read()
                print(f"-> 成功載入技能: {os.path.basename(txt_files[int(choice)-1])}\n")
                return skill_content
        except Exception as e:
            print(f"讀取技能檔案失敗: {e}\n")
    return ""

def main():
    # 載入環境變數 (讀取 .env 檔案)
    load_dotenv()
    
    # 設置 API 金鑰
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("警告: 找不到 GEMINI_API_KEY。請確認已設定環境變數或在 .env 檔案中指定。")
        return

    genai.configure(api_key=api_key)
    
    # 1. 詢問並載入 Skill (System Prompt)
    system_instruction = load_skill_prompt()

    # 2. 建立模型實例並配置 tool 與 system instruction
    # 注意: system_instruction 參數能在系統層級影響模型行為
    model_kwargs = {
        "model_name": 'gemini-2.5-flash',
        "tools": [get_city_weather, read_pdf_content, read_code_files, search_weather_outfit]
    }
    
    if system_instruction:
        model_kwargs["system_instruction"] = system_instruction
        
    model = genai.GenerativeModel(**model_kwargs)

    # 啟動對話 (使用 enable_automatic_function_calling=True)
    print("======================================")
    print("  Gemini 萬能 Agent 已啟動！")
    print("  你可以問我天氣、讀取 PDF、或幫你作 Code Review。")
    print("  輸入 'exit' 或 'quit' 來結束對話。")
    print("======================================\n")
    
    chat = model.start_chat(enable_automatic_function_calling=True)

    while True:
        try:
            user_input = input("\n你: ")
            if user_input.lower() in ['exit', 'quit']:
                break
                
            if not user_input.strip():
                continue
                
            # 為了讓你能「明確了解發送了什麼」，我們在此印出包含 Skill 與 User Input 的完整結構
            print("\n" + "="*50)
            print(" [正在發送至 Gemini 的完整 Prompt 結構]")
            if system_instruction:
                print("\n【System Instruction (Skill)】:")
                print(system_instruction.strip())
            print(f"\n【User Message】: \n{user_input}")
            print("="*50 + "\n") 
            
            # 獲取回應
            response = chat.send_message(user_input)
            
            print(f"\nAgent: {response.text}")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"\n發生錯誤: {e}")

if __name__ == "__main__":
    main()
