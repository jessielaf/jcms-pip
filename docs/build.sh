sphinx-apidoc -o . ../jcms -f
mv modules.rst index.rst
sphinx-build -b html . _build
