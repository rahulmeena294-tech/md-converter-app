[app]
title = MD Converter
package.name = mdconverter
package.domain = org.mdconverter
icon.filename = %(source.dir)s/assets/icon.png

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xlsx,xls,csv,docx,pdf,txt
source.include_patterns = assets/*,images/*

version = 0.1

requirements = python3,kivy,pandas,openpyxl,python-docx,pdfplumber,tabulate

orientation = portrait
fullscreen = 0

# Android specific
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# Logging
log_level = 2

# Build settings
p4a.branch = master