---
abstract: This is a collection of Ansible playbooks that will create a CA usable
   for Kubernetes and etcd clusters.
authors:
   - name: Xander Harris
     email: xandertheharris@gmail.com
date: 2024-03-08
title: Ansible CA
---

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/edwardtheharris/ansible-k8s-ca/ansible.yml?branch=main&style=flat-square&logo=ansible&label=Ansible%20Lint)
![GitHub CodeQL](https://img.shields.io/github/actions/workflow/status/edwardtheharris/ansible-k8s-ca/codeql.yml?branch=main&style=flat-square&logo=githubactions&label=CodeQL)
[![GitHub Pages Status](https://img.shields.io/github/actions/workflow/status/edwardtheharris/ansible-k8s-ca/pages.yml?branch=main&style=flat-square&logo=githubpages&label=GitHub%20Pages)](https://edwardtheharris.github.io/ansible-k8s-ca/)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/edwardtheharris/ansible-k8s-ca/shell.yml?branch=main&style=flat-square&logo=gnubash&label=ShellCheck)

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
