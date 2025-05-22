---
abstract: This directory contains the playbook to clean old CA files.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2025-05-22
title: CA Clean
---

## CA Clean Usage

```{code-block} shell
:caption: Create the root CA

ansible-playbook -t ca site.yml
```

```{index} ca; playbook

```

### CA Clean readme

```{toctree}
README
```

### CA Clean Playbook

```{literalinclude} /roles/clean/tasks/main.yml
:language: yaml
:caption: ca clean
```

```{codeauthor} xander harris <xandertheharris@gmail.com>

```

```{sectionauthor} xander harris <xandertheharris@gmail.com>

```
