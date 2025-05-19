---
abstract: >-
  This role uses the root and intermediate certificate authorities from
  the ca and int roles to sign a certificate that can be used for encrypted
  services.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2025-05-19
title: Certificate Signing Readme
---

## Requirements

This role assumes the presence of [openssl](https://openssl.org) on an
[ArchLinux](https://artchlinux.org) system along with services that can
be verified by globally-untrusted authorities.

## Role Variables

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
- - `sign_ca_san`
  - the subject alternative names for the ca
  - - `DNS:ca.iana.org`
    - `email:user@iana.org`
- - `sign_cert_san`
  - the subject altnerative names for the signed cert
  - - `DNS:cert.iana.org`
    - `email:user@iana.org`
- - `sign_int_path_crt`
  - filesystem path to the intermediate authority cert
  - `/etc/ssl/root/int/certs/int.crt`
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

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

## Dependencies

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

## Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

## License

BSD

## Author Information

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
