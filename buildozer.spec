[app]
title = Pixel 11 Pro AI Camera
package.name = pixel11procamera
package.domain = com.pixel11pro.camera
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = CAMERA,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.accept_sdk_license_agreement = True

[buildozer]
log_level = 2
