#!/usr/bin/env bash
set -euo pipefail

# Check if an output location argument is provided
if [ $# -eq 0 ]; then
    echo "Error: Please provide an output path for the app bundle."
    echo "Usage: $0 <output>"
    exit 1
fi

# Store the output location
output=$(cd "$(dirname "$1")" && pwd)/$(basename "$1")

# Create a temporary directory that will be automatically removed when the script exits
temp_dir=$(mktemp -d)
trap 'rm -rf "$temp_dir"' EXIT

bazel build //src:example_tar

# Untar the example.tar file to the staging directory
mkdir -p "$temp_dir/extracted"
tar -xvf bazel-bin/src/example_tar.tar -C "$temp_dir/extracted"

# Create the new app package
mkdir -p "$temp_dir/example.app/Contents/MacOS"
mkdir -p "$temp_dir/example.app/Contents/Resources"

# Create the Info.plist
pushd "$temp_dir/example.app/Contents"
/usr/libexec/PlistBuddy -c "Add :CFBundleIdentifier string com.example.com.example" Info.plist
/usr/libexec/PlistBuddy -c "Add :CFBundleExecutable string Example" Info.plist

# Copy the executable
cp "$temp_dir/extracted/example" \
  "$temp_dir/example.app/Contents/MacOS/example"
cp -r "$temp_dir/extracted/example.runfiles" \
  "$temp_dir/example.app/Contents/MacOS/example.runfiles"

# Copy the runfiles. 
cp -r "$temp_dir/extracted/example.runfiles/"* "$temp_dir/example.app/Contents/Resources/"

# Move any shared libraries to the MacOS directory
find "$temp_dir/extracted/" -name "*.dylib" -exec mv {} "$temp_dir/example.app/Contents/MacOS" \;

# Make everything writeable
chmod -R +w "$temp_dir/example.app/"

# codesign the app bundle
#codesign -s '-' -f "$temp_dir/example.app"

mv "$temp_dir/example.app" $output

popd
