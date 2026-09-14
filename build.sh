#!/usr/bin/env bash
set -o errexit

mkdir -p /opt/render/project/src/image

if [ -d "/opt/render/project/src/image_seed" ]; then
    cp -rn /opt/render/project/src/image_seed/. /opt/render/project/src/image/
fi

python manage.py collectstatic --no-input
python manage.py migrate
