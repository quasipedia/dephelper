DepHelper [Dependencies Helper]
===============================
__Copyright (C) 2011 Mac Ryan__


Description
-----------
This is a small script that I put together while experimenting with debian
packaging. It explore a source tree and find all imports that are performed in
the code.

It can then filter in a number of ways. The standard filter setting is such that
only imports of modules that are not in the python standard library or in the
source tree are returned. This translates as _external dependencies_ in most
cases.


Known limitations
-----------------
The script **only traces explicit import statements** in either form:
 - `import modulename`
 - `from modulename import something`
aliases `as`, comments `#` and multiple statements `;` are handled correctly.

In other words **metaprogrammed imports** which use the `imp` module or the
`__import__` functions or that evaluate strings with `eval` and `exec` are not
(yet?) handled.


ToDo's
------
The next step for the script will be to be able to link the module names used
during import to their respective debian packages, and to generate the
dependency file of the `debian/` directory automatically.


Licence [MIT]
-------------
Copyright (C) 2011 by Mac Ryan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
