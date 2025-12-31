import os

def generate_project_summary():
    # Analiz edilecek kritik dosyalar [cite: 2025-12-31]
    critical_files = [
        "architect.py", 
        "coder.py", 
        "main_vyno.py", 
        "publisher.py", 
        "current_project_plan.txt"
    ]
    
    summary = "=== VYNO PROJECT DIAGNOSTIC SUMMARY ===\n"
    
    for file_name in critical_files:
        summary += f"\n--- FILE: {file_name} ---\n"
        if os.path.exists(file_name):
            try:
                with open(file_name, "r", encoding="utf-8") as f:
                    content = f.read()
                    summary += content if content.strip() else "[EMPTY FILE]"
            except Exception as e:
                summary += f"[ERROR READING FILE: {e}]"
        else:
            summary += "[FILE NOT FOUND]"
        summary += "\n" + "="*30 + "\n"
    
    # Kütüphane kontrolü [cite: 2025-12-31]
    summary += "\n--- INSTALLED PACKAGES ---\n"
    try:
        import subprocess
        libs = subprocess.check_output(["pip", "freeze"]).decode()
        summary += libs
    except:
        summary += "[COULD NOT RETRIEVE LIBS]"
        
    return summary

if __name__ == "__main__":
    print("Generating diagnostic report...")
    report = generate_project_summary()
    
    with open("vyno_diagnostic_report.txt", "w", encoding="utf-8") as f:
        f.write(report)
        
    print("\n✅ Teşhis raporu 'vyno_diagnostic_report.txt' adıyla oluşturuldu.")
    print("Lütfen bu dosyanın içeriğini kopyalayıp bana buraya yapıştır.")