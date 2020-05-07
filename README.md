# To build 1 variant

> pip install virtualenv
> virtualenv mypython
> source mypython/bin/activate
> pip install -r requirements

## 3 arguments required:
1) path to origin html file
2) path to other html file
3) name of tag id in origin html file

# To run
> python app.py templates/sample-0-origin.html templates/sample-1-evil-gemini.html make-everything-ok-button
> python app.py templates/sample-0-origin.html templates/sample-2-container-and-clone.html make-everything-ok-button
> python app.py templates/sample-0-origin.html templates/sample-3-the-escape.html make-everything-ok-button
> python app.py templates/sample-0-origin.html templates/sample-4-the-mash.html make-everything-ok-button

# To run all files

> python run_all_templates.py


# To build and run all files 2 variant

> docker build -t analyzer_html:latest .
> docker run analyzer_html:latest 