#/bin/bash

echo "===== line-notify.sh ====="
sed -i 's/${TOKEN}/${{TOKEN}}/g' lineNotify.py
python lineNotify.py "test post"
