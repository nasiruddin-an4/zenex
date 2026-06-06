import os

html_files = [
    "business-email.html",
    "domains.html",
    "managed-cloud.html",
    "s3-bucket.html",
    "vps-hosting.html",
    "web-hosting.html",
    "zenexcloud-lambda.html"
]

for fname in html_files:
    if not os.path.exists(fname):
        print(f"File not found: {fname}")
        continue
    
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Update basic dropdown panel transition
    target1 = """.dropdown-panel {
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%) translateY(10px);
  width: 340px;
  background: #0f0f11;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: var(--r-lg);
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.65), inset 0 1px 0 rgba(255, 255, 255, 0.05);
  padding: 12px;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s cubic-bezier(0.16, 1, 0.3, 1), transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);"""
  
    replacement1 = """.dropdown-panel {
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%) translateY(10px);
  width: 340px;
  background: #0f0f11;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: var(--r-lg);
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.65), inset 0 1px 0 rgba(255, 255, 255, 0.05);
  padding: 12px;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s cubic-bezier(0.16, 1, 0.3, 1), transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  transition-delay: 0.25s;"""

    content = content.replace(target1, replacement1)

    # 2. Update basic dropdown panel hover transition delay reset
    target2 = """.nav-item:hover .dropdown-panel {
  opacity: 1;
  pointer-events: auto;
  transform: translateX(-50%) translateY(0);
}"""

    replacement2 = """.nav-item:hover .dropdown-panel {
  opacity: 1;
  pointer-events: auto;
  transform: translateX(-50%) translateY(0);
  transition-delay: 0s;
}"""

    content = content.replace(target2, replacement2)

    # 3. Update DO mega menu dropdown panel transition
    target3 = """.dropdown-panel.mega-menu-do {
  position: absolute;
  top: 100%;
  left: 40px;
  right: 40px;
  transform: translateY(10px);
  width: auto;
  max-width: 900px;
  margin: 0 auto;
  background: #09090b;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 16px;
  padding: 0;
  overflow: hidden;
  box-shadow: 0 24px 64px rgba(0, 0, 0, 0.8);
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s cubic-bezier(0.16, 1, 0.3, 1), transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);"""

    replacement3 = """.dropdown-panel.mega-menu-do {
  position: absolute;
  top: 100%;
  left: 40px;
  right: 40px;
  transform: translateY(10px);
  width: auto;
  max-width: 900px;
  margin: 0 auto;
  background: #09090b;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 16px;
  padding: 0;
  overflow: hidden;
  box-shadow: 0 24px 64px rgba(0, 0, 0, 0.8);
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s cubic-bezier(0.16, 1, 0.3, 1), transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  transition-delay: 0.25s;"""

    content = content.replace(target3, replacement3)

    # 4. Update DO mega menu hover transition delay reset
    target4 = """.nav-item-products:hover .dropdown-panel.mega-menu-do {
  opacity: 1;
  pointer-events: auto;
  transform: translateY(0);
}"""

    replacement4 = """.nav-item-products:hover .dropdown-panel.mega-menu-do {
  opacity: 1;
  pointer-events: auto;
  transform: translateY(0);
  transition-delay: 0s;
}"""

    content = content.replace(target4, replacement4)
    
    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully added delay: {fname}")

