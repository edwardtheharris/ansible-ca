---
abstract: This directory contains the playbook to create the initial root CA.
authors: Xander Harris
date: 2024-03-08
title: Root CA
---

## Root CA Usage

```{code-block} shell
:caption: Create the root CA

ansible-playbook ca/site.yml
```

```{index} ca; playbook
```

### Root CA Playbook

```{literalinclude} site.yml
:language: yaml
:caption: root ca
```

There should be proper comments below this line.
<!--
```{ansible-task}
- include_tasks: ca/site.yml
```
-->
