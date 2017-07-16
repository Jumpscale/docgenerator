
# title of this doc

- is below including some other doc

```
!!!include("test5")
```

```
!!!include("ays9:events")
```

## example where we have link to original


```
!!!include("whatis:dual license strategy")

```

[source link](https://docs.greenitglobe.com/company30/whatis/src/master/Dual%20license%20strategy.md) 

this link will not be used when generating a doc, is just to make it easy to edit

## source of this test doc

```
# title of this doc

- is below including some other doc

\`\`\`
!!!include("test5")
\`\`\`

#next will include events doc from ays9 repo
\`\`\`
!!!include("ays9:events")
\`\`\`

\`\`\`
!!!include("whatis:dual license strategy")
\`\`\`

[source link](https://docs.greenitglobe.com/company30/whatis/src/master/Dual%20license%20strategy.md) 

this link will not be used when generating a doc, is just to make it easy to edit


```


```toml
!!!
title = "IncludeTest"
date = "2017-03-02"
tags= ["test"]
```
