#!/bin/sh
# script to build the resume in .html and .pdf.
# pandoc & wkhtmltopdf are required.

echo
echo 'Generate Markdown to HTML ...'
pandoc -s -c css/design.css src/resume.md -o resume.html
echo 'Done'

echo
echo 'Generate HTML to PDF ...'
wkhtmltopdf resume.html resume.pdf

echo
echo 'Generate Markdown to HTML + Footer (Download Link) ...'
pandoc -s -c css/design.css src/resume.md src/footer.md -o resume.html
echo 'Done'

echo
echo 'Finish !'