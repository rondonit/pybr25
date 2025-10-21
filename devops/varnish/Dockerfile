# syntax=docker/dockerfile:1
FROM varnish:7.6

LABEL maintainer="rondonit <gabriel.cruz@ecomp.ufsm.br>" \
      org.label-schema.name="pybr25-varnish" \
      org.label-schema.description="Tutorial Python Brasil Varnish image." \
      org.label-schema.vendor="rondonit"

COPY etc/varnish.vcl /etc/varnish/default.vcl
