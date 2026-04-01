import os
import glob

def read_code_files() -> str:
    """
    讀取專案中 'code' 資料夾底下的所有 .py 程式碼檔案，並將其全部內容回傳，
    讓你可以依照檔案內容進行 Code Review 或程式碼分析。
    
    Returns:
        包含所有 .py 檔案路徑與程式碼內容的合併字串。
    """
    print(f"\n[Tool Execution] Agent 調用了 'read_code_files' 工具")
    
    code_dir = "code"
    
    if not os.path.exists(code_dir):
        error_msg = f"找不到 '{code_dir}' 資料夾，請確認它是否存在於專案根目錄中。"
        print(f"[Tool Execution] 發生錯誤: {error_msg}\n")
        return error_msg
        
    py_files = glob.glob(os.path.join(code_dir, "*.py"))
    
    if not py_files:
        error_msg = f"'{code_dir}' 資料夾中沒有找到任何 .py 檔案。"
        print(f"[Tool Execution] 發生錯誤: {error_msg}\n")
        return error_msg
        
    print(f"[Tool Execution] 成功找到 {len(py_files)} 個 Python 檔案，正在讀取...")
    
    content_list = []
    
    for file_path in py_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code_content = f.read()
                content_list.append(f"--- File: {file_path} ---\n```python\n{code_content}\n```\n")
        except Exception as e:
            content_list.append(f"--- File: {file_path} (讀取失敗: {str(e)}) ---\n")
            
    full_content = "\n".join(content_list)
    print(f"[Tool Execution] 讀取完成！已提取所有程式碼並準備交由 Agent 分析。\n")
    
    return full_content
