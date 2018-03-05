# docgenerator

## pre-requisites

- jumpscale 9 (https://github.com/Jumpscale/core9)
## to install

- see install section in [docs](/docs/docgenerator.md)

## how to get started

```
#to generate example docs only
js9 'j.tools.docgenerator.generateExamples()'
#to generate jumpscale docs & example docs
js9 'j.tools.docgenerator.generateJSDoc()'
```

- will generate some example documentation site in /optvar/docgenerator
- will also start caddy in tmux (config file in /optvar/docgenerator/caddyfile)

do tmux to go into caddy session & see if its running
```
tmux -a
```

- to see result go to http://localhost:8080/

## docu

- [docs](/docs/docgenerator.md)

## library in

- https://github.com/Jumpscale/jumpscale_core8/tree/8.2.0/lib/JumpScale/tools/docgenerator
