# docgenerator

## pre-requisites

- jumpscale 8.2 (https://github.com/Jumpscale/jumpscale_core8/tree/8.2.0)

## to install

- see install section in [docs](/docs/docgenerator.md)
- make sure you install caddy with required plugins: https://caddyserver.com/download
  - e.g. filemanager is required

## how to get started

```
#to generate example docs only
js 'j.tools.docgenerator.generateExamples()'
#to generate jumpscale docs & example docs
js 'j.tools.docgenerator.generateJSDoc()'
```

- will generate some example documentation site in /optvar/docgenerator
- will also start caddy in tmux (config file in /optvar/docgenerator/caddyfile)

do tmux to go into caddy session & see if its running
```
tmux -a
```

- to see result go to http://localhost:1313/

## docu

- [docs](/docs/docgenerator.md)

## library in

- https://github.com/Jumpscale/jumpscale_core8/tree/8.2.0/lib/JumpScale/tools/docgenerator
