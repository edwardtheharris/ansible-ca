---
abstract: This directory contains the playbook to create an intermediate CA.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2024-03-08
title: Intermediate CA
---

## Intermediate CA Usage

```{code-block} shell
:caption: Create the root CA

ansible-playbook -t int site.yml
```

```{index} ca; intermediate
```

### Intermediate CA Playbook

```{autoyaml} roles/ca/tasks/site.yml
```

```{literalinclude} /roles/ca/tasks/site.yml
:language: yaml
:caption: intermediate ca
```
