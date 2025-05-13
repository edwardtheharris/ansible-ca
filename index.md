---
abstract: This is a collection of Ansible playbooks that will create a CA usable
  for Kubernetes and etcd clusters.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2024-03-08
title: Ansible CA
---

[![Ansible Lint](https://github.com/edwardtheharris/ansible-ca/actions/workflows/ansible.yml/badge.svg)](https://github.com/edwardtheharris/ansible-ca/actions/workflows/ansible.yml)
[![Documentation](https://github.com/edwardtheharris/ansible-ca/actions/workflows/documentation.yml/badge.svg)](https://github.com/edwardtheharris/ansible-ca/actions/workflows/documentation.yml)
[![ShellCheck](https://github.com/edwardtheharris/ansible-ca/actions/workflows/shell.yml/badge.svg)](https://github.com/edwardtheharris/ansible-ca/actions/workflows/shell.yml)

## Roles

```{toctree}
:maxdepth: 1
:caption: roles

roles/ca/index
roles/int/index
roles/sign/index
roles/secondary/index
```

```{index} playbooks; ca

```

## Readme

```{toctree}
:caption: other information
:maxdepth: 1

.github/index
readme
license
security
```

```{index} metadata; repository

```

## References

- [community.crypto.x509_certificate](https://docs.ansible.com/ansible/latest/collections/community/crypto/x509_certificate_module.html)
- [How to create a small CA](https://docs.ansible.com/ansible/latest/collections/community/crypto/docsite/guide_ownca.html)

## Indices and tables

- {ref}`genindex`
- {ref}`modindex`
- {ref}`search`
