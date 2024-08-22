---
abstract: This directory contains the playbook to create an intermediate CA.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2024-03-08
title: Secondary Intermediate CA
---

## Secondary Intermediate CA Usage

```{code-block} shell
:caption: Create the secondary CA

ansible-playbook -t secondary site.yml
```

```{index} ca; intermediate
```

### Secondary Intermediate CA Playbook

```{autoyaml} roles/secondary/tasks/main.yml
```

```{literalinclude} /roles/secondary/tasks/main.yml
:language: yaml
:caption:
```
