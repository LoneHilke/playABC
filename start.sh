#!/usr/bin/env bash
set -o errexit

mkdir -p /opt/render/project/src/image

cp -rn /opt/render/project/src/image_seed/. /opt/render/project/src/image/

exec gunicorn play.wsgi:application