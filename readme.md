---
abstract: These roles enable the geneation of a root and interemediate
  Certificate Auhtority as well as the creation and signing of server
  and client certificates.
authors: Xander Harris
date: 2024-03-08
title: Ansible CA Readme
---

[![Ansible Lint](https://github.com/edwardtheharris/ansible-ca/actions/workflows/ansible.yml/badge.svg)](https://github.com/edwardtheharris/ansible-ca/actions/workflows/ansible.yml)
[![Documentation](https://github.com/edwardtheharris/ansible-ca/actions/workflows/documentation.yml/badge.svg)](https://github.com/edwardtheharris/ansible-ca/actions/workflows/documentation.yml)
[![ShellCheck](https://github.com/edwardtheharris/ansible-ca/actions/workflows/shell.yml/badge.svg)](https://github.com/edwardtheharris/ansible-ca/actions/workflows/shell.yml)

## Assumptions

The default configuration assumes a vault password exists at
{file}`/etc/ansible/vault`. It also assumes the inventory file is in YAML format
and located at {file}`/etc/ansible/hosts.yaml`

### Fact Caching

The default configuration uses fact caching with Redis running on the controller
with the default port.

## Usage

This code was originally developed to automate generation of the PKI infrastructure
required by a bare-metal Kubernetes cluster as described by the [Kubernetes Usage](#kubernetes-usage)
section below.

It evolved into a general-purpose set of roles that can create an OpenSSL server
for use in verifying any sort of service that requires TLS.

The default {file}`site.yml` is shown below.

```{code-block} yaml
:language: yaml

- name: Create root CA
  hosts: localhost
  become: true
  roles:
    - role: ca
      tags:
        - ca
      vars:
        ca_common_name: ca.iana.org
        ca_dirs:
          - /etc/ssl/root/private
          - /etc/ssl/root/certs
          - /etc/ssl/root/csr
          - /etc/ssl/root
        ca_email: user@iana.org
        ca_localilty: Los Angeles
        ca_org: Internet Assigned Numbers Authority
        ca_org_unit: Engineering
        ca_path_key: /etc/ssl/root/private/ca.key
        ca_path_crt: /etc/ssl/root/certs/ca.crt
        ca_path_csr: /etc/ssl/root/csr/ca.csr
        ca_san:
          - DNS:ca.iana.org
          - email:user@iana.org
        ca_state: California
    - role: clean
      tags:
        - clean
      vars:
        ca_dirs:
          - /etc/ssl/root
- name: Create int CA
  hosts: localhost
  become: true
  roles:
    - role: int
      tags:
        - int
      vars:
        int_ca_host: localhost
        int_ca_san:
          - DNS:ca.iana.org
          - email:user@iana.org
        int_ca_path_crt: /etc/ssl/root/certs/ca.crt
        int_ca_path_key: /etc/ssl/root/private/ca.key
        int_dirs:
          - /etc/ssl/root/int/private
          - /etc/ssl/root/int/certs
          - /etc/ssl/root/int/csr
          - /etc/ssl/root/int
        int_path_key: /etc/ssl/root/int/private/int.key
        int_path_crt: /etc/ssl/root/int/certs/int.crt
        int_path_csr: /etc/ssl/root/int/csr/int.csr
        int_san:
          - DNS:int.iana.org
          - email:user@iana.org
- name: Sign End User Certificate
  hosts: localhost
  roles:
    - role: sign
      tags:
        - sign
      vars:
        sign_ca_san:
          - DNS:ca.iana.org
          - email:user@iana.org
        sign_cert_san:
          - DNS:cert.iana.org
          - email:user@iana.org
        sign_common_name: cert.iana.org
        sign_int_path_crt: /etc/ssl/root/int/certs/int.crt
        sign_int_path_key: /etc/ssl/root/int/private/int.key
        sign_int_san:
          - DNS:int.iana.org
          - email:user@iana.org
        sign_dirs:
          - /etc/ssl/root/int/certs
          - /etc/ssl/root/int/csr
          - /etc/ssl/root/int/private
          - /etc/ssl/root/int
        sign_path_crt: /etc/ssl/root/int/certs/iana.crt
        sign_path_csr: /etc/ssl/rott/int/csr/iana.csr
        sign_path_key: /etc/ssl/root/int/private/iana.key

```

To use this playbook you'd need to adjust the variable values to those suiting
your needs then you can either run the playbook all at once which should work,
though the author has had more success using the tags assigned to each role.

### Single Command

```{code-block} shell
ansible-playbook site.yml
```

### Tags Commands

```{code-block} shell
ansible-playbook -t root

ansible-playbook -t int

ansible-playbook -t sign
```

### Kubernetes Usage

You can find an example inventory file below, this inventory is intended
to house a Kubernetes cluster with a pair of control planes that are members
of a Samba Active Directory Domain that contains a pair of controllers and
is responsible for authentication, file, and routing services.

```{code-block} yaml
:caption: /etc/ansible/hosts.yaml

dc:
  hosts:
    dc01.example.com:
      ansible_user: user
    dc02.example.com:
      ansible_user: user
np:
  hosts:
    napalm.example.com:
      ansible_user: user
kcp:
  hosts:
    kcp01.example.com:
      ansible_user: user
    kcp02.example.com:
      ansible_user: user
ca:
  hosts:
    ca.example.com:
      ansible_user: user
      secret_ca_passphrase: secret-ca-passphrase
```

The remaining usage for a Kubernetes cluster should be roughly the same
as the general purpose usage above. You will need to deploy a CA
for your intended Kubernetes cluster and use that CA to create and sign
server and client certificates for both the Kubernetes services and the
required [etcd](https://github.com/edwardtheharris/ansible-etcd) cluster.
