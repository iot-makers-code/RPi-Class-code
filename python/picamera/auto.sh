rm camera/*
python elapse.py  &

cd camera
python -m SimpleHTTPServer 8000  &
