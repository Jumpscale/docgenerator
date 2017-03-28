# docgenerator

## to install

- make sure you install caddy with required plugins: https://caddyserver.com/download
  - e.g. filemanager is required
- now follow install instructions on our docs (see below)
 

## how to get started

```
j.tools.docgenerator.generateExamples()
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
