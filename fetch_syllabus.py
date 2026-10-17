import urllib.request
import re
import json
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
url = 'https://gate2027.iitm.ac.in/exam_papers_and_syllabus'

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

with open('syllabus_page.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved syllabus_page.html. Length:", len(html))

# Search for all links
links = re.findall(r'<a\s+(?:[^>]*?\s+)?href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html, re.DOTALL | re.IGNORECASE)
print(f"Total links found: {len(links)}")

cs_links = []
for href, text in links:
    clean_text = ' '.join(re.sub(r'<[^>]+>', ' ', text).split())
    if any(k in href.lower() or k in clean_text.lower() for k in ['cs', 'computer', 'syllabus', '.pdf']):
        cs_links.append({'text': clean_text, 'href': href})
        print(f"Match: {clean_text} -> {href}")

with open('cs_links.json', 'w', encoding='utf-8') as f:
    json.dump(cs_links, f, indent=2)
