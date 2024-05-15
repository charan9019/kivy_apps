[app]
title = CharanApp
package.name = charanapk
package.domain = org.novfensec
source.dir = .
source.include_exts = py,kv,png,jpg,atlas
requirements = python3,kivy==2.0.0
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1

[android]
fullscreen = 0
android.permissions = INTERNET
android.api = 30
android.minapi = 21
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.debug_artifact = apk
