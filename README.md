# markdown-resume
The simplest possible resume workflow from markdown source.

Changing the content or styling of a resume or CV is a relatively common event that can be a frustrating, time-consuming hassle. This repo contains starter files for the simplest possible workflow where resume *content* is maintained in a simple markdown file and generating `.html` and `.pdf` output formats can be automated with two tools: `pandoc` and `wkhtmltopdf`. 

**Still trying to decide if this is the workflow for you? Here are the original markdown files and the two output files for your persual**: 

[Markdown](resume.md) . [HTML](resume.html) . [PDF](resume.pdf) . [Preview](https://resume.jvincent.eu)

We'll need just two tools. Pandoc: the swiss army knife of interconverting file formats, and wkhtmtopdf the precision scalpel (?) of printing HTML to PDFs. Here is the simplest workflow:

Use pandoc to convert .md to .html, with styling via a .css file
Use wkhtmltopdf to print .html as .pdf

## Convert .md to .html
```sh
pandoc -c design.css -o resume.html -s resume.md
```

## Convert .html to .pdf
```sh
wkhtmltopdf resume.html resume.pdf
```



