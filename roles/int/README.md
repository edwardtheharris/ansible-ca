---
abstract: >-
  This role provides a functional intermediate certificate authority.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2025-05-13
title: Intermediate CA Readme
---

```{note}
[IANA](https://www.iana.org/) is used for default values, though this code is not affiliated with
that authority or any of its subsidiaries
```

## Requirements

You will need [OpenSSL](https://www.openssl.org/) on an [ArchLinux](https://archlinux.org)
system in order for this role
to work. If you want to use something other than Arch, you'll need to
update the [commmunity.general.pacman](https://docs.ansible.com/ansible/latest/collections/community/general/pacman_module.html#ansible-collections-community-general-pacman-module)
tasks to use the package manager
of your choice.

## Role Variables

This role requires the following variables to be set.

````{list-table}
:header-rows: 1

- - variable
  - description
  - default
- - `ca_dirs`
  - a list of directories required by the root ca
  - ```{code-block} yaml
    - /etc/ssl/root/private
    - /etc/ssl/root/certs
    - /etc/ssl/root/csr
    - /etc/ssl/root
    ```
- - `ca_email`
  - an email for use in the SAN and email fields
  - `user@email.com`
- - `ca_locality`
  - name of the municipality to be used for the ca
  - `Los Angeles`
- - `ca_org`
  - the organization the ca represents
  - `Internet Assigned Numbers Authority`
- - `ca_org_unit`
  - organization department used by the ca
  - `Engineering`
- - `ca_path_key`
  - path to the ca private key
  - `/etc/ssl/root/private/ca.key`
- - `ca_path_crt`
  - path to the ca crt
  - `/etc/ssl/root/certs/ca.crt`
- - `ca_path_csr`
  - path to the certificate signing request
  - `/etc/ssl/root/csr/ca.csr`
- - `ca_san`
  - a list of subject alternative names for the ca
  - `user@email.com`
- - `ca_state`
  - a state or region in which the ca was made
  - `California`
````

## Dependencies

You will need the following collections.

- [community.general](https://docs.ansible.com/ansible/latest/collections/community/general/index.html)
- [community.crypto](https://docs.ansible.com/ansible/latest/collections/community/crypto/index.html)

They can be installed using the bash below.

```{code-block} shell
:caption: install required collections

ansible-galaxy collection install {community.general,community.crypto}
```

## Example Playbook

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

```{code-block} yaml
:caption: example playbook

- name: Create root CA
  hosts: localhost
  become: true
  roles:
    - role: ca
      tags:
        - ca
        - private_key
      vars:
        ca_email: user@domain.com
        ca_locality: Los Angeles
        ca_org: IANA
        ca_org_unit: Engineering
        ca_san:
          - DNS:iana.domain.com
          - email:user@domain.com
        ca_state: California
```

## License

This software is {doc}`/license`

## Author Information

```{sectionauthor} Xander Harris <xandertheharris@gmail.com>

```
