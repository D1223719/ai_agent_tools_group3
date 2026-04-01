import os
try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None

def read_pdf_content(filename: str) -> str:
    """
    讀取資料夾內指定的 PDF 檔案，並回傳其純文字內容，以便按照文件內容回答使用者的問題。
    
    Args:
        filename: PDF 檔案名稱 (例如: "document.pdf" 或 "sample.pdf")。包含附檔名。
    
    Returns:
        該 PDF 檔案內的完整文字內容。如果檔案不存在或發生錯誤，將會回傳錯誤訊息。
    """
    print(f"\n[Tool Execution] Agent 調用了 'read_pdf_content' 工具")
    print(f"[Tool Execution] 傳入參數: filename='{filename}'")
    
    if PdfReader is None:
        error_msg = "尚未安裝 pypdf 套件，請執行 'pip install pypdf'"
        print(f"[Tool Execution] 發生錯誤: {error_msg}\n")
        return error_msg
        
    # 首先嘗試從 pdfs 資料夾尋找，若沒有則從根目錄尋找
    filepath = os.path.join("pdfs", filename)
    if not os.path.exists(filepath):
        filepath = filename
        
    if not os.path.exists(filepath):
        error_msg = f"找不到檔案: {filename}。請確認 PDF 檔案是否放在 'pdfs' 資料夾或當前專案目錄下。"
        print(f"[Tool Execution] 發生錯誤: {error_msg}\n")
        return error_msg
        
    print(f"[Tool Execution] 正在解析 PDF 檔案: {filepath} ...")
    
    try:
        reader = PdfReader(filepath)
        text_content = []
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                text_content.append(f"--- 第 {i+1} 頁 ---\n{text}")
                
        full_text = "\n".join(text_content)
        
        print(f"[Tool Execution] 讀取成功！共提取了 {len(reader.pages)} 頁的文字內容。\n")
        return full_text
    
    except Exception as e:
        error_msg = f"讀取 PDF 發生錯誤: {str(e)}"
        print(f"[Tool Execution] 發生錯誤: {error_msg}\n")
        return error_msg
