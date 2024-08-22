---
abstract: This directory contains the playbook to sign a certificate.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2024-03-08
title: Sign a Cert
---

## Cert Signing Usage

```{code-block} shell
:caption: sign a certificate

ansible-playbook -t sign site.yml
```

```{index} certificate; sign
```

## Signing Playbook

```{autoyaml} roles/sign/tasks/main.yml
```

```{literalinclude} /roles/sign/tasks/main.yml
:language: yaml
:caption: sign a cert
```
