#!/usr/bin/env python3
"""构建简历：Markdown -> HTML -> PDF。

用法：
    python3 scripts/build.py                        # src/resume.md -> index.html + resume.pdf
    python3 scripts/build.py src/agent.md agent     # 变体 -> dist/agent.html + dist/agent.pdf

依赖：
    pip install markdown
    chromium / chromium-browser / google-chrome / google-chrome-stable 任一在 PATH 中
"""

from __future__ import annotations

import html
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BROWSERS = ("chromium", "chromium-browser", "google-chrome", "google-chrome-stable")

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="author" content="{author}">
<meta name="description" content="{description}">
<title>{title}</title>
<link rel="stylesheet" href="{css}">
</head>
<body>
<main class="page">
{body}
</main>
</body>
</html>
"""


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    """极简 front matter 解析：只支持 `key: value`，够用即可。"""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    meta: dict[str, str] = {}
    for line in text[3:end].strip("\n").splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip()
    return meta, text[end + 4:].lstrip("\n")


def find_browser() -> str:
    for name in BROWSERS:
        path = shutil.which(name)
        if path:
            return path
    sys.exit("找不到浏览器（chromium / google-chrome），无法生成 PDF。")


def render_html(md_path: Path, css_rel: str) -> str:
    try:
        import markdown
    except ImportError:
        sys.exit("缺少依赖：markdown。请先运行 pip install markdown")

    meta, body_md = parse_front_matter(md_path.read_text(encoding="utf-8"))
    body = markdown.markdown(body_md, extensions=["extra", "sane_lists", "attr_list"])
    return HTML_TEMPLATE.format(
        lang=meta.get("lang", "zh-CN"),
        title=html.escape(meta.get("title", "Resume")),
        author=html.escape(meta.get("author", "")),
        description=html.escape(meta.get("description", "")),
        css=css_rel,
        body=body,
    )


def html_to_pdf(html_path: Path, pdf_path: Path) -> None:
    subprocess.run(
        [
            find_browser(),
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            "--virtual-time-budget=10000",
            f"--print-to-pdf={pdf_path}",
            html_path.resolve().as_uri(),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def main() -> None:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "src" / "resume.md"
    name = sys.argv[2] if len(sys.argv) > 2 else "resume"
    if not src.is_absolute():
        src = ROOT / src
    if not src.exists():
        sys.exit(f"找不到源文件：{src}")

    is_default = name == "resume"
    out_dir = ROOT if is_default else ROOT / "dist"
    out_dir.mkdir(parents=True, exist_ok=True)

    html_path = out_dir / ("index.html" if is_default else f"{name}.html")
    pdf_path = out_dir / ("resume.pdf" if is_default else f"{name}.pdf")
    # 根目录产物用 css/design.css，dist/ 产物用 ../css/design.css
    css_rel = "css/design.css" if is_default else "../css/design.css"

    html_path.write_text(render_html(src, css_rel), encoding="utf-8")
    print(f"HTML  -> {html_path.relative_to(ROOT)}")
    html_to_pdf(html_path, pdf_path)
    print(f"PDF   -> {pdf_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
