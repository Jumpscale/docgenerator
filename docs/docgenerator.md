
# docgenerator

process all markdown files in a git repo, write a summary.md file
optionally call pdf gitbook generator to produce pdf(s)

# install required components

```
js 'j.tools.docgenerator.installDeps()'
```

- IMPORTANT: need to check if all right plugins are installed of caddy e.g. the filemanager, if not do it manually

# process

## arguments are

- outdirectory: ```j.tools.docgenerator.outdir=...```
- url of site where docs will be: ```j.tools.docgenerator.webserver=...```

## preprocess

- docgenerator walks over all directories below a dir
- docgenerator remembers when a .git repo & get's the url path
- docgenerator identifies following types of dirs
    - macros
        - each dir called macros is considered to be a macros dir
    - documentation
        - file ```.docs``` is in the root of such a dir
        - files in here can be definitions, documents, blogs, ...
        - config.toml defines how to deal with the info in such a directory
    - the directories are remembered together with their git counterparts
- now all macro's are loaded
- now all filenames are remembered (this is to let the include work)

## process per doc directory (as found in previous step)

- walk over files in directory (recursive)
- for each dir we will check
    - data.toml
    - default.md
- these are remembered and will be applied on each markdown document (so you have hugo template variables available)
- walk over the .md files and for each file
    - execute the macro's  (recursive until no more macro's to be processed)
    - the aggregated data (is a dict) is put as toml metadata at beginning of the markdown document
- write resulting .md files to outdirectory/$sitename/content/...
    - this depends on the template used, std is a neutral template with no branding
- per site do the production step
    - lookup template used, copy inside $outdir/$sitename
    - use hugo or ... to generate the site (depends on the generate.py which is put in the template dir)

# metadata

## config.toml

- in root of each .doc directory there needs to be a config.toml
    - this config file is the hugo config file but also has some arguments for our own generation (see below)
- our own arguments
    - depends (will fetch & process other mentioned locations, can be subsection of a repo or full branch)
    - name is meaning full name of the Documentation part e.g js8_defs
    - description e.g. definitions of jumpscale

```toml
name = "js8_lots"
description = "some description"
depends = ["https://github.com/Jumpscale/jumpscale_core8/tree/8.1.2/docs",
    "https://github.com/Jumpscale/jscockpit",
    "https://github.com/Jumpscale/ays_jumpscale8/tree/8.2.0"]
theme = "hugo-future-imperfect"
```
