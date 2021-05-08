# import docx

# doc = docx.Document()
# doc.add_paragraph(f"This morning, Joey woke up at 6.")
# doc.add_paragraph(f"Her first nap should be at 9.")
# doc.add_paragraph(f"For lunch today, we have blues.")
# doc.add_paragraph(f"For dinner today, we have red.")
# doc.add_paragraph(f"As a reminder to do do do.")
# doc.save("nannyinfo.docx")
import subprocess

subprocess.Popen(["C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE", "nannyinfo.docx", "/mFileExit", "/mFileCloseOrExit"]).communicate()