[app]
title = Pixel 11 Pro AI Camera
package.name = pixel11pro
package.domain = org.pixel11pro.camera
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3,kivy,opencv, Pillow, numpy
orientation = portrait
fullscreen = 0
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True

[buildozer]
log_level = 2
warn_on_root = 1
