---
abstract: This directory contains the playbook to create the initial root CA.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2024-03-08
title: Root CA
---

## Root CA Usage

```{code-block} shell
:caption: Create the root CA

ansible-playbook -t ca site.yml
```

```{index} ca; playbook

```

### Root CA readme

```{toctree}
README
```

### Root CA Playbook

```{literalinclude} /roles/ca/tasks/main.yml
:language: yaml
:caption: root ca
```

```{codeauthor} xander harris <xandertheharris@gmail.com>

```

```{sectionauthor} xander harris <xandertheharris@gmail.com>

```
