[app]
title = Pixel11 Camera
package.name = pixel11camera
package.domain = org.test
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,Pillow
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreements = True
android.archs = arm64-v8a, armeabi-v7a
p4a.bootstrap = sdl2
