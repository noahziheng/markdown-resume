FROM nginx:latest

COPY ./css /usr/share/nginx/html/css
COPY ./img /usr/share/nginx/html/img   
COPY ./index.html /usr/share/nginx/html/index.html
COPY ./resume.pdf /usr/share/nginx/html/resume.pdf