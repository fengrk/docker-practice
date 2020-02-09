FROM rancher/k3s:v1.17.2-k3s1 

RUN crictl pull docker.io/coredns/coredns:1.6.3 && \
    crictl pull docker.io/istio/citadel:1.4.3 && \
    crictl pull docker.io/istio/examples-bookinfo-details-v1:1.15.0 && \
    crictl pull docker.io/istio/examples-bookinfo-productpage-v1:1.15.0 && \
    crictl pull docker.io/istio/examples-bookinfo-ratings-v1:1.15.0 && \
    crictl pull docker.io/istio/examples-bookinfo-reviews-v1:1.15.0 && \
    crictl pull docker.io/istio/examples-bookinfo-reviews-v2:1.15.0 && \
    crictl pull docker.io/istio/examples-bookinfo-reviews-v3:1.15.0 && \
    crictl pull docker.io/istio/galley:1.4.3 && \
    crictl pull docker.io/istio/kubectl:1.4.3 && \
    crictl pull docker.io/istio/mixer:1.4.3 && \
    crictl pull docker.io/istio/pilot:1.4.3 && \
    crictl pull docker.io/istio/proxyv2:1.4.3 && \
    crictl pull docker.io/istio/sidecar_injector:1.4.3 && \
    crictl pull docker.io/prom/prometheus:v2.12.0 && \
    crictl pull docker.io/rancher/klipper-lb:v0.1.2 && \
    crictl pull docker.io/rancher/local-path-provisioner:v0.0.11 && \
    crictl pull docker.io/rancher/metrics-server:v0.3.6 && \
    crictl pull docker.io/rancher/pause:3.1 && \
    crictl pull gcr.io/kubernetes-helm/tiller:v2.16.1
