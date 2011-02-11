#!/bin/sh
cd generated
tar -czf - *.html | ssh dmethods@dmethods.com "cd /home/dmethods/www/collection; tar xzf -"
cd ..