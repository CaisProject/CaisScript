<img src="assets/CAIS\ Banner\ logo.png">
[![AppVeyor](https://img.shields.io/appveyor/ci/gruntjs/grunt.svg)](https://caispl.org/status/build)
[![License](https://img.shields.io/badge/license-GNU-green.svg)](https://caispl.org/license)
[![version](https://img.shields.io/badge/version-v1.0-orange.svg)](https://caispl.org/releases/recent)
[![platforms](https://img.shields.io/badge/platforms-macOS%20Mojave%20%7C%20Windows%2010%20%7C%20linux--64-blue.svg)](https://caispl.org/releases/recent)

# The CAIS programming language.
Made by [iAlex11](https://twitter.com/amvro_) the 7th June 2018.
Sponsored by HEMO Inc.

CAIS is an open-source programming language made for experimental purposes such us Platform testing, library, process and script developing.

CAIS is supposed to be a fast, easy and powerful programming language.

## What can you do with CAIS?

```
#use <cais>

write "Hello World!";
%awn = ask "What's your name? ";
if (%awn) not (empty) {
    write "Hello %i!".include(%awn)
}
exit;
```
### Finishing exceptions:
**0**: Program finished successfully following standart CAIS procedure of execution and didn't have any error.

**1**: Program finished successfully following framework procedure of execution and didn't have any error.

**2**: Program finished successfully following third-party procedure of execution and didn't have any error.
### Passing arguments from exit:
```
#use <cais>

$version = 1.0 // This is a constant, and constants can't be passed from exit.
_version_ = 1.0 // All variables starting with "_" are arguments.
_author_ = "iAlex11"

exit << _version_, _author_; // exit method can have additions.
```
Result:
```
CAIS: Program finished with exception O.
CAIS: Program finished with arguments 'version, author'.
CAIS: Object 'file' located at tests/test2.cai.
```
