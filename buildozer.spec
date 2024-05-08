[app]
title = CharanApp
package.name = sampleapk
package.domain = org.novfensec
source.dir = .
source.include_exts = py,png,jpg,kv,txt,atlas
requirements = python3,kivy==2.1.0,kivymd==0.104.2,pillow==8.3.1
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1

# Android specific
fullscreen = 0
android.permissions = INTERNET

android.api = 31  # Adjusted to the appropriate API level
android.minapi = 21  # Adjusted to the appropriate minimum API level
android.archs = arm64-v8a, armeabi-v7a

# Automatically accept Android SDK license
android.accept_sdk_license = True

# Code signing (if applicable)
#android.keystore = /path/to/your.keystore
#android.keyalias = your-key-alias
#android.store_password = your-store-password
#android.key_password = your-key-password
