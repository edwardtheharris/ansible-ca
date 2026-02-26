---
abstract: This role cleans up previous ca deployments.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2025-05-22
title: CA clean
---

A small role to clean up CA directories.

## CA Clean Requirements

Some CA directories to clean up.

## CA Clean Role Variables

| name      | description                    | default           |
| --------- | ------------------------------ | ----------------- |
| `ca_dirs` | a list of directories to clean | `- /etc/ssl/root` |

## CA Clean Dependencies

None.

## CA Clean Example Playbook

Usage of this one is simple.

```{code-block} yaml

- hosts: localhost
  become: true
  roles:
    - role: clean
      tags:
        - clean
      vars:
        ca_dirs:
          - /etc/ssl/root
```

## CA Clean License

MIT

## Author Information

```{sectionauthor} Xander Harris <xandertheharris@gmail.com>

```
