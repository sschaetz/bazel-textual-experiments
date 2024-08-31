#!/usr/bin/env bash
set -euo pipefail

bazel build //src:example_tar

# Untar the example.tar file to the staging directory
mkdir -p /tmp/staging/extracted 
tar -xvf bazel-bin/src/example_tar.tar -C /tmp/staging/extracted

# Create the new app package
mkdir -p /tmp/staging/example.app/Contents/MacOS
mkdir -p /tmp/staging/example.app/Contents/Resources

# Create the Info.plist
pushd /tmp/staging/example.app/Contents
/usr/libexec/PlistBuddy -c "Add :CFBundleIdentifier string com.example.com.example" Info.plist
/usr/libexec/PlistBuddy -c "Add :CFBundleExecutable string Example" Info.plist

# Copy the executable
cp /tmp/staging/extracted/example \
  /tmp/staging/example.app/Contents/MacOS/example
cp -r /tmp/staging/extracted/example.runfiles \
  /tmp/staging/example.app/Contents/MacOS/example.runfiles

# Copy the runfiles. 
cp -r /tmp/staging/extracted/example.runfiles/* /tmp/staging/example.app/Contents/Resources/

# Move any shared libraries to the MacOS directory
find /tmp/staging/extracted/ -name "*.dylib" -exec mv {} /tmp/staging/example.app/Contents/MacOS \;

# Make everything writeable
chmod -R +w /tmp/staging/example.app/

# codesign the app bundle
codesign -s '-' -f /tmp/staging/example.app 
popd
