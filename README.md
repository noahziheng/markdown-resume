# markdown-resume

简历的**唯一数据源**是 `src/resume.md`，网页版和 PDF 都由它生成，不用手动维护两份内容。

```
src/resume.md   ──build──▶   index.html   （网页版，noahgao.net 直接托管）
                             resume.pdf   （A4 打印版，投递用）
```

## 为什么这样组织

- **只改一个文件**：内容和排版分离，改简历只动 Markdown，样式统一在 `css/design.css`。
- **产物自动重建**：推到 `master` 后 GitHub Actions 自动跑构建并把 `index.html` / `resume.pdf` 提交回来，不需要本地装环境。
- **本地也能一键出 PDF**：`./build.sh` 依赖很少（Python + 任意 Chromium 内核浏览器）。
- **支持多个投递版本**：换一个 Markdown 就能出针对不同岗位的版本，见下文。

## 本地构建

依赖：

```bash
pip install markdown          # 唯一 Python 依赖
# 浏览器：chromium / chromium-browser / google-chrome / google-chrome-stable 任一即可
```

构建：

```bash
./build.sh                    # src/resume.md -> index.html + resume.pdf
```

Python 不在默认路径时可以指定：

```bash
PYTHON=/path/to/python ./build.sh
```

## 多版本模式

不同岗位对关键词和叙事重点的要求不一样，用变体模式生成平行版本，互不覆盖：

```bash
./build.sh src/resume.md resume     # 主版本 -> index.html + resume.pdf
./build.sh src/agent.md  agent      # 变体   -> dist/agent.html + dist/agent.pdf
```

约定：

- `src/resume.md` 是主版本，产物固定在仓库根目录，供网站托管。
- 其它 Markdown 作为变体，产物落在 `dist/`（已加入 `.gitignore`），按需导出投递。

## 排版

`css/design.css` 是**打印优先**的主题：A4、单栏、中文排版优化、避免标题和列表被分页切断。
屏幕预览和打印共用同一份样式，`@media print` 里只做必要收紧。

## 部署

`Dockerfile` 把 `index.html`、`resume.pdf`、`css/`、`img/` 打包成 nginx 镜像，用于托管网页版。

## 文件说明

| 路径 | 作用 |
| --- | --- |
| `src/resume.md` | 简历正文（唯一数据源） |
| `css/design.css` | 打印优先主题 |
| `scripts/build.py` | Markdown -> HTML -> PDF 构建器 |
| `build.sh` | 构建入口 |
| `.github/workflows/build.yml` | CI：push 后自动重建产物 |
| `index.html` / `resume.pdf` | 构建产物，勿手改 |
