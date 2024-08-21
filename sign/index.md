---
abstract: This directory contains the playbook to sign a certificate.
authors: Xander Harris
date: 2024-03-08
title: Sign a Cert
---

## Cert Signing Usage

```{code-block} shell
:caption: sign a certificate

ansible-playbook sign/site.yml
```

```{index} certificate; sign
```

## Signing Playbook
<!--
```{autoyaml} sign/site.yml
```
-->

```{literalinclude} site.yml
:language: yaml
:caption: sign a cert
```
