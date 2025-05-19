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

## Certificate Sign Requirements

This role assumes the presence of [openssl](https://openssl.org) on an
[ArchLinux](https://artchlinux.org) system along with services that can
be verified by globally-untrusted authorities.

## Certificate Sign Role Variables

This role requires the following variables to be set.

````{list-table}
:header-rows: 1

- - variable
  - description
  - default
- - `sign_ca_san`
  - the subject alternative names for the ca
  - ```{code-block} yaml
    - DNS:ca.iana.org
    - email:user@iana.org
    ```
- - `sign_cert_san`
  - the subject altnerative names for the signed cert
  - ```{code-block} yaml
    - DNS:cert.iana.org
    - email:user@iana.org
    ```
- - `sign_common_name`
  - the common name to be associated with the signed cert
  - `cert.iana.org`
- - `sign_int_path_crt`
  - filesystem path to the intermediate authority cert
  - `/etc/ssl/root/int/certs/int.crt`
- - `sign_int_path_key`
  - filesystem path to the intermediate authority private key
  - `/etc/ssl/root/int/private/int.key`
- - `sign_int_san`
  - subject alternative names for the intermediate cert
  - ```{code-block} yaml
    - DNS:int.iana.org
    - email:user@iana.org
    ```
- - `sign_dirs`
  - a list of directories required by the signed cert
  - ```{code-block} yaml
    - /etc/ssl/root/int/private
    - /etc/ssl/root/int/certs
    - /etc/ssl/root/int/csr
    - /etc/ssl/root/int
    ```
- - `sign_path_crt`
  - path to the ca crt
  - `/etc/ssl/root/int/certs/iana.org.crt`
- - `sign_path_csr`
  - path to the certificate signing request
  - `/etc/ssl/root/int/csr/iana.org.csr`
- - `sign_path_key`
  - a list of subject alternative names for the ca
  - `/etc/ssl/root/int/private/iana.org.key`
````

## Dependencies

The following roles should have been run on the target
before using this role.

- edwardtheharris.ca]()
- [edwardtheharris.int]()

## Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

## License

[Unlicense](../../license.md)

## Author Information

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
