# Annotation Tool

This tool is originally based upon [BBox-Label-Tool](https://github.com/puzzledqs/BBox-Label-Tool), with many modifications, feature additions and error handling.


## Notes

* Can annotate for JPG, PNG and JPEG image formats.
* Can Annotate For Single or Multi Classes.
* Can Add a new class on runtime.
* `yoloconvertor.py` dedicated for converting bounding boxes to yolo format with classes.
* Easy configuration handling in `config.py`.
* Additional `process.py` for creating test.txt and train.txt files set.

## Installation

I would highly recommend using python virtual environment for installing dependencies used in python programming. For installation of python virtual environment one can follow the [guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

```bash
pip install -r requirements.txt
```

## Usage

```python

- For Annotations in Yolo format
  * Add configurations in config.py file
  * Add Images
  * python main.py
  * python yolocovertor.py

- For Process.py File
  * Change configuration inside the file, in Config part
  * python process.py
```
