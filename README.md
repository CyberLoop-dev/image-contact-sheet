<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:0f766e&height=160&section=header&text=Image%20Contact%20Sheet&fontSize=38&fontColor=ffffff" width="100%" alt="Image Contact Sheet banner" />
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=2800&pause=700&color=0F766E&center=true&vCenter=true&width=820&lines=Browse%20a%20whole%20image%20folder%20at%20a%20glance" alt="Animated project title" />
<p>Create labeled image contact sheets from a folder, with consistent thumbnails and a single shareable output.</p>
<p><img src="https://img.shields.io/github/license/CyberLoop-dev/image-contact-sheet?style=for-the-badge" alt="MIT license" /> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/image-contact-sheet?style=for-the-badge" alt="Top language" /> <img src="https://img.shields.io/github/stars/CyberLoop-dev/image-contact-sheet?style=for-the-badge" alt="Stars" /> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/image-contact-sheet?style=for-the-badge" alt="Last commit" /></p>
<img src="assets/illustration.svg" width="92%" alt="Image Contact Sheet illustration" />
</div>

## 🎯 Overview

Image Contact Sheet turns a folder of images into a labeled grid. It is useful for reviewing photo batches, comparing generated assets, or preparing a quick visual index. The tool reads images locally and writes one output image.

## ✨ Features

- 🖼️ Scans common image formats recursively.
- 📐 Fits thumbnails into consistent cells without stretching them.
- 🏷️ Adds readable filenames beneath each thumbnail.
- ⚙️ Lets you choose the number of columns and thumbnail dimensions.
- 🔒 Works locally; source images are never changed.

## 🎬 Demo

<pre><code>python main.py ./photos --output contact-sheet.jpg --columns 4</code></pre>

No hosted demo is claimed. Run the command locally to see the actual output.

## 🚀 Quick Start

<pre><code>python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python main.py ./photos --output contact-sheet.jpg</code></pre>

## 🧰 Tech Stack

- Python 3.10+
- Pillow for image decoding, resizing, and output

## 🗂️ Folder Structure

<pre><code>image-contact-sheet/
├── main.py
├── requirements.txt
└── assets/
    └── illustration.svg</code></pre>

## 🧭 Roadmap

- [ ] Add optional date-based grouping.
- [ ] Add a compact PDF export mode.
- [ ] Add configurable filename truncation and font sizing.

## 🤝 Contributing

Issues and pull requests are welcome. Keep changes focused, explain behavior changes, and include a reproducible example for bug reports.

## 📄 License

Released under the MIT License. See [LICENSE](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:111827&height=110&section=footer" width="100%" alt="Animated wave footer" /></div>
