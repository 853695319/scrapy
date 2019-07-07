Running Tesseract

Tesseract is a command-line program, so first open a terminal or command prompt. The command is used like this:
```
  tesseract imagename outputbase [-l lang] [-psm pagesegmode] [configfile...]
  
  l:\etc\Tesseract-OCR\tesseract.exe tesseracttest.jpg out
  
  out.txt => 
    This is some text, written in Arial, that will be read by
    Tesseract. Here are some symbols: !@#$%*&*()
```
So basic usage to do OCR on an image called 'myscan.png' and save the result to 'out.txt' would be:
```
  tesseract myscan.png out
```
Or to do the same with German:

```
  tesseract myscan.png out -l deu
```

It can even be used with multiple languages traineddata at a time eg. English and German:

```
  tesseract myscan.png out -l eng+deu
```

Tesseract also includes a hOCR mode, which produces a special HTML file with the coordinates of each word. This can be used to create a searchable pdf, using a tool such as Hocr2PDF. To use it, use the 'hocr' config option, like this:

```
  tesseract myscan.png out hocr
```

You can also create a searchable pdf directly from tesseract ( versions >=3.03):

```
  tesseract myscan.png out pdf
```

More information about the various options is available in the Tesseract manpage.