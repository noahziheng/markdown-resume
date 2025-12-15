#!/bin/sh
# script to build the resume in .html and .pdf.
# pandoc & wkhtmltopdf are required.

echo
echo 'Generate Markdown to HTML ...'
python -m pandoc -- -s -c css/design.css src/resume.md -o index.html
echo 'Done'

echo
echo 'Generate HTML to PDF ...'
python -m wkhtmltopdf -- --enable-local-file-access index.html resume.pdf

echo
echo 'Generate Markdown to HTML + Footer (Download Link) ...'
python -m pandoc -- -s -c css/design.css src/resume.md src/footer.md -o index.html
echo 'Done'

echo
echo 'Finish !'