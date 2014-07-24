#! /bin/bash
echo ""
echo "Get 5 first line of auth log and storing them into a 'tail5authlog' file."
# file : a changer si besoin
path=/root/scpy
file=tail5authlog
cd $path
tail -5 /var/log/auth.log > $file
echo "Done."
echo ""
