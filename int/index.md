---
abstract: This directory contains the playbook to create an intermediate CA.
authors: Xander Harris
date: 2024-03-08
title: Intermediate CA
---

## Intermediate CA Usage

```{code-block} shell
:caption: Create the root CA

ansible-playbook int/site.yml
```

```{index} ca; intermediate
```

### Intermediate CA Playbook
<!--
```{autoyaml} ca/site.yml
```
-->

```{literalinclude} site.yml
:language: yaml
:caption: intermediate ca
```
