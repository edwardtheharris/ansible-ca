#!/bin/bash

ocsp_domain=ocsp.example.com
ssl_domain=your.example.com
test_domain=test.example.com

openssl req -config openssl.cnf \
  -key private/${ssl_domain}.key.pem \
  -new -sha256 -out csr/${ssl_domain}.csr.pem

openssl ca -config openssl.cnf \
  -extensions server_cert -days 375 -notext -md sha256 \
  -in csr/${ssl_domain}.csr.pem \
  -out certs/${ssl_domain}.cert.pem

openssl x509 -noout -text \
  -in certs/${ssl_domain}.cert.pem

openssl genrsa \
  -out private/${ocsp_domain}.key.pem 4096

openssl req -config int.cnf -new \
  -key private/${ocsp_domain}.key.pem \
  -out csr/${ocsp_domain}.csr.pem

openssl ca -config int.cnf \
  -extensions ocsp -days 375 -notext -md sha256 \
  -in csr/${ocsp_domain}.csr.pem \
  -out certs/${ocsp_domain}.cert.pem

# Test OCSP

openssl genrsa -out private/${test_domain}.key.pem 4096
openssl req -config openssl.cnf \
  -key private/${test_domain}.key.pem \
  -new -out csr/${test_domain}.csr.pem
openssl ca -config openssl.cnf \
  -extensions server_cert -days 375 -notext \
  -in csr/${test_domain}.csr.pem \
  -out certs/${test_domain}.cert.pem

openssl ocsp -port 127.0.0.1:2560 -text -sha256 \
  -index index.txt \
  -CA certs/ca-chain.cert.pem \
  -rkey private/${ocsp_domain}.key.pem \
  -rsigner certs/${ocsp_domain}.cert.pem \
  -nrequest 1

openssl ocsp -CAfile certs/ca-chain.cert.pem \
  -url http://127.0.0.1:2560 -resp_text \
  -issuer certs/intermediate.cert.pem \
  -cert certs/${test_domain}.cert.pem
