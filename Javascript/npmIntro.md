### Basic commands of NPM
#### Linus, 2018/10/07 10pm
#### This article will help you understand
1. what npm is
2. Install/remove packages
3. create packages

---

```
$ which node
/usr/bin/node
$ node --version
v6.10.3

Changing the Location of Global Packages

$ npm config list
; cli configs
user-agent = "npm/3.10.10 node/v6.10.3 linux x64"

; userconfig /home/sitepoint/.npmrc
prefix = "/home/sitepoint/.node_modules_global"

; node bin location = /usr/bin/nodejs
; cwd = /home/sitepoint
; HOME = /home/sitepoint
; "npm config ls -l" to show all defaults.
```


### The output however, is rather verbose. We can change that with the -- depth=0 option.

    $ npm list -g --depth=0

### Any packages installed globally will become available from the command line. For example, here’s how you would use the Uglify package to minify example.js into example.min.js:

    $ uglifyjs example.js -o example.min.js

### Installing Packages in Local Mode
    $ npm init

#### Tip: If you want a quicker way to generate a package.json file use npm init --y



### let’s try and install Underscore.

    $ npm install underscore
    semantic versioning. The caret (^) at the front of the version number indicates that when installing ^1.8.3


### removes package globally
    $ npm -g uninstall <packagename>



### Installing a Specific Version of a Package
    $ npm install underscore@1.8.2


### Updating a Package

```
$ npm outdated
Package     Current  Wanted  Latest  Location
underscore    1.8.2   1.8.3   1.8.3  project

$ npm update underscore
```


### Searching for Packages
    $ npm search <packagename>

### Re-installing Project Dependencies

    $ npm install request

### Note the dependencies list got updated automatically. In previous versions of npm, you would have had to execute npm install request --save to save the dependency in package.json.

### If you wanted to install a package without saving it in package.json, just use --no-save argument.

```
$ rm -R node-modules
$ npm list
project@1.0.0 /home/sitepoint/project
├── UNMET DEPENDENCY mkdirp@^0.5.1
├── UNMET DEPENDENCY request@^2.81.0
└── UNMET DEPENDENCY underscore@^1.8.2

npm ERR! missing: mkdirp@^0.5.1, required by project@1.0.0
npm ERR! missing: request@^2.81.0, required by project@1.0.0
npm ERR! missing: underscore@^1.8.2, required by project@1.0.0

$ npm install
added 57 packages in 1.595s
```


### Managing the Cache
When npm installs a package it keeps a copy, so the next time you want to install that package, it doesn’t need to hit the network. The copies are cached in the .npm directory in your home path.

    $ ls ~/.npm


### This directory will get cluttered with old packages over time, so it’s useful to clean it up occasionally.

    $ npm cache clean


### You can also purge all node_module folders from your workspace if you have multiple node projects on your system you want to clean up.

    $ find . -name "node_modules" -type d -exec rm -rf '{}' +
    $ find . -name "linus"


### Aliases

```
npm i <package> – install local package
npm i -g <package> – install global package
npm un <package> – uninstall local package
npm up – npm update packages
npm t – run tests
npm ls – list installed modules
npm ll or npm la – print additional package information while listing modules
```


### Installs multiple packages at once

    $ npm i express momemt lodash mongoose body-parser webpack
