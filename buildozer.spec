[app]

# (str) Title of your application
title = CharanApp

# (str) Package name
package.name = charanapk

# (str) Package domain (needed for android/ios packaging)
package.domain = org.novfensec

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,kv,png,jpg,atlas

# (list) Application requirements
requirements = python3,kivy==2.0.0

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

[android]

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
#android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
#android.api = 27

# (int) Minimum API your APK / AAB will support.
#android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 23b

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
android.accept_sdk_license = True

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# In past, was `android.arch` as we weren't supporting builds for multiple archs at the same time.
android.archs = arm64-v8a, armeabi-v7a

# (str) The format used to package the app for release mode (aab or apk or aar).
# android.release_artifact = aab

# (str) The format used to package the app for debug mode (apk or aar).
# android.debug_artifact = apk
